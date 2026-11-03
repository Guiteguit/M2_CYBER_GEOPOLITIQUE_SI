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
