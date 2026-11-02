#!/usr/bin/env python3
"""Extraire des données d'offres fictives, sans prendre la décision."""
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("offre_a", type=Path)
parser.add_argument("offre_b", type=Path)
args = parser.parse_args()
offers = [json.loads(path.read_text(encoding="utf-8")) for path in (args.offre_a, args.offre_b)]
actors = []
for offer in offers:
    costs = offer["couts_eur"]
    actors.append({component["provider_id"] for component in offer["composants"]})
    print(offer["offre"], "mise en place + 18 mois =", costs["mise_en_place"] + 18 * costs["mensuel"],
          "EUR ; charge =", offer["charge_jours_equipe"], "jours")
print("Acteurs communs aux deux offres :", ", ".join(sorted(actors[0] & actors[1])) or "aucun dans le dossier")
print("Vérifier séparément les frais de sortie et la portée des déclarations contractuelles.")
