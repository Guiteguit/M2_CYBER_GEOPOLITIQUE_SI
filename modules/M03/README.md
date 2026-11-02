# M03 — Changer d’implantation réduit-il les dépendances ?

**90 min · Analyse technique de deux architectures et calculs · Formatif.** Prérequis : M01–M02. Matériel : éditeur JSON, tableur ou Python 3.10+. Aucune infrastructure distante à déployer.

## Mission

Asteria compare deux offres pour ses applications de commandes et de collaboration. La direction souhaite réduire ses dépendances transfrontières, mais ne dispose que de vingt jours d’équipe et de 45 000 € sur dix-huit mois pour cette décision. Les données du dossier sont **fictives**, les pays également ; ce plafond est propre à la comparaison M03, pas un nouveau budget global du SI.

L’offre A peut être maintenue avec ses conditions proposées ; l’offre B est une alternative. Vous pouvez retenir l’une, la conditionner ou demander une modification limitée. Aucune offre n’est à choisir uniquement à partir du pays annoncé.

## Déroulé

| Temps | Travail |
|---|---|
| 0–10 | Hypothèse individuelle : « Quelle dépendance un changement de région supprime-t-il ? » |
| 10–25 | [Notions](NOTIONS.md) : plan de données, contrôle, accès et coût de sortie |
| 25–45 | Lire les deux JSON et construire leurs graphes de dépendances |
| 45–65 | Croiser [les pièces contractuelles fictives](donnees/CONTRATS.md), coûts et capacité d’exécution |
| 65–80 | Défendre des options contradictoires ; rechercher une condition qui change le choix |
| 80–90 | Note d’arbitrage et questions au fournisseur |

## Investigation

1. Examiner `donnees/offre_A.json` et `offre_B.json`. Séparer l’exploitant des applications, le fournisseur d’identité, les noms DNS, la sauvegarde et le support. Repérer les acteurs communs aux deux offres.
2. Dessiner les chemins nécessaires à l’utilisation et à la reprise. Expliquer pourquoi changer le stockage ne suffit pas forcément à changer le contrôle des accès.
3. Calculer les coûts sur dix-huit mois : mise en place + récurrents + sortie éventuelle de A si passage à B. Les jours d’équipe sont une contrainte distincte : ne pas leur inventer un taux journalier.
4. Distinguer les déclarations contractuelles, les tests fournis et les inconnues. Demander trois preuves capables de modifier l’arbitrage.
5. Proposer une décision compatible avec l’enveloppe et les jours disponibles, en identifiant au moins un risque conservé.

Le [script de comparaison](AIDE.md) affiche des éléments et calcule les montants de base. Vérifiez la convention de sortie de contrat : il ne choisit pas l’offre à votre place.

## Discussion géopolitique et SI

Un acteur extérieur peut-il encore conditionner l’accès après le déplacement des données ? Quels intérêts ont les éditeurs à faciliter ou ralentir une sortie ? Comment vérifier support, sous-traitance et autonomie sans conclure automatiquement à une obligation juridique ?

## Livrables

[Rendu M03](../../rendus/M03/SYNTHESE.md) : deux cartes sobres, tableau coût/charge/dépendances, décision d’une page maximum et trois demandes de preuves. Chacun explique une objection à sa propre préférence initiale. Les réponses alternatives sont recevables si elles respectent les données et les limites.
