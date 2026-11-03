#!/usr/bin/env python3
"""Laboratoire pédagogique local, bibliothèque standard Python 3.10+.

Ce modèle émet de vrais échanges HTTP sur loopback. L'identité est un
contrôle de disponibilité simulé, pas une implémentation SSO de production.
"""
import argparse
import csv
import hashlib
import io
import json
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import ProxyHandler, Request, build_opener

ROOT = Path(__file__).resolve().parent
DEFAULT_STATE = ROOT / "runtime"
FIELDS = ["commande", "client", "quantite", "statut"]
INITIAL = [
    {"commande": "C001", "client": "Client-A", "quantite": "4", "statut": "prete"},
    {"commande": "C002", "client": "Client-B", "quantite": "3", "statut": "en_cours"},
    {"commande": "C003", "client": "Client-C", "quantite": "2", "statut": "prete"},
]
LOCK = threading.RLock()
HTTP = build_opener(ProxyHandler({}))


def now():
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def atomic(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(text.encode("utf-8"))
    temporary.replace(path)


def defaults(base):
    return {
        "base_port": base,
        "disabled": [],
        "routes": {"portail": base + 1, "commandes": base + 2},
        "auth_ports": {"portail": [base + 3], "commandes": [base + 3]},
    }


def read_config(state):
    config = json.loads((state / "config.json").read_text(encoding="utf-8"))
    return validate_config(config)


def validate_config(config):
    base = config["base_port"]
    if not isinstance(base, int) or not 1024 <= base <= 65520:
        raise ValueError("base_port invalide")
    for role in ("portail", "commandes"):
        ports = [config["routes"][role]] + config["auth_ports"][role]
        if not all(isinstance(p, int) and 1024 <= p <= 65535 for p in ports):
            raise ValueError("Port de laboratoire invalide")
    if not set(config["disabled"]).issubset({"edge", "portail", "commandes", "idp", "idp_backup"}):
        raise ValueError("Rôle désactivé inconnu")
    return config


def save_config(state, config):
    atomic(state / "config.json", json.dumps(config, ensure_ascii=False, indent=2) + "\n")


def csv_text(rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def parse_orders(text):
    reader = csv.DictReader(io.StringIO(text))
    if reader.fieldnames != FIELDS:
        raise ValueError("En-tête CSV attendu : " + ",".join(FIELDS))
    rows = list(reader)
    identifiers = set()
    for row in rows:
        if None in row or any(row.get(k) is None for k in FIELDS):
            raise ValueError("Ligne CSV mal formée")
        if not row["commande"] or row["commande"] in identifiers:
            raise ValueError("Identifiant de commande vide ou dupliqué")
        identifiers.add(row["commande"])
        if not row["quantite"].isdigit() or int(row["quantite"]) <= 0:
            raise ValueError("Quantité entière positive requise")
        if row["statut"] not in {"prete", "en_cours", "expediee"}:
            raise ValueError("Statut inconnu")
    return rows


def orders(state):
    return parse_orders((state / "commandes.csv").read_bytes().decode("utf-8-sig"))


def event(state, service, path, status, detail):
    with LOCK:
        with (state / "events.jsonl").open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"timestamp_utc": now(), "service": service,
                                     "path": path, "status": status, "detail": detail},
                                    ensure_ascii=False) + "\n")


def initialize(state, base, confirm=False):
    if (state / "config.json").exists() and not confirm:
        raise ValueError("État existant : utiliser reset --confirm pour le réinitialiser")
    state.mkdir(parents=True, exist_ok=True)
    save_config(state, defaults(base))
    atomic(state / "commandes.csv", csv_text(INITIAL))
    event(state, "controle", "reset", 200, "État de démonstration initialisé ; journaux conservés")


