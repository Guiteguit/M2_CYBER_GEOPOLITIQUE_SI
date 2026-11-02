# Données M02

Deux natures de preuves restent séparées.

- `ripe_routing_history_reel.json` : réponse réellement collectée de RIPEstat pour le préfixe choisi au M01. L’enveloppe conserve URL, date de collecte et nature. Les périodes et filtres de la réponse décrivent sa portée ; la collecte ne constitue pas un incident observé.
- `routes_simulees.csv` et `sondes_simulees.csv` : jeu entièrement inventé, horodaté au 10 avril 2030 pour marquer son caractère fictif. Le préfixe de documentation et les ASN de laboratoire ne décrivent aucun réseau réel. Les colonnes sont une normalisation pédagogique, pas le format brut d’un message BGP.

Les deux collecteurs fictifs voient dix pairs chacun. `peers_seeing` compte les pairs voyant le préfixe et `peers_total` la population examinée. Les chemins sont des observations synthétiques. Les sondes HTTP sont distinctes des collecteurs BGP : ne pas les assimiler à la même machine ou au même lieu. Le dossier ne donne pas la cause de l’incident simulé ni les pays des réseaux.

Conserver les fichiers d’origine ; faire ses tableaux dans les rendus. L’analyse hors ligne utilise les mêmes missions et doit préciser les limites des points d’observation.
