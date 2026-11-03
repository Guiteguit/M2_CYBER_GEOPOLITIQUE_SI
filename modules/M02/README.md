# M02 — Une route visible signifie-t-elle un service disponible ?

**90 minutes · Autonomie complète · Analyse BGP et mesures · Formatif.** Suivre le [guide commun](../../docs/DEMARRER_AUTONOMIE.md). Aucun cours oral, script ou site externe n’est nécessaire pour terminer. Les JSON et CSV sont lisibles directement dans GitHub ou avec une copie locale.

## Mission

Asteria cherche si une observation de routage suffit à expliquer une interruption de service. Distinguez route observée, accès depuis une sonde et disponibilité applicative. Votre analyse doit préciser le périmètre et proposer une surveillance utile.

Le module utilise une collecte RIPE réelle datée et deux CSV simulés : [présentation des données](donnees/README.md). Ne leur attribuez pas le même incident ou la même période. Vous pouvez terminer M02 même si le diagnostic M01 reste incertain : toutes les ressources sont fournies ici.

B est rapporteur. A commence par les sondes HTTP, B par le JSON RIPE, C par le CSV de routes ; chacun relit au moins une autre source.

## Chronomètre — 90 minutes

| Minutes | Travail autonome |
|---|---|
| 0–5 | Hypothèse individuelle et attribution des tâches |
| 5–20 | Lecture de [NOTIONS.md](NOTIONS.md) et reformulation croisée |
| 20–38 | Qualifier la collecte réelle : ressource, dates, origine et premier saut |
| 38–58 | Comparer les deux CSV simulés et construire quatre jalons |
| 58–70 | Présentations croisées et mise à l’épreuve des hypothèses |
| 70–83 | Rédiger la synthèse et trois indicateurs |
| 83–90 | [Auto-vérification](AUTO_VERIFICATION.md), trace individuelle et enregistrement |

## 1. Hypothèse et lecture

Avant les notions, chacun écrit : « Une route disparaît chez un observateur : puis-je affirmer que tous les utilisateurs ont perdu le service ? Quelle information manque ? » Ne corrigez pas votre réponse avant de l’avoir conservée.

Lire les notions puis expliquer à un autre la différence entre ASN d’origine, chemin observé et trajet physique. Utilisez les [aides progressives](AIDE.md) si une colonne ou un champ bloque.

## 2. Collecte réelle

Ouvrir [ripe_routing_history_reel.json](donnees/ripe_routing_history_reel.json). Retrouver :

- la date à laquelle le fichier a été collecté ;
- la ressource et les paramètres demandés dans `source_url` ;
- la période effectivement couverte dans `response.data` ;
- un groupe de `by_origin`, son origine/premier saut et une de ses périodes de visibilité.

Avec l’option de premier saut, une valeur `origin` peut contenir deux ASN ; les notions expliquent comment lire ce format. N’assimilez pas le nombre de groupes au nombre d’origines distinctes sans examiner ces valeurs. La collecte réelle ne fournit pas à elle seule un incident à diagnostiquer.

La consultation de RIPEstat en ligne et le formatage avec Python sont facultatifs. Si un site ou un outil bloque plus de trois minutes, restez sur le fichier fourni.

## 3. Exercice simulé

Ouvrir [routes_simulees.csv](donnees/routes_simulees.csv) et [sondes_simulees.csv](donnees/sondes_simulees.csv), dans le navigateur ou un tableur. Les dates, préfixes et ASN de cet exercice sont fictifs ; aucune requête vers ces adresses n’est demandée.

Pour chacun des quatre instants : comparer R1 et R2, calculer `peers_seeing / peers_total`, noter les chemins observés puis relever les résultats des sondes A et B. La fraction obtenue décrit les pairs du collecteur, pas les utilisateurs affectés.

Votre chronologie doit comporter quatre lignes : instant, route selon R1/R2, service selon A/B, conclusion limitée. Cherchez un exemple de différence entre observateurs et un exemple de différence entre routage et application. Le script de l’[aide](AIDE.md) est seulement une calculatrice facultative.

## 4. Discussion à trois

Deux minutes chacun pour présenter une observation et une limite, puis six minutes pour confronter au moins deux explications possibles. Pour chacune, demander une preuve qui pourrait la confirmer ou la rendre moins plausible.

Un opérateur pourrait-il contrôler plusieurs accès apparemment différents ? De quelles données disposer pour décider d’une deuxième liaison ? Une variation de chemin suffit-elle à affirmer une censure ou une opération étatique ? Conservez les conditions et les inconnues dans le rendu.

## 5. Livrables et suite

Compléter [la synthèse M02](../../rendus/M02/SYNTHESE.md) : trois observations sourcées, chronologie de quatre jalons, deux hypothèses et trois indicateurs comportant source, responsable, fréquence, déclencheur et action.

B dépose la synthèse sur `tp/autonomie-b`. Chacun complète son fichier individuel sur sa propre branche, déjà utilisée au M01. Ne fusionnez pas et n’attendez pas d’approbation. En mode local, conserver les fichiers pour remise ultérieure.

Effectuer l’[auto-vérification](AUTO_VERIFICATION.md), consigner les blocages et ouvrir [M03](../M03/README.md), même si une hypothèse reste ouverte. Le formateur discutera vos raisonnements à partir de M04.
