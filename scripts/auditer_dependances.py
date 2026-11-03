#!/usr/bin/env python3
"""Lecture d'un inventaire pédagogique, sans résolution de paquets ni réseau."""
import argparse
import json
from pathlib import Path

def audit(inventory, advisories):
    components = {c['id']: c for c in inventory['components']}
    for service, roots in inventory['services'].items():
        seen = set()
        def visit(cid):
            if cid in seen:
                return
            seen.add(cid)
            for dep in components[cid]['depends_on']:
                visit(dep)
        for root in roots:
            visit(root)
        selected = [components[c] for c in sorted(seen)]
        matches = [dict(advisory=a['id'], component=c['id'], version=c['version'], severity=a['severity'], condition=a['condition'])
                   for c in selected for a in advisories['advisories']
                   if a['component']==c['id'] and c['version'] in a['affected_versions']]
        yield dict(service=service, components=selected, matches=matches)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inventory', required=True, type=Path)
    p.add_argument('--advisories', required=True, type=Path)
    a = p.parse_args()
    try:
        reports = list(audit(json.loads(a.inventory.read_text(encoding='utf-8-sig')), json.loads(a.advisories.read_text(encoding='utf-8-sig'))))
    except (OSError, ValueError, KeyError, TypeError) as e:
        p.exit(2, f'Inventaire non exploitable : {e}\n')
    print(json.dumps({'simulation': True, 'services': reports}, ensure_ascii=False, indent=2))
    return 0  # réussite de lecture, pas certification de sécurité

if __name__ == '__main__':
    raise SystemExit(main())
