#!/usr/bin/env python3
"""Vérification non destructive des prérequis locaux avant la séance."""
import argparse
import socket
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--base-port", type=int, default=18180)
args = parser.parse_args()
if sys.version_info < (3, 10):
    print("Python 3.10+ requis")
    raise SystemExit(1)
if not 1024 <= args.base_port <= 65520:
    parser.error("Port de base invalide")
failures = []
for offset in [0, 1, 2, 3, 4, 9]:
    port = args.base_port + offset
    with socket.socket() as probe:
        try:
            probe.bind(("127.0.0.1", port))
        except OSError:
            failures.append(port)
print("Python :", sys.version.split()[0])
print("Ports à libérer : " + str(failures) if failures else "Ports disponibles ; lancer le laboratoire.")
print("À lancer avant le serveur ; un port occupé par votre labo en cours est normal.")
raise SystemExit(1 if failures else 0)
