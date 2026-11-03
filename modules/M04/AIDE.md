# M04 — Aides

Placer le fichier reçu pour cette activité dans `incidents/m04.json`. Dans un terminal serveur : suivre [le démarrage du laboratoire](../../lab/README.md). Depuis un deuxième terminal :

```bash
python3 lab/asteria_lab.py status
curl -i http://127.0.0.1:18180/portail
curl -i http://127.0.0.1:18180/commandes
python3 lab/asteria_lab.py incident --from incidents/m04.json --confirm
```

Sous Windows, utiliser `curl.exe` pour éviter une éventuelle confusion avec un alias PowerShell. Un navigateur affiche les réponses ; les outils réseau du navigateur ou `status` permettent d’obtenir les codes.

Ressources d’investigation : `lab/runtime/config.json`, `lab/runtime/events.jsonl`, les ports et chemins du [tableau des composants](../../lab/README.md). Les modifications de configuration sont relues sans redémarrage. La panne injectée renvoie une indisponibilité applicative ; elle ne tue pas le processus.

Après sauvegarde des preuves et seulement pour préparer la séance suivante :

```bash
python3 lab/asteria_lab.py reset --confirm
```


## Aides progressives — choisir le niveau utile

1. **Reformuler :** relire la mission et les notions ; écrire ce qui est observé, ce qui est supposé et le prochain résultat attendu.
2. **Comparer :** demander à un pair de proposer une autre explication. Choisir un test qui distingue les deux ; les chemins et commandes de ce fichier ou du [laboratoire](../../lab/README.md) servent à exécuter ce choix.
3. **Solliciter :** après trois à cinq minutes sans progrès, présenter au formateur l’objectif, le test tenté, le résultat exact et l’aide recherchée. Il peut aider plus tôt sur un blocage matériel ou un risque de perte des preuves.
4. **Reprendre la main :** après une question, un indice ou une démonstration, expliquer votre décision, effectuer votre vérification et consigner l’aide déterminante dans le rendu.

Ne pas empiler des modifications au hasard. Conserver l’état et les erreurs utiles. Si l’exécution est impossible, faire constater le blocage au formateur, proposer une séquence de tests et marquer les résultats non exécutés comme prédictions. Lire le [fonctionnement commun](../../docs/AUTONOMIE_ACCOMPAGNEE.md).
