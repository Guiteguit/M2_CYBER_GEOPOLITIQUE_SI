# M05 — Aides

Voir les champs `auth_ports` et `disabled` dans [la configuration du laboratoire](../../lab/README.md). Les ports de validation sont calculés depuis le port de base. Garder la validation fictive ; ne pas modifier le code pour la supprimer.

```bash
python3 lab/asteria_lab.py export --to lab/runtime/sauvegardes/m05.csv
python3 lab/asteria_lab.py restore --from lab/runtime/sauvegardes/m05.csv --confirm
python3 lab/asteria_lab.py status
```

Copie locale sans dépendance au shell :

```bash
python3 -c "from pathlib import Path; import shutil; shutil.copy2('lab/runtime/config.json','lab/runtime/config-avant-m05.json')"
```

L’en-tête attendu est `commande,client,quantite,statut`. Avant de vider le CSV du laboratoire dans un éditeur, vérifier que l’export et son manifeste existent et sont lisibles. La commande `restore` vérifie le format et le manifeste adjacent s’il existe ; elle refuse une sauvegarde vide. Elle ne valide pas votre choix de date de sauvegarde.

Pour les preuves, utiliser une copie de l’export sous `rendus/M05/preuves/` ; le répertoire `runtime` est exclu de Git pour éviter d’envoyer tout l’état de travail.
