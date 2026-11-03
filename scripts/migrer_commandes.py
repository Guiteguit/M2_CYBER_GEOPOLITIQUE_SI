#!/usr/bin/env python3
"""Transformation et import local de données fictives M10. Aucun réseau."""
import argparse
import csv
import json
import sqlite3
from pathlib import Path

FIELDS = ['id', 'client', 'quantity']

def validate(rows):
    if not rows:
        raise ValueError('Aucune commande retenue')
    seen = set()
    out = []
    for row in rows:
        if not row['id'] or not row['client'] or row['id'] in seen:
            raise ValueError('Identifiant/client vide ou identifiant dupliqué')
        q = int(row['quantity'])
        if q <= 0:
            raise ValueError('Quantité non positive')
        seen.add(row['id'])
        out.append(dict(id=row['id'], client=row['client'], quantity=q))
    return sorted(out, key=lambda r: r['id'])

def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != FIELDS:
            raise ValueError('En-tête attendu : id,client,quantity')
        return validate(list(reader))

def run(a):
    if a.action == 'transform':
        if a.output.exists():
            raise ValueError('La sortie existe : choisir un nouveau nom pour préserver les preuves')
        source = json.loads(a.source.read_text(encoding='utf-8-sig'))
        mapping = json.loads(a.mapping.read_text(encoding='utf-8-sig'))
        rows = []
        for order in source['orders']:
            if order[mapping['status_field']] not in mapping['include_statuses']:
                continue
            rows.append({field: order[mapping['fields'][field]] for field in FIELDS})
        rows = validate(rows)
        a.output.parent.mkdir(parents=True, exist_ok=True)
        with a.output.open('w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader(); writer.writerows(rows)
        return dict(output=str(a.output), count=len(rows), quantity=sum(r['quantity'] for r in rows))
    if a.action == 'import':
        rows = read_csv(a.csv)  # valider avant toute écriture en base
        a.db.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(a.db) as db:
            db.execute('CREATE TABLE IF NOT EXISTS orders (id TEXT PRIMARY KEY, client TEXT NOT NULL, quantity INTEGER NOT NULL CHECK(quantity > 0))')
            # transaction : un doublon fait échouer tout cet import ; pas de suppression implicite
            with db:
                db.executemany('INSERT INTO orders VALUES (:id, :client, :quantity)', rows)
        return dict(imported=len(rows), db=str(a.db))
    if not a.db.is_file():
        raise ValueError('Base absente : aucun fichier créé par la lecture')
    with sqlite3.connect(a.db.resolve().as_uri()+'?mode=ro', uri=True) as db:
        db.row_factory=sqlite3.Row
        rows=validate([dict(r) for r in db.execute('SELECT id, client, quantity FROM orders')])
    result=dict(count=len(rows), quantity=sum(r['quantity'] for r in rows), orders=rows)
    if a.action == 'verify':
        expected=read_csv(a.reference)
        result['matches_reference']=(rows==expected)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if rows==expected else 1
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest='action', required=True)
    s=sub.add_parser('transform')
    for flag in ['source','mapping','output']:s.add_argument('--'+flag, required=True, type=Path)
    s=sub.add_parser('import')
    for flag in ['csv','db']:s.add_argument('--'+flag, required=True, type=Path)
    s=sub.add_parser('inspect');s.add_argument('--db', required=True, type=Path)
    s=sub.add_parser('verify')
    for flag in ['db','reference']:s.add_argument('--'+flag, required=True, type=Path)
    a=p.parse_args()
    try: result=run(a)
    except (OSError, ValueError, KeyError, TypeError, sqlite3.Error) as e:
        p.exit(2, f'Opération interrompue : {e}\n')
    if isinstance(result,int):return result
    print(json.dumps(result, ensure_ascii=False, indent=2));return 0

if __name__=='__main__':raise SystemExit(main())
