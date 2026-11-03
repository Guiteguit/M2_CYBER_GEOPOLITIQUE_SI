# Participer au cours et rendre son travail

## Avant la séance

Accepter l’invitation au dépôt, vérifier que l’on peut le cloner avec son propre compte, puis noter sa lettre A/B/C. Lire les [outils](OUTILS.md) et préparer le [laboratoire](../lab/README.md) avant M04. Les critères d’évaluation sont dans [EVALUATION.md](EVALUATION.md).

## Au début d’un module

Depuis son clone, à jour et sans modification non enregistrée :

```bash
git switch main
git pull --ff-only
git switch -c tp/m02-a
```

Adapter le module et la lettre. Si la branche existe, la reprendre avec `git switch` au lieu de la recréer. Ouvrir la mission et écrire son hypothèse dans `rendus/M02/individuel/A.md` avant les recherches.

## Pendant l’activité

Conserver des preuves datées dans `rendus/Mxx/preuves/` en distinguant mesures, jeux simulés et résultats prédits. Une preuve partagée peut être déposée une seule fois puis citée par chacun. Ne pas ajouter de secret ou de données d’entreprise.

Le laboratoire fonctionne sur sa propre machine : `127.0.0.1` ne désigne pas le poste d’un autre participant. L’état de travail `lab/runtime` reste hors de Git ; copier uniquement les preuves sélectionnées. Pour les exercices avec incident, appliquer une seule fois le fichier fourni au lancement de l’activité ; ne pas le réappliquer pour effacer une correction.

## Déposer sa contribution

```bash
git add rendus/M02/individuel/A.md
# Ajouter les fichiers de preuve effectivement créés.
git commit -m "M02 A : observations et hypothèses"
git push -u origin tp/m02-a
```

Ouvrir une pull request vers `main` et compléter le modèle : observation, preuve, interprétation, limite et décision SI. Corriger dans la même branche après les commentaires ; la pull request se met à jour après le prochain push. Voir le [guide Git](GIT.md).

## Synthèse collective et fin de séance

Après intégration des contributions, le rapporteur repart de `main` à jour et crée `tp/m02-synthese`. Le groupe complète `SYNTHESE.md`, ouvre la pull request collective et présente les arguments. Chacun explique au moins une preuve ou décision.

Si Git bloque, conserver les fichiers et poursuivre l’analyse ; leur dépôt peut être régularisé après la restitution. Avant de fermer le laboratoire, conserver les preuves et arrêter les serveurs par Ctrl+C. Un reset n’est pas une preuve de restauration.
