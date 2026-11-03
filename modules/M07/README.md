# M07 — Vérifier une affirmation publique sur un incident

> **Autonomie accompagnée :** vous conduisez ce module à partir des supports. Le formateur est présent en soutien, pour une aide ciblée et pour challenger vos décisions ; aucun exposé oral n’est nécessaire pour commencer. Lire [le fonctionnement commun](../../docs/AUTONOMIE_ACCOMPAGNEE.md). Les apports sont dans [NOTIONS.md](NOTIONS.md), les aides dans [AIDE.md](AIDE.md), puis utiliser [AUTO_VERIFICATION.md](AUTO_VERIFICATION.md).

**90 min · Analyse de preuves, intégrité et recherche de source · Évaluation collective.** Prérequis : dossier M06 ; Python 3.10+ ou outil de calcul d’empreinte. Le parcours de base fonctionne sans Internet.

## Mission

Une publication affirme que l’incident Asteria prouve une opération étatique. Votre équipe doit produire une analyse vérifiable et une communication proportionnée. Vous travaillez sur les pièces fictives de M06 et sur quatre nouvelles publications **également fictives**, sans reprendre leurs affirmations comme des faits.

## Déroulé

| Minutes | Travail conduit par les étudiants |
|---|---|
| 0–8 | Formuler les preuves nécessaires à une attribution |
| 8–20 | Lire les notions et distinguer les niveaux de preuve |
| 20–40 | Vérifier les manifestes et tracer les citations |
| 40–60 | Confronter les cinq affirmations aux pièces |
| 60–78 | Discussion contradictoire et message de situation |
| 78–90 | Auto-vérifier et enregistrer la synthèse |

## Travail technique et documentaire

1. Calculer les empreintes des fichiers du dossier M06 et des pièces M07 avec le script fourni. Expliquer ce que confirme un manifeste fourni dans le même dépôt et ce qu’il ne prouve pas sur l’auteur ou l’exhaustivité.
2. Construire le graphe de citations entre `publication_1.md`, `reprise_2.md`, `reprise_3.md` et `note_operateur.md`. Compter les origines réellement indépendantes pour chaque affirmation, pas le nombre de liens.
3. Pour chaque ligne d’`affirmations.csv`, rechercher une pièce technique qui soutient, contredit ou laisse ouverte l’affirmation. Citer la date et le périmètre. Il est possible que plusieurs aspects d’une même phrase aient des statuts différents.
4. Formuler deux hypothèses concurrentes sur l’incident et une demande de preuve permettant de progresser. Séparer mécanisme technique et attribution de l’auteur.
5. Produire un message de six lignes maximum à la direction : impacts confirmés, action de reprise, inconnues et prochaine vérification. Ne pas promettre une attribution future certaine.

Le manifeste ne doit pas être modifié pour masquer une différence. Si un fichier a changé, analyser la divergence par rapport à la version du dépôt et l’indiquer. Le script ne vérifie pas de signature d’éditeur.

## Comparaison réelle facultative — dans le temps de discussion

Lire le [retour d’expérience officiel de Meta sur la panne du 4 octobre 2021](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/). Comparer les types de preuves et les difficultés de reprise à votre dossier. Ne pas attribuer à Asteria les événements d’un autre incident. Un bref [repère hors ligne](donnees/REPERES_REELS.md) est fourni.

## Sens géopolitique

Comment une accusation peut-elle influencer les choix de fournisseurs ou la communication d’une entreprise ? Quel acteur bénéficierait d’une décision précipitée ? Une hypothèse sur un intérêt n’est pas la preuve d’une campagne coordonnée. Les pays et comptes du dossier sont fictifs.

## Livrables

[Rendu M07](../../rendus/M07/SYNTHESE.md) : résultat d’intégrité, graphe des sources, matrice des cinq affirmations, deux hypothèses et message final. Chacun défend une affirmation et une limite. Le retour juge la qualité de la preuve, pas l’adhésion à un récit politique.

## Points de décision à consigner

- Que vérifie l’empreinte et quelle confiance accordez-vous à sa référence ?
- Combien d’origines indépendantes soutiennent réellement une affirmation ?
- Quelle formulation permet d’informer la direction sans dépasser les preuves ?

Ces traces ne sont pas des demandes d’autorisation. Après une aide ou une objection, expliquez vous-mêmes la décision retenue et testez-la. À la fin, le rapporteur consigne la synthèse sur sa branche personnelle du module, sans attendre une fusion ; chacun garde son fichier individuel.
