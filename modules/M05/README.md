# M05 — Démontrer un repli et une restauration

**90 min · Configuration, export et restauration locale · Évaluation collective.** Prérequis : laboratoire démarré, navigateur/HTTP et Python 3.10+. Ne pas réinstaller d’environnement. Les données sont fictives et les changements restent dans `lab/runtime`.

## Mission

Asteria demande deux preuves différentes : continuer à accéder aux applications lorsque l’identité principale est indisponible, et récupérer les commandes après une perte de données. Vous devez démontrer ces capacités puis dire ce qu’elles ne garantissent pas.

## Déroulé

| Temps | Activité |
|---|---|
| 0–10 | Prédire la différence entre disponibilité et récupération de données |
| 10–25 | [Notions](NOTIONS.md) : bascule, intégrité, RTO/RPO et limites d’un essai |
| 25–45 | Configurer et tester un chemin d’identité alternatif |
| 45–65 | Exporter, provoquer une perte limitée aux données fictives et restaurer |
| 65–80 | Contre-tests et discussion des dépendances restantes |
| 80–90 | Tableau de preuves et recommandation de résilience |

## Partie A — Le repli d’accès

1. Sauvegarder votre configuration puis établir une référence saine. L’injection M04 permet de reproduire l’indisponibilité de l’identité principale.
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
