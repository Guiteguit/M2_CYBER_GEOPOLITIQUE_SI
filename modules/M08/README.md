# M08 — Diagnostiquer, reprendre et défendre une stratégie

**90 min · Épreuve finale technique et orale.** Prérequis : laboratoire préparé avant la séance, techniques M04–M07, Python 3.10+ et navigateur. [Barème commun](../../docs/EVALUATION.md). Aucun composant externe ni compte cloud requis.

## Mandat

Une perturbation affecte le laboratoire Asteria. Vous devez établir les symptômes, proposer une correction minimale, démontrer le fonctionnement métier et défendre une évolution du SI. Le diagnostic porte sur le laboratoire, pas sur une panne réelle d’un pays ou d’un fournisseur.

Le formateur choisit la graine de l’injection `scenario M08`. L’injecteur prépare un état initial et une copie préincident, puis une perturbation reproductible. Il ne s’agit pas d’un secret anti-triche : l’évaluation porte sur la méthode, les preuves et l’explication individuelle. Ne pas lire la sélection du scénario pour remplacer un diagnostic observé.

## Critères de reprise annoncés

- Les deux parcours `/portail` et `/commandes` répondent HTTP 200 via le point d’entrée.
- Les commandes C001, C002 et C003 sont présentes, sans doublon, avec les quantités 4, 3 et 2 : total neuf.
- La validation d’identité fictive reste utilisée ; pas de suppression de contrôle dans le code.
- Les journaux et preuves avant/après sont conservés.
- La correction vise le périmètre touché ; pas de reset ou de nouvelle injection pour faire disparaître la panne.

Le formateur indique avant le départ si les trois étudiants travaillent sur un labo collectif avec rôles tournants ou sur trois instances locales. La même exigence de preuves et d’explication individuelle s’applique. Les variantes doivent être comparées selon la méthode, pas au seul temps de réparation.

## Déroulé — 90 minutes

| Temps | Travail |
|---|---|
| 0–10 | Lecture, rôles et hypothèses individuelles ; aucune nouvelle notion |
| 10–20 | Constat initial, périmètre et sauvegarde des preuves |
| 20–45 | Tests discriminants, décision et correction minimale |
| 45–60 | Vérifications de reprise, contenu et non-régression |
| 60–70 | Synthèse et feuille de route courte |
| 70–85 | Présentation de six minutes puis neuf minutes de questions réparties |
| 85–90 | Retour individuel sur une hypothèse révisée |

## Travaux attendus

1. Établir une matrice de symptômes : chemin utilisateur, couche locale, données et journaux.
2. Énoncer deux hypothèses et un test qui les départage. En cas de première hypothèse correcte, expliquer pourquoi une autre est moins compatible avec vos observations.
3. Documenter l’action proposée et son risque, puis conserver un diff ou une preuve d’import/restauration si nécessaire. N’appliquer aucun changement hors du laboratoire.
4. Valider les critères de reprise. Une réponse HTTP 200 sans les données requises n’est pas une reprise métier.
5. Présenter une feuille de route de trois mesures à 30/60/90 jours : dépendance réduite, responsable, preuve de résultat et effort relatif (faible/moyen/fort). Aucun coût de marché inventé n’est nécessaire.
6. Relier au moins une mesure à une dépendance de contrôle ou de support international. Préciser ce qu’un autre fournisseur ou un autre pays changerait, et ce qu’il ne changerait pas.

## Livrables

[Rendu M08](../../rendus/M08/SYNTHESE.md) : journal de cinq décisions maximum, hypothèses/test, correction, preuves de reprise, limites et feuille de route. Chaque étudiant explique une décision ou vérification dont il a la responsabilité. Conserver les fichiers individuels A/B/C pour distinguer les contributions.

En cas d’impossibilité de lancer le serveur, prévenir immédiatement le formateur. La variante d’analyse de traces décrite dans [AIDE.md](AIDE.md) permet d’évaluer les raisonnements, mais doit être signalée comme telle : elle ne prouve pas une réparation exécutée.
