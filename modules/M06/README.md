# M06 — Panne, changement ou action malveillante ?

**90 min · Investigation de traces et reproduction HTTP · Évaluation individuelle.** Prérequis : M04–M05, laboratoire opérationnel et Python 3.10+ ; accès Internet non nécessaire.

## Mission

Deux applications Asteria deviennent indisponibles pendant une période de tension internationale. Un compte externe a également échoué à se connecter. La direction demande un diagnostic et une reprise proportionnée. Vous ne devez ni attribuer l’incident par intuition ni effacer les traces pour obtenir une page verte.

Le [dossier de traces](donnees/README.md) est **synthétique**, avec des dates fictives. Il contient événements d’exploitation, mesures, journal d’accès et deux configurations. Les journaux réels produits par votre reproduction auront les dates de votre machine : gardez les deux chronologies distinctes.

## Déroulé

| Temps | Travail |
|---|---|
| 0–10 | Chaque étudiant propose une hypothèse et un test qui pourrait l’infirmer |
| 10–25 | [Notions](NOTIONS.md) : corrélation, causalité, périmètre et préservation |
| 25–45 | Croiser les traces et comparer les configurations |
| 45–65 | Reproduire le scénario M06 et tester une correction minimale |
| 65–80 | Confronter les hypothèses et vérifier la reprise des deux applications |
| 80–90 | Consigner la décision et les limites d’attribution |

## Investigation et reprise

1. Construire une chronologie de cinq jalons en citant les fichiers et champs. Qualifier les sources et leurs limites.
2. Comparer `config_avant.json` et `config_apres.json`. Expliquer un mécanisme qui produit les symptômes et chercher un contre-exemple possible.
3. Examiner les échecs de connexion externes : démontrent-ils un accès réussi, un changement de configuration ou seulement des tentatives ? Quelle autre preuve serait nécessaire ?
4. Conserver l’état initial du laboratoire, puis appliquer le fichier d’incident fourni pour M06. Réaliser au moins un test de bout en bout et un test direct d’une dépendance. Conserver les réponses avant d’éditer la configuration.
5. Proposer une correction minimale de configuration, annoncer l’effet attendu et l’appliquer. Vérifier les deux applications et le contenu métier. Ne pas remplacer le laboratoire par un reset.
6. Vérifier la non-régression : le contrôle d’identité existe toujours et les journaux sont conservés. Ne pas modifier le code du laboratoire pour ignorer une erreur.

La modification en classe prouve qu’une correction résout les symptômes de votre modèle. Le dossier documentaire sert à examiner la cause et les limites de l’attribution de l’incident fictif, sans assimiler automatiquement reproduction et preuve historique.

## Échange avec la direction

Que peut-on dire publiquement à cet instant ? Faut-il maintenir le fournisseur, suspendre des accès, contrôler un changement ou attendre d’autres éléments ? Quelle dépendance de support international complique éventuellement la reprise ? Distinguer ce qui est établi dans les traces et les scénarios ajoutés.

## Livrables

[Rendu M06](../../rendus/M06/SYNTHESE.md) : chronologie, deux hypothèses comparées, diff de correction, preuves avant/après et message de situation de six lignes. Chaque étudiant défend une hypothèse, un test et ce qu’il a révisé. Voir le [barème](../../docs/EVALUATION.md).