def request_local(port, path, timeout=1.0):
    request = Request(f"http://127.0.0.1:{port}{path}", headers={"Cache-Control": "no-cache"})
    try:
        with HTTP.open(request, timeout=timeout) as response:
            return response.status, response.read().decode("utf-8"), response.headers.get("Content-Type", "")
    except HTTPError as error:
        return error.code, error.read().decode("utf-8"), error.headers.get("Content-Type", "")
    except (URLError, TimeoutError, OSError) as error:
        return 599, str(error), "text/plain"


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_args):
        pass

    def reply(self, status, payload, detail="", content_type="application/json; charset=utf-8"):
        text = payload if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False)
        data = text.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        try:
            self.wfile.write(data)
        except (BrokenPipeError, ConnectionResetError):
            pass
        event(self.server.state, self.server.role, self.path, status, detail)

    def do_GET(self):
        state, role = self.server.state, self.server.role
        path = urlsplit(self.path).path
        try:
            config = read_config(state)
            if role in config["disabled"]:
                self.reply(503, {"service": role, "error": "service_indisponible"}, "indisponibilité injectée")
                return
            if path == "/health":
                self.reply(200, {"service": role, "listener": "up"}, "Santé locale, sans test des dépendances")
                return
            if role in {"idp", "idp_backup"}:
                if path != "/validate":
                    self.reply(404, {"error": "route_inconnue"})
                else:
                    self.reply(200, {"training_identity": "student", "provider": role},
                               "Identité fictive ; aucun mot de passe traité")
                return
            if role == "edge":
                if path == "/":
                    self.reply(200, {"service": "edge", "routes": ["/portail", "/commandes", "/commandes/export"]})
                    return
                name = path.strip("/").split("/")[0]
                if name not in config["routes"]:
                    self.reply(404, {"error": "route_inconnue"})
                    return
                backend_path = "/export" if path == "/commandes/export" else "/"
                code, body, ctype = request_local(config["routes"][name], backend_path)
                self.reply(502 if code == 599 else code, body, "upstream=" + str(config["routes"][name]), ctype)
                return
            if path not in {"/", "/export"} or (path == "/export" and role != "commandes"):
                self.reply(404, {"error": "route_inconnue"})
                return
            auth_provider = None
            attempts = []
            for port in config["auth_ports"][role]:
                code, _body, _ctype = request_local(port, "/validate")
                attempts.append({"port": port, "status": code})
                if code == 200:
                    auth_provider = port
                    break
            if auth_provider is None:
                self.reply(503, {"service": role, "error": "identite_indisponible", "attempts": attempts},
                           "Toutes les dépendances d'identité ont échoué")
                return
            if role == "portail":
                self.reply(200, {"service": role, "message": "Portail Asteria accessible",
                                 "auth_port": auth_provider}, "Identité disponible")
                return
            rows = orders(state)
            if path == "/export":
                self.reply(200, csv_text(rows), "Export commandes", "text/csv; charset=utf-8")
            else:
                self.reply(200, {"service": role, "auth_port": auth_provider, "count": len(rows),
                                 "quantity_total": sum(int(row["quantite"]) for row in rows), "orders": rows},
                           "Lecture des commandes")
        except (KeyError, ValueError, OSError, TypeError) as error:
            self.reply(503, {"service": role, "error": "configuration_ou_donnees", "detail": str(error)})


def serve(state):
    config = read_config(state)
    base = config["base_port"]
    servers = []
    started = []
    try:
        for offset, role in enumerate(["edge", "portail", "commandes", "idp", "idp_backup"]):
            server = ThreadingHTTPServer(("127.0.0.1", base + offset), Handler)
            server.daemon_threads = True
            server.role, server.state = role, state
            servers.append(server)
        for server in servers:
            threading.Thread(target=server.serve_forever, daemon=True).start()
            started.append(server)
        print(f"Laboratoire local : http://127.0.0.1:{base} ; Ctrl+C pour arrêter", flush=True)
        print(f"État : {state.resolve()} ; configuration relue à chaque requête", flush=True)
        while True:
            time.sleep(0.25)
    except KeyboardInterrupt:
        print("Arrêt du laboratoire.")
    finally:
        for server in started:
            server.shutdown()
        for server in servers:
            server.server_close()


def export_data(state, destination):
    config = read_config(state)
    code, body, _ctype = request_local(config["base_port"], "/commandes/export")
    if code != 200:
        raise ValueError(f"Export impossible : HTTP {code} {body}")
    rows = parse_orders(body)
    atomic(destination, body)
    metadata = {"exported_at_utc": now(), "sha256": hashlib.sha256(body.encode()).hexdigest(),
                "rows": len(rows), "quantity_total": sum(int(r["quantite"]) for r in rows)}
    atomic(destination.with_suffix(destination.suffix + ".meta.json"), json.dumps(metadata, indent=2) + "\n")
    event(state, "controle", "export", 200, str(destination))
    return metadata


