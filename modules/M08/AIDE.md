# M08 — Ressources autorisées

Les modules précédents, la documentation du laboratoire et vos propres notes sont autorisés. Un seul injecteur est lancé au départ, avec la graine donnée par le formateur :

```bash
python3 lab/asteria_lab.py scenario M08 --seed 27
python3 lab/asteria_lab.py status
```

Utiliser la graine attribuée, pas nécessairement 27. Si les ports de base diffèrent, les chemins sont ceux du [labo](../../lab/README.md). Le code de sortie de `status` porte sur les réponses HTTP, pas sur le contenu des commandes.

Le répertoire `lab/runtime/sauvegardes/` peut contenir une copie préincident ; vérifier sa provenance et sa validité avant de l’utiliser. L’import et une modification de configuration résolvent des classes de problèmes différentes. Conserver les preuves avant de choisir l’une de ces actions.

**Variante de secours sans exécution**, décidée par le formateur : analyser le dossier M06, fournir le diff proposé, la séquence de tests et les résultats attendus, puis défendre la stratégie. Identifier clairement les résultats comme prédictions ; le formateur adapte l’appréciation de la partie démonstration sans attribuer des tests non réalisés.
