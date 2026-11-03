# M08 — Ressources autorisées

Les modules précédents, la documentation du laboratoire et vos propres notes sont autorisés. Appliquer une seule fois le fichier d’incident reçu au départ, placé dans `incidents/m08.json` :

```bash
python3 lab/asteria_lab.py incident --from incidents/m08.json --confirm
python3 lab/asteria_lab.py status
```

Utiliser le fichier attribué pour votre exercice. Si les ports de base diffèrent, les chemins sont ceux du [labo](../../lab/README.md). Le code de sortie de `status` porte sur les réponses HTTP, pas sur le contenu des commandes.

Le répertoire `lab/runtime/sauvegardes/` peut contenir une copie préincident ; vérifier sa provenance et sa validité avant de l’utiliser. L’import et une modification de configuration résolvent des classes de problèmes différentes. Conserver les preuves avant de choisir l’une de ces actions.

**Variante de secours sans exécution**, décidée par le formateur : analyser le dossier M06, fournir le diff proposé, la séquence de tests et les résultats attendus, puis défendre la stratégie. Identifier clairement les résultats comme prédictions ; le formateur adapte l’appréciation de la partie démonstration sans attribuer des tests non réalisés.
