# M08 — Critères et limites à garder en tête

Ce module mobilise les acquis, sans nouvelle technologie. Une correction minimale doit être reliée à une hypothèse vérifiée. Une mesure de succès doit couvrir le parcours utilisateur et l’état métier, puis les dépendances restantes.

Documenter ce que le laboratoire ne démontre pas : autonomie physique, conformité juridique, haute disponibilité multi-site, identité de production ou indépendance réelle entre prestataires. Ces limites deviennent des exigences à tester dans la feuille de route.

Une restitution claire explique les décisions, leurs preuves et leurs conditions de validité. Le fait de changer d’hypothèse après un test est un résultat positif s’il est justifié.


## Conduire une reprise avec des preuves

Commencer par le mandat : quels parcours rétablir, quelles données retrouver et quels contrôles conserver ? Une priorité sans critère de réussite ne permet pas de déclarer la reprise. Préserver les traces et la configuration avant de changer l’état ; une réparation qui efface ses propres indices réduit la capacité à expliquer ce qui s’est passé.

Écrire une hypothèse et une alternative, puis annoncer le résultat attendu d’un test qui les distingue. Privilégier les vérifications rapides et informatives. La capsule attribuée ne se déduit pas de la réussite d’un exercice précédent : observer l’état actuel. L’existence d’une copie de données ne signifie pas qu’elle soit nécessaire à toute correction.

## Décider, contrôler, expliquer

Une intervention minimale est plus facile à relier à un effet mesuré. Conserver le diff ou la description exacte de l’opération et vérifier les parcours ainsi que le contenu métier. Dans cet exercice, retrouver les deux parcours et les commandes attendues en conservant le contrôle d’identité est plus exigeant qu’obtenir un seul HTTP 200. Une réinitialisation ou une réinjection de capsule ne constitue pas une preuve de réparation.

La décision stratégique vient ensuite : quelle dépendance a été mise en évidence, quel scénario reste mal couvert, quelle mesure prioriser et quelle preuve demander pour la valider ? Distinguer la reprise locale démontrée d’une promesse de résilience en production.

Le formateur reste disponible pendant l’épreuve et évalue votre compréhension. Une aide ne doit pas être dissimulée : consigner son apport, puis expliquer votre choix et vos propres vérifications. L’auto-vérification prépare la soutenance ; elle ne remplace pas l’évaluation.