def apply_incident(state, source):
    """Appliquer des données de TP, sans charger de code ou choisir une panne."""
    payload = json.loads(source.read_text(encoding="utf-8-sig"))
    if payload.get("format") != "asteria-incident-v1":
        raise ValueError("Format de capsule inconnu")
    if payload.get("module") not in {"M04", "M06", "M08"}:
        raise ValueError("Module de capsule invalide")
    config = validate_config(payload["config"])
    if config["base_port"] != read_config(state)["base_port"]:
        raise ValueError("La capsule ne correspond pas au port de base du laboratoire")
    text = payload["commandes_csv"]
    parse_orders(text)
    snapshot_text = payload.get("preincident_csv")
    snapshot_rows = parse_orders(snapshot_text) if snapshot_text is not None else None
    # Toutes les données sont vérifiées avant de remplacer l'état de travail.
    # Aucun chemin ni code arbitraire n'est lu depuis la capsule.
    if snapshot_text is not None:
        snapshot = state / "sauvegardes" / "preincident.csv"
        atomic(snapshot, snapshot_text)
        atomic(snapshot.with_suffix(".csv.meta.json"), json.dumps({
            "exported_at_utc": now(), "sha256": hashlib.sha256(snapshot_text.encode()).hexdigest(),
            "rows": len(snapshot_rows), "quantity_total": sum(int(r["quantite"]) for r in snapshot_rows),
            "provenance": "copie_fournie_dans_exercice"}, indent=2))
    atomic(state / "commandes.csv", text)
    save_config(state, config)
    event(state, "controle", "incident_applique", 200, f"module={payload['module']}; fichier={source.name}")
    print("État d'exercice appliqué ; conservez les preuves avant correction.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path, default=DEFAULT_STATE)
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init")
    init.add_argument("--base-port", type=int, default=18180)
    sub.add_parser("start")
    sub.add_parser("status")
    reset = sub.add_parser("reset")
    reset.add_argument("--confirm", action="store_true", required=True)
    injection = sub.add_parser("incident")
    injection.add_argument("--from", dest="source", type=Path, required=True)
    injection.add_argument("--confirm", action="store_true", required=True)
    export = sub.add_parser("export")
    export.add_argument("--to", type=Path, required=True)
    restore = sub.add_parser("restore")
    restore.add_argument("--from", dest="source", type=Path, required=True)
    restore.add_argument("--confirm", action="store_true", required=True)
    args = parser.parse_args()
    state = args.state_dir.resolve()
    try:
        if args.command == "init":
            if not 1024 <= args.base_port <= 65520:
                raise ValueError("Choisir un port de base entre 1024 et 65520")
            initialize(state, args.base_port)
        elif args.command == "start":
            serve(state)
        elif args.command == "reset":
            initialize(state, read_config(state)["base_port"], confirm=True)
        elif args.command == "status":
            config = read_config(state)
            results = {}
            for offset, role in enumerate(["edge", "portail", "commandes", "idp", "idp_backup"]):
                code, _body, _ctype = request_local(config["base_port"] + offset, "/health")
                results[role] = code
            for path in ("/portail", "/commandes"):
                code, body, _ctype = request_local(config["base_port"], path)
                results[path] = {"status": code, "body": body}
            print(json.dumps(results, ensure_ascii=False, indent=2))
            return 0 if all(results[path]["status"] == 200 for path in ("/portail", "/commandes")) else 2
        elif args.command == "incident":
            apply_incident(state, args.source)
        elif args.command == "export":
            print(json.dumps(export_data(state, args.to.resolve()), indent=2))
        elif args.command == "restore":
            text = args.source.read_bytes().decode("utf-8-sig")
            rows = parse_orders(text)
            if not rows:
                raise ValueError("Refus de restaurer un export vide")
            metadata_path = args.source.with_suffix(args.source.suffix + ".meta.json")
            if metadata_path.exists():
                metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
                if hashlib.sha256(text.encode()).hexdigest() != metadata["sha256"]:
                    raise ValueError("Empreinte incohérente avec le manifeste")
            atomic(state / "commandes.csv", csv_text(rows))
            event(state, "controle", "restore", 200, f"{args.source}; rows={len(rows)}")
            print(f"{len(rows)} commandes restaurées ; vérifier ensuite le parcours utilisateur.")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("ERREUR : " + str(error))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
