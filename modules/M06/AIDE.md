# M06 — Aides

```bash
python3 lab/asteria_lab.py incident --from incidents/m06.json --confirm
python3 lab/asteria_lab.py status
python3 -m json.tool lab/runtime/config.json
```

Comparer des JSON dans VS Code (« Select for Compare », puis « Compare with Selected ») ou avec un outil de diff. Relever les valeurs qui changent, pas seulement les lignes ajoutées.

Les ports et endpoints se trouvent dans [le laboratoire](../../lab/README.md). Utiliser un accès direct permet de tester une couche en dehors d’un chemin complet ; ce n’est pas une preuve que tout le service fonctionne.

Placer le fichier fourni dans `incidents/m06.json`. La commande `incident` applique les données et la configuration de cette capsule. Lancer l’injection une seule fois avant d’investiguer ; la relancer après une correction écraserait celle-ci. Copier ses preuves et son diff sous `rendus/M06/preuves` avant de terminer.


## Aides progressives — choisir le niveau utile

1. **Reformuler :** relire la mission et les notions ; écrire ce qui est observé, ce qui est supposé et le prochain résultat attendu.
2. **Comparer :** demander à un pair de proposer une autre explication. Choisir un test qui distingue les deux ; les chemins et commandes de ce fichier ou du [laboratoire](../../lab/README.md) servent à exécuter ce choix.
3. **Solliciter :** après trois à cinq minutes sans progrès, présenter au formateur l’objectif, le test tenté, le résultat exact et l’aide recherchée. Il peut aider plus tôt sur un blocage matériel ou un risque de perte des preuves.
4. **Reprendre la main :** après une question, un indice ou une démonstration, expliquer votre décision, effectuer votre vérification et consigner l’aide déterminante dans le rendu.

Ne pas empiler des modifications au hasard. Conserver l’état et les erreurs utiles. Si l’exécution est impossible, faire constater le blocage au formateur, proposer une séquence de tests et marquer les résultats non exécutés comme prédictions. Lire le [fonctionnement commun](../../docs/AUTONOMIE_ACCOMPAGNEE.md).
