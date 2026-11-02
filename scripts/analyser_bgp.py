#!/usr/bin/env python3
"""Afficher des fractions d'observation, sans diagnostiquer leur cause."""
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("csv_file")
args = parser.parse_args()
with open(args.csv_file, encoding="utf-8-sig", newline="") as handle:
    for row in csv.DictReader(handle):
        seen, total = int(row["peers_seeing"]), int(row["peers_total"])
        if total <= 0 or not 0 <= seen <= total:
            raise ValueError("Population de pairs incohérente")
        print(row["timestamp_utc"], row["collector"], row["prefix"],
              f"{seen}/{total} = {seen / total:.0%}", "AS_PATH=" + (row["as_path"] or "non observe"))
