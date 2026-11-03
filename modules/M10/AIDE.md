# M10 — Commandes et aides progressives

Depuis la racine du dépôt, avec Python 3.10+ standard ; sous Windows, `py -3` peut remplacer `python3`. Créer `lab/runtime/m10` et y copier source et mapping comme demandé dans la mission. Les noms de champs doivent correspondre exactement aux clés JSON de l’export.

## Transformer, importer, vérifier

```bash
python3 scripts/migrer_commandes.py transform --source lab/runtime/m10/source.json --mapping lab/runtime/m10/mapping.json --output lab/runtime/m10/commandes.csv
python3 scripts/migrer_commandes.py import --csv lab/runtime/m10/commandes.csv --db lab/runtime/m10/cible.sqlite
python3 scripts/migrer_commandes.py inspect --db lab/runtime/m10/cible.sqlite
python3 scripts/migrer_commandes.py verify --db lab/runtime/m10/cible.sqlite --reference modules/M10/donnees/reference_metier.csv
```

`verify` renvoie 0 si toutes les lignes concordent, 1 si les lignes diffèrent, 2 pour une erreur de lecture ou de validation. Les autres commandes renvoient 0 si l’opération réussit, 2 en cas d’erreur. Sous PowerShell, lire `$LASTEXITCODE` juste après la commande ; sous Bash, `echo $?`. Conserver la sortie et le code, sans supposer qu’une commande silencieuse démontre tout le métier.

## Aides graduées et erreurs

1. **Mapping :** pour chaque champ cible, chercher sa clé source, puis vérifier la règle de sélection de statut dans le contrat. `fields` mappe les trois champs cibles ; `status_field` désigne le champ à tester et `include_statuses` les valeurs admises. Éditer la copie, pas le modèle fourni.
2. **Erreur de clé / aucune commande :** contrôler orthographe, casse et statut. Une règle trop large peut importer les commandes annulées ; `verify` doit alors contredire votre résultat.
3. **Sortie déjà présente :** ne pas écraser la preuve ; produire `commandes_v2.csv` et utiliser une nouvelle base `cible_v2.sqlite` pour une tentative corrigée.
4. **Identifiant dupliqué :** lors du second import attendu, conserver le refus, puis relancer `verify`. Pour un CSV malformé, corriger la copie et expliquer la cause. Ne pas supprimer les contraintes de la cible.

Après le renommage de la seule copie `source.json`, rejouer les deux dernières commandes : elles n’utilisent pas le source. Les données de référence restent disponibles pour le contrôle ; leur disponibilité ne prouve pas l’indépendance de tous les services.

Après trois à cinq minutes sans progrès, demander une aide avec but, hypothèse, commande et erreur. Si Python/SQLite manque, solliciter immédiatement le formateur : poste collectif ou **secours d’analyse** du mapping et des tests. Une sortie attendue reste une prédiction si l’import n’a pas été exécuté.
