# M02 — Aides facultatives

Depuis la racine du dépôt :

```bash
python3 scripts/analyser_bgp.py modules/M02/donnees/routes_simulees.csv
python3 -m json.tool modules/M02/donnees/ripe_routing_history_reel.json
```

En ligne, [RIPEstat](https://stat.ripe.net/) permet de rechercher le préfixe de l’adresse étudiée au M01. L’[API Routing History](https://stat.ripe.net/docs/data-api/api-endpoints/routing-history) accepte une IP, un préfixe ou un ASN. Noter la période et les filtres ; ne pas interpréter les informations filtrées comme un recensement exhaustif.

Exemple de requête publique, à dater si vous l’utilisez :

```bash
curl 'https://stat.ripe.net/data/routing-history/data.json?resource=151.101.0.0%2F22&max_rows=30'
```

Le script ne détecte pas une attaque et ne vérifie pas la validité RPKI. Pour comparer deux instants, aligner collecteur, préfixe et population de pairs. Utiliser un tableur est tout aussi recevable.
