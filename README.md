# M2 Cyber — Géopolitique du cyberespace et stratégie SI

**8 modules de 90 minutes · 3 étudiants · Parcours technique complet.** Observer, manipuler, confronter les preuves et défendre une décision SI.

## Démarrer

- **Formateur et groupe :** [comment utiliser le dépôt en classe](docs/UTILISER_EN_CLASSE.md).
- **Étudiants :** [contexte Asteria](docs/CONTEXTE.md), [outils](docs/OUTILS.md), puis [M01](modules/M01/README.md).
- **Avant les manipulations locales :** [préparer le laboratoire](lab/README.md).
- **Avant M04 :** prendre connaissance du [barème proposé](docs/EVALUATION.md).

## Parcours disponible

| Module | Mission technique | Support principal | Rendu |
|---|---|---|---|
| [M01](modules/M01/README.md) | DNS, IP, ASN : dépendances visibles | Observation publique et collectes datées | [M01](rendus/M01/README.md) |
| [M02](modules/M02/README.md) | Routage observé et service disponible | Collecte RIPE réelle + traces simulées | [M02](rendus/M02/README.md) |
| [M03](modules/M03/README.md) | Comparer deux implantations | Manifestes JSON et contrats fictifs | [M03](rendus/M03/README.md) |
| [M04](modules/M04/README.md) | Tester une dépendance commune | Applications HTTP locales | [M04](rendus/M04/README.md) |
| [M05](modules/M05/README.md) | Prouver repli et restauration | Configuration, CSV et manifeste | [M05](rendus/M05/README.md) |
| [M06](modules/M06/README.md) | Investiguer et corriger une perturbation | Traces synthétiques et reproduction | [M06](rendus/M06/README.md) |
| [M07](modules/M07/README.md) | Vérifier une affirmation sur un incident | Empreintes, sources et traces | [M07](rendus/M07/README.md) |
| [M08](modules/M08/README.md) | Diagnostiquer, reprendre et défendre | Épreuve locale reproductible | [M08](rendus/M08/README.md) |

Chaque module M02–M08 comprend une mission, des notions, une aide et des supports de restitution individuels/collectifs. Le contenu est écrit pour un travail autonome suivi d’un échange ; les aides ne sont pas une correction complète.

## Environnement

M01–M03 et M07 s’appuient sur des observations ou des jeux de données. Le laboratoire M04–M06/M08 utilise Python 3.10+ et sa bibliothèque standard, sans VM, Docker ni `pip`. Ses cinq composants écoutent uniquement sur `127.0.0.1`. Les essais de cette version ont été exécutés sous Linux/Python 3.12 ; vérifier les postes de classe avant la séance.

Il s’agit d’un modèle d’applications et d’identité fictive, pas d’un déploiement SSO ou d’une architecture résiliente de production. Le labo fait de vrais échanges HTTP locaux ; BGP est étudié via les observations du M02, sans émission d’annonces.

## Méthode et évaluation

Douze heures effectives, hors pauses et préparation des postes. Conserver des hypothèses individuelles, des preuves datées et une synthèse argumentée. Chaque conclusion relie un acteur, une dépendance et une décision pour Asteria. Les pays et offres du cas sont fictifs ; les observations réelles sont explicitement séparées des traces simulées.

M01–M03 sont formatifs. Le [barème](docs/EVALUATION.md) propose 12 points individuels et 8 collectifs à valider par l’école. Les notes nominatives et corrections restent hors de ce dépôt partagé. Une branche « formateur » ne fournit pas de confidentialité.

## Travailler ensemble

Utiliser une branche par contribution puis une branche de synthèse. Le [guide Git](docs/GIT.md) présente le principe et le [guide de classe](docs/UTILISER_EN_CLASSE.md) détaille accès, rôles, pull requests, revues et intégration. Les comptes étudiants doivent être invités et les droits vérifiés avant le cours ; aucune invitation n’a été envoyée automatiquement.
