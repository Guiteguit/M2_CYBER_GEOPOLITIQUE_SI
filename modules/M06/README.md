# M06 — Panne, changement ou action malveillante ?

> **Autonomie accompagnée :** vous conduisez ce module à partir des supports. Le formateur est présent en soutien, pour une aide ciblée et pour challenger vos décisions ; aucun exposé oral n’est nécessaire pour commencer. Lire [le fonctionnement commun](../../docs/AUTONOMIE_ACCOMPAGNEE.md). Les apports sont dans [NOTIONS.md](NOTIONS.md), les aides dans [AIDE.md](AIDE.md), puis utiliser [AUTO_VERIFICATION.md](AUTO_VERIFICATION.md).

**90 min · Investigation de traces et reproduction HTTP · Évaluation individuelle.** Prérequis : M04–M05, laboratoire opérationnel et Python 3.10+ ; accès Internet non nécessaire.

## Mission

Deux applications Asteria deviennent indisponibles pendant une période de tension internationale. Un compte externe a également échoué à se connecter. La direction demande un diagnostic et une reprise proportionnée. Vous ne devez ni attribuer l’incident par intuition ni effacer les traces pour obtenir une page verte.

Le [dossier de traces](donnees/README.md) est **synthétique**, avec des dates fictives. Il contient événements d’exploitation, mesures, journal d’accès et deux configurations. Les journaux réels produits par votre reproduction auront les dates de votre machine : gardez les deux chronologies distinctes.

## Déroulé

| Minutes | Travail conduit par les étudiants |
|---|---|
| 0–8 | Hypothèse individuelle et test susceptible de l’infirmer |
| 8–20 | Lire les notions et préciser les sources/périmètres |
| 20–42 | Croiser les traces et comparer les configurations |
| 42–65 | Reproduire, choisir une correction et vérifier |
| 65–78 | Défendre le raisonnement et les limites d’attribution |
| 78–90 | Auto-vérifier, rédiger la situation et enregistrer |

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

## Points de décision à consigner

- Quel test distingue vos deux premières hypothèses ?
- Quel changement minimal proposez-vous, avec quelle prédiction et quel moyen de vérifier la non-régression ?
- Qu’avez-vous établi sur le mécanisme, et que manque-t-il encore pour parler d’un auteur ?

Ces traces ne sont pas des demandes d’autorisation. Après une aide ou une objection, expliquez vous-mêmes la décision retenue et testez-la. À la fin, le rapporteur consigne la synthèse sur sa branche personnelle du module, sans attendre une fusion ; chacun garde son fichier individuel.
