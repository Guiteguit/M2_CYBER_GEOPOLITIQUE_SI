# M07 — Aides

Depuis la racine :

```bash
python3 scripts/verifier_preuves.py modules/M06/donnees/SHA256SUMS.json
python3 scripts/verifier_preuves.py modules/M07/donnees/SHA256SUMS.json
```

Le script renvoie 0 si les fichiers du manifeste correspondent et 1 sinon. Le manifeste liste des chemins relatifs à son dossier ; aucun fichier extérieur à ce dossier n’est accepté. Il ne valide ni une origine cryptographique ni le caractère exhaustif des pièces.

Pour une ligne du journal, noter le service, l’instant, le statut et la portée. Pour une publication, noter la source citée, son indépendance et le saut logique éventuel. Si votre conclusion exige un journal d’administration absent, demander ce journal plutôt qu’en inventer le contenu.


## Aides progressives — choisir le niveau utile

1. **Reformuler :** relire la mission et les notions ; écrire ce qui est observé, ce qui est supposé et le prochain résultat attendu.
2. **Comparer :** demander à un pair de proposer une autre explication. Choisir un test qui distingue les deux ; les chemins et commandes de ce fichier ou du [laboratoire](../../lab/README.md) servent à exécuter ce choix.
3. **Solliciter :** après trois à cinq minutes sans progrès, présenter au formateur l’objectif, le test tenté, le résultat exact et l’aide recherchée. Il peut aider plus tôt sur un blocage matériel ou un risque de perte des preuves.
4. **Reprendre la main :** après une question, un indice ou une démonstration, expliquer votre décision, effectuer votre vérification et consigner l’aide déterminante dans le rendu.

Ne pas empiler des modifications au hasard. Conserver l’état et les erreurs utiles. Si l’exécution est impossible, faire constater le blocage au formateur, proposer une séquence de tests et marquer les résultats non exécutés comme prédictions. Lire le [fonctionnement commun](../../docs/AUTONOMIE_ACCOMPAGNEE.md).
