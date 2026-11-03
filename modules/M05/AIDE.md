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


## Aides progressives — choisir le niveau utile

1. **Reformuler :** relire la mission et les notions ; écrire ce qui est observé, ce qui est supposé et le prochain résultat attendu.
2. **Comparer :** demander à un pair de proposer une autre explication. Choisir un test qui distingue les deux ; les chemins et commandes de ce fichier ou du [laboratoire](../../lab/README.md) servent à exécuter ce choix.
3. **Solliciter :** après trois à cinq minutes sans progrès, présenter au formateur l’objectif, le test tenté, le résultat exact et l’aide recherchée. Il peut aider plus tôt sur un blocage matériel ou un risque de perte des preuves.
4. **Reprendre la main :** après une question, un indice ou une démonstration, expliquer votre décision, effectuer votre vérification et consigner l’aide déterminante dans le rendu.

Ne pas empiler des modifications au hasard. Conserver l’état et les erreurs utiles. Si l’exécution est impossible, faire constater le blocage au formateur, proposer une séquence de tests et marquer les résultats non exécutés comme prédictions. Lire le [fonctionnement commun](../../docs/AUTONOMIE_ACCOMPAGNEE.md).
