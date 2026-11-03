# M03 — Changer d’implantation réduit-il les dépendances ?

**90 minutes · Autonomie complète · Architectures, coûts et décision · Formatif.** Un navigateur, du papier ou un document texte et une calculatrice suffisent. Python et le tableur sont facultatifs. Aucun fournisseur fictif ne doit être recherché ou contacté.

## Mission et contraintes

Asteria compare deux offres pour ses applications. Elle veut réduire certaines dépendances transfrontières et dispose, pour cette comparaison, de **45 000 € sur dix-huit mois et vingt jours d’équipe**. Ce plafond ne remplace pas un budget global du SI.

Les [offres JSON](donnees/offre_A.json) et [les contrats](donnees/CONTRATS.md) sont fictifs. Asteria peut renouveler A ou migrer vers B. Vous pouvez conditionner votre choix à des preuves. Le pays d’hébergement annoncé n’est pas une justification suffisante à lui seul.

C consigne la synthèse. A commence par contrats/coûts, B par l’architecture B, C par A ; chacun vérifie une partie du raisonnement des autres. Vous n’avez pas à attendre la validation de M02 pour travailler : les données de M03 sont complètes pour la comparaison demandée.

## Chronomètre — 90 minutes

| Minutes | Travail autonome |
|---|---|
| 0–5 | Hypothèse individuelle et répartition |
| 5–20 | Lecture de [NOTIONS.md](NOTIONS.md) et des contraintes du contrat |
| 20–40 | Lire les deux JSON et construire leurs cartes de dépendances |
| 40–58 | Calculer coûts et charges, relever preuves et inconnues |
| 58–70 | Confronter deux options et une objection à chacune |
| 70–83 | Rédiger la décision et trois demandes de preuves |
| 83–90 | [Auto-vérification](AUTO_VERIFICATION.md), enregistrement et bilan du bloc |

## 1. Votre point de départ

Chacun écrit : « Déplacer les données dans un autre pays : quelle dépendance disparaît nécessairement, et laquelle peut rester ? » Gardez la réponse initiale avant de lire les notions. Relisez-la en fin de module.

## 2. Comparer les architectures

Ouvrir [offre A](donnees/offre_A.json) et [offre B](donnees/offre_B.json). Pour chaque fonction, relever le `provider_id`, la localisation déclarée si elle existe et les dépendances d’administration ou d’identité décrites. Utiliser une table « fonction — acteur A — acteur B — dépendance supplémentaire — preuve » si un dessin prend trop de temps.

Dessiner ou lister les relations nécessaires à l’usage et à la restauration. Comparer les identifiants d’acteurs exacts entre les offres. Expliquer ce qu’un changement de calcul, de stockage ou de DNS change, et ce qu’il laisse commun.

Consulter ensuite les [contrats fictifs](donnees/CONTRATS.md) : une déclaration, une possibilité prévue et un résultat testé ne sont pas équivalents. Relever une incertitude importante pour chaque offre.

## 3. Calculer sans inventer des coûts

Calculer sur dix-huit mois la mise en place et les récurrents. Appliquer les frais de sortie de A seulement dans le cas décrit par le contrat. Les jours d’équipe constituent une seconde contrainte ; ne pas leur inventer un tarif journalier.

Écrire la formule, les données utilisées et le résultat. Faire refaire le calcul par une autre personne. Le [script facultatif](AIDE.md) peut contrôler les montants de base, mais la convention de sortie et la décision restent à analyser.

## 4. Confronter les choix

Chacun dispose de deux minutes pour présenter un constat, une preuve et une limite. Pendant les six minutes restantes, défendre au moins deux options : renouveler, migrer ou conditionner l’une de ces décisions. Une personne doit chercher un contre-argument au choix qu’elle préfère.

Pour chaque option, examiner coût, jours disponibles, dépendance réduite, dépendance conservée et preuve à obtenir. Si vous n’êtes pas d’accord, écrire le désaccord et la condition qui ferait changer la décision ; ne pas attendre un arbitrage absent.

## 5. Livrables et bilan

Compléter [SYNTHESE.md](../../rendus/M03/SYNTHESE.md) : deux cartes ou listes de relations, tableau de comparaison, note d’arbitrage d’une page maximum et trois demandes de preuves précisant interlocuteur et effet sur la décision. Relier la recommandation à un acteur de contrôle ou de support international, sans inventer une règle de droit.

Chacun complète son fichier individuel. C dépose la synthèse sur `tp/autonomie-c`, puis renseigne le [bilan du bloc](../../rendus/M03/BILAN_AUTONOMIE.md) avec A et B. Laisser les trois pull requests ouvertes, sans fusion ni attente de validation.

M01–M03 restent formatifs. À la fin des 90 minutes, conserver le travail même partiel, relever les questions restantes et terminer le bloc. **Le M04 commence avec le retour du formateur** ; ne pas lancer ses manipulations en avance.
