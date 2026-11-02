# Dossier M06 — entièrement synthétique

Ces traces ont été écrites pour l’exercice, pas collectées dans une entreprise. Les dates au 10 avril 2030, identifiants, comptes et IP de documentation sont fictifs. Les références techniques correspondent au modèle du laboratoire, pas à un incident public réel.

- `mesures.csv` : contrôles de disponibilité ponctuels ; pas une surveillance continue de tous les chemins.
- `changements.csv` : processus de changement et application d’une configuration ; l’origine complète de la préparation n’est pas documentée.
- `acces.csv` : tentatives échouées dans un périmètre limité ; aucun journal complet de toutes les authentifications n’est fourni.
- `config_avant.json` et `config_apres.json` : deux états de configuration à comparer.
- `SHA256SUMS.json` : empreintes des autres pièces de ce dossier, fournies avec elles ; intégrité comparative, pas signature indépendante.

Les journaux réels `lab/runtime/events.jsonl` produits lors de votre reproduction portent d’autres dates. Ne pas les présenter comme des traces historiques de 2030. Les configurations statiques utilisent le port de base 18180 ; l’injecteur adapte les ports si vous avez choisi une autre base.
