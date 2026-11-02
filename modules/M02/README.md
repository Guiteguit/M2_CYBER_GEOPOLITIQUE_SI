# M02 — Une route visible signifie-t-elle un service disponible ?

**90 min · Recherche BGP et analyse de traces · Formatif.** Prérequis : vocabulaire IP/préfixe/ASN du M01. Matériel : navigateur et Python 3.10+ ou tableur ; aucun routeur ni VM à installer.

## Mission

Asteria souhaite savoir si un changement de routage observé suffit à expliquer une interruption de service. Vous devez séparer visibilité des routes, accès mesuré et fonctionnement applicatif, puis proposer une surveillance pertinente.

Commencer par les [notions](NOTIONS.md), les [données](donnees/README.md) et l’[aide](AIDE.md). Deux jeux sont séparés : une collecte réelle RIPEstat et un exercice CSV **entièrement simulé**. Ne pas mélanger leurs dates, préfixes ou conclusions.

## Déroulé — 90 minutes

| Temps | Activité |
|---|---|
| 0–10 | Chacun écrit : « Si une route disparaît d’un observateur, que puis-je conclure ? » |
| 10–25 | Apports : origine, AS_PATH, observateurs, visibilité et mesure du service |
| 25–45 | Examiner le JSON RIPE et relever ressource, période, origines et périmètre d’observation |
| 45–65 | Analyser les CSV simulés et construire une chronologie croisant les couches |
| 65–80 | Confronter les diagnostics et leurs contre-exemples |
| 80–90 | Rédiger une décision de supervision et une limite de preuve |

## Investigation

1. Dans la collecte réelle, retrouver les paramètres et la période effectivement couverte. Identifier un ASN d’origine et, si disponible, un premier saut. Distinguer date de collecte et dates des observations.
2. Dans `routes_simulees.csv`, comparer les deux collecteurs à chaque instant : nombre de pairs voyant le préfixe, population totale et chemin rapporté. Calculer les fractions sans les transformer en pourcentage d’utilisateurs affectés.
3. Croiser avec `sondes_simulees.csv`. Identifier un moment où un changement de visibilité ne produit pas les mêmes effets depuis toutes les sondes et un moment où le routage semble revenu mais où l’application reste indisponible.
4. Proposer au moins deux explications compatibles avec les observations. Pour les départager, demander une preuve précise : données opérateur, journaux de changement, autres observateurs ou mesure applicative.

Les CSV peuvent être ouverts dans un tableur. Le script `scripts/analyser_bgp.py` donne les fractions par ligne, sans expliquer la cause. Le résultat brut n’est pas votre diagnostic.

## Questions de débat

- Est-ce une anomalie locale, une interruption partielle, une panne applicative ou une opération intentionnelle ? Que pouvez-vous réellement établir ?
- Quels opérateurs et dépendances d’interconnexion Asteria devrait-elle examiner avant de choisir une deuxième liaison ?
- Deux opérateurs pourraient-ils dépendre d’un même transit ou passage physique ? Quelles preuves manquent ?
- Une variation d’AS_PATH prouve-t-elle un passage physique par tous les pays supposés associés aux ASN ?

## Livrables et retour

Compléter [le rendu](../../rendus/M02/SYNTHESE.md) : chronologie de quatre jalons, trois observations sourcées, deux hypothèses concurrentes et trois indicateurs (source, fréquence, responsable, déclencheur, action). Chacun conserve une courte position individuelle et explique une limite pendant l’oral.

Le retour porte sur la précision des périodes, la séparation des couches et la prudence de l’attribution. M02 est formatif. En cas de problème Internet, les fichiers locaux suffisent ; aucune requête vers les préfixes simulés n’est attendue.
