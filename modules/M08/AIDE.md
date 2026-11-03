# M08 — Ressources autorisées

Les modules précédents, la documentation du laboratoire et vos propres notes sont autorisés. Appliquer une seule fois le fichier d’incident reçu au départ, placé dans `incidents/m08.json` :

```bash
python3 lab/asteria_lab.py incident --from incidents/m08.json --confirm
python3 lab/asteria_lab.py status
```

Utiliser le fichier attribué pour votre exercice. Si les ports de base diffèrent, les chemins sont ceux du [labo](../../lab/README.md). Le code de sortie de `status` porte sur les réponses HTTP, pas sur le contenu des commandes.

Le répertoire `lab/runtime/sauvegardes/` peut contenir une copie préincident ; vérifier sa provenance et sa validité avant de l’utiliser. L’import et une modification de configuration résolvent des classes de problèmes différentes. Conserver les preuves avant de choisir l’une de ces actions.

**Variante de secours sans exécution**, décidée par le formateur : analyser le dossier M06, fournir le diff proposé, la séquence de tests et les résultats attendus, puis défendre la stratégie. Identifier clairement les résultats comme prédictions ; le formateur adapte l’appréciation de la partie démonstration sans attribuer des tests non réalisés.


## Aides progressives — choisir le niveau utile

1. **Reformuler :** relire la mission et les notions ; écrire ce qui est observé, ce qui est supposé et le prochain résultat attendu.
2. **Comparer :** demander à un pair de proposer une autre explication. Choisir un test qui distingue les deux ; les chemins et commandes de ce fichier ou du [laboratoire](../../lab/README.md) servent à exécuter ce choix.
3. **Solliciter :** après trois à cinq minutes sans progrès, présenter au formateur l’objectif, le test tenté, le résultat exact et l’aide recherchée. Il peut aider plus tôt sur un blocage matériel ou un risque de perte des preuves.
4. **Reprendre la main :** après une question, un indice ou une démonstration, expliquer votre décision, effectuer votre vérification et consigner l’aide déterminante dans le rendu.

Ne pas empiler des modifications au hasard. Conserver l’état et les erreurs utiles. Si l’exécution est impossible, faire constater le blocage au formateur, proposer une séquence de tests et marquer les résultats non exécutés comme prédictions. Lire le [fonctionnement commun](../../docs/AUTONOMIE_ACCOMPAGNEE.md).
