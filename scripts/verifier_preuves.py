#!/usr/bin/env python3
"""Vérifier les empreintes d'un dossier sans en certifier l'origine."""
import argparse
import hashlib
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("manifest", type=Path)
args = parser.parse_args()
manifest = args.manifest.resolve()
root = manifest.parent
entries = json.loads(manifest.read_text(encoding="utf-8"))["files"]
failed = False
for name, expected in sorted(entries.items()):
    path = (root / name).resolve()
    if not path.is_relative_to(root):
        raise ValueError("Chemin hors du dossier de preuves")
    actual = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else "ABSENT"
    ok = actual == expected
    print("OK" if ok else "DIFFERENT", name)
    failed = failed or not ok
raise SystemExit(1 if failed else 0)
