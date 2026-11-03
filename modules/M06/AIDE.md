# M06 — Aides

```bash
python3 lab/asteria_lab.py incident --from incidents/m06.json --confirm
python3 lab/asteria_lab.py status
python3 -m json.tool lab/runtime/config.json
```

Comparer des JSON dans VS Code (« Select for Compare », puis « Compare with Selected ») ou avec un outil de diff. Relever les valeurs qui changent, pas seulement les lignes ajoutées.

Les ports et endpoints se trouvent dans [le laboratoire](../../lab/README.md). Utiliser un accès direct permet de tester une couche en dehors d’un chemin complet ; ce n’est pas une preuve que tout le service fonctionne.

Placer le fichier fourni dans `incidents/m06.json`. La commande `incident` applique les données et la configuration de cette capsule. Lancer l’injection une seule fois avant d’investiguer ; la relancer après une correction écraserait celle-ci. Copier ses preuves et son diff sous `rendus/M06/preuves` avant de terminer.
