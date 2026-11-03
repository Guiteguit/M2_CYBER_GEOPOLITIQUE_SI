# M02 — Aides facultatives

**Mode autonome de base :** ouvrez le JSON et les deux CSV dans GitHub ou un éditeur. Aucun script ni accès à RIPEstat n’est obligatoire. Après trois minutes de blocage d’un outil, poursuivre dans ces fichiers.

## Aides progressives

1. **Je confonds les dates.** `collected_at_utc` décrit le téléchargement. `source_url` porte la demande. Les champs `query_starttime` et `query_endtime` dans les données décrivent la période effective. Relevez-les séparément avant de comparer.
2. **Le CSV me paraît trop dense.** Prenez un seul instant. Copiez les lignes R1 et R2, puis A et B à ce même instant. Calculez une fraction et écrivez une phrase par couche. Répétez pour les autres instants. Si un tableur met tout dans une colonne, choisir la virgule comme séparateur ou lire le texte brut.
3. **Je ne peux pas prouver la cause.** C’est possible avec ce dossier. Donnez deux mécanismes compatibles, les faits utiles et une preuve supplémentaire qui les départagerait. La mission ne demande pas de deviner une cause certaine.

Les [notions](NOTIONS.md) expliquent le format de premier saut et la différence entre fraction de pairs et utilisateurs. Le résultat d’un calcul seul n’est pas une interprétation.

## Outils facultatifs déjà disponibles

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
