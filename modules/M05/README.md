# M05 — Démontrer un repli et une restauration

> **Autonomie accompagnée :** vous conduisez ce module à partir des supports. Le formateur est présent en soutien, pour une aide ciblée et pour challenger vos décisions ; aucun exposé oral n’est nécessaire pour commencer. Lire [le fonctionnement commun](../../docs/AUTONOMIE_ACCOMPAGNEE.md). Les apports sont dans [NOTIONS.md](NOTIONS.md), les aides dans [AIDE.md](AIDE.md), puis utiliser [AUTO_VERIFICATION.md](AUTO_VERIFICATION.md).

**90 min · Configuration, export et restauration locale · Évaluation collective.** Prérequis : laboratoire démarré, navigateur/HTTP et Python 3.10+. Ne pas réinstaller d’environnement. Les données sont fictives et les changements restent dans `lab/runtime`.

## Mission

Asteria demande deux preuves différentes : continuer à accéder aux applications lorsque l’identité principale est indisponible, et récupérer les commandes après une perte de données. Vous devez démontrer ces capacités puis dire ce qu’elles ne garantissent pas.

## Déroulé

| Minutes | Travail conduit par les étudiants |
|---|---|
| 0–8 | Écrire l’objectif et préparer les preuves de référence |
| 8–20 | Lire les notions ; prédire les critères de succès |
| 20–42 | Configurer le repli et exécuter les contre-tests |
| 42–65 | Exporter, simuler la perte puis restaurer et contrôler |
| 65–78 | Confronter les résultats et les dépendances restantes |
| 78–90 | Auto-vérifier, présenter et enregistrer |

## Partie A — Le repli d’accès

1. Sauvegarder votre configuration puis établir une référence saine. Le fichier d’incident fourni pour cette activité permet de reproduire l’indisponibilité de l’identité principale.
2. Examiner le second service d’identité fourni dans le laboratoire. Modifier uniquement la configuration des applications pour disposer d’un second choix. Justifier l’ordre des essais.
3. Avec la dépendance principale indisponible, démontrer les deux parcours HTTP et le fournisseur effectivement utilisé. Vérifier aussi l’échec lorsque les deux validations d’identité sont indisponibles : le modèle ne doit pas simplement ignorer ce contrôle.
4. Rétablir une configuration fonctionnelle pour la partie B. Conserver les différences et les preuves, pas seulement une réponse finale HTTP 200.

## Partie B — Les données

1. Exporter les commandes par le parcours prévu ; conserver le CSV et son manifeste. Relever nombre de commandes, quantité totale et empreinte.
2. Après vérification de cette copie, remplacer **uniquement** `lab/runtime/commandes.csv` par un CSV contenant son en-tête et aucune ligne de données. Ne pas supprimer de répertoire. Mesurer l’effet dans l’application : un HTTP 200 suffit-il à valider le service métier ?
3. Restaurer depuis votre export. Contrôler le contenu, les identifiants, les quantités et les deux parcours utilisateur.
4. Mesurer la durée entre votre constat de perte et le contrôle de reprise. Indiquer la date de l’export et les éventuelles écritures non couvertes. Cet essai ne démontre pas un RTO/RPO contractuel en production.

Les [aides](AIDE.md) donnent les commandes de gestion de fichiers et de restauration, pas une procédure complète de résilience.

## Contre-épreuve stratégique

Votre seconde identité et votre copie sont sur le même ordinateur. Que se passe-t-il si l’hôte, le disque ou l’équipe d’exploitation devient indisponible ? Quelle autonomie exigeriez-vous d’un fournisseur externe ? Qui pourrait autoriser une reprise sans les outils du fournisseur principal ?

## Livrables

[Rendu M05](../../rendus/M05/SYNTHESE.md) : configuration avant/après, matrice de tests principal seul/secondaire/deux indisponibles, export et manifeste, contrôles de contenu et chronologie de reprise. Terminer par deux exigences pour une architecture réellement indépendante, avec un moyen de les vérifier.

Le reset ne remplace pas la restauration : il recrée les données initiales et ne démontre pas l’usage de votre sauvegarde. Ne pas l’utiliser comme preuve de réussite de la partie B.

## Points de décision à consigner

- Avant le repli : quel ordre de dépendances proposez-vous et comment prouver qu’un contrôle reste actif ?
- Avant de vider les lignes fictives : la copie et son manifeste sont-ils présents et vérifiés ? Sinon, ne pas provoquer la perte ; poursuivre la vérification ou solliciter une aide.
- Après restauration : quel contrôle métier complète le HTTP 200 et quelles écritures ne sont pas démontrées récupérables ?

Ces traces ne sont pas des demandes d’autorisation. Après une aide ou une objection, expliquez vous-mêmes la décision retenue et testez-la. À la fin, le rapporteur consigne la synthèse sur sa branche personnelle du module, sans attendre une fusion ; chacun garde son fichier individuel.
