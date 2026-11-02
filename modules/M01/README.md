# M01 — Qui contrôle réellement l’accès à un service numérique ?

**90 minutes · 3 étudiants · DNS, IP et ASN · Travail formatif.**

## Mission

> Asteria envisage de dépendre davantage de services Internet. Elle vous demande de montrer ce qu’une investigation externe permet d’apprendre sur les acteurs nécessaires à leur accès, et ce qui exige encore des informations du fournisseur.

Le domaine principal observé est **`isc.org`**, avec le nom **`www.isc.org`**. Ce sont des ressources publiques de l’Internet Systems Consortium, utilisées comme cas d’observation externe ; elles n’appartiennent pas à Asteria. L’objet du TP est la méthode d’enquête, pas un audit de sécurité d’ISC.

Les requêtes portent sur les enregistrements `NS`, `MX`, `A`, `AAAA` de `isc.org`, puis `CNAME`, `A`, `AAAA` de `www.isc.org`. Les noms retournés peuvent être résolus pour comprendre une relation déjà observée. Complétez par RIPEstat et la documentation officielle pertinente. Le TP ne demande ni scan, ni recherche de vulnérabilité, ni énumération automatisée de noms.

Les données changent : notez les dates, le résolveur ou le service interrogé, et conservez les résultats. Une différence avec une collecte précédente doit être expliquée ou laissée ouverte, pas masquée.

## Objectifs

- Distinguer domaine, service, adresse, préfixe, ASN et fournisseur.
- Identifier les dépendances visibles du DNS, du web et de la réception du courrier.
- Relier une observation à sa preuve et à ses limites.
- Décrire une dépendance commune possible sans inventer la topologie d’origine.
- Formuler une recommandation SI et une question sur le contrôle de ces ressources.

## Avant les outils — 10 minutes

Chacun répond en quelques lignes dans son fichier individuel :

1. Qui pourrait empêcher l’accès à un service web, sans être propriétaire de son serveur ?
2. Quelles observations chercherez-vous pour identifier ces acteurs ?
3. Qu’est-ce qu’une recherche externe ne permettra probablement pas de démontrer ?

Le formateur recueille les trois propositions, puis consacre 15 minutes aux notions nécessaires. Ne cherchez pas une liste d’acteurs attendue à recopier.

## Investigation DNS — 20 minutes

Répondez aux questions suivantes avec vos outils ou les [collectes de secours](preuves_secours/README.md) :

- Quels serveurs sont annoncés comme autoritaires pour le domaine ?
- Vers quels noms est dirigée la réception du courrier ? Quelles adresses peut-on associer à ces noms si on poursuit la résolution ?
- Quelles adresses ou relations d’alias sont visibles pour le web ? Distinguez ce qui est demandé et les éventuelles autres réponses renvoyées.
- Une absence de réponse pour un type prouve-t-elle l’absence du service ? Précisez le statut de la réponse et le nom étudié.

Conservez des extraits exploitables plutôt qu’une capture de terminal illisible. Les commandes d’aide sont dans [AIDE.md](AIDE.md) ; vous choisissez la démarche.

## Du réseau aux acteurs — 20 minutes

- Choisissez une adresse effectivement observée et retrouvez son préfixe et son ou ses ASN annonçants avec RIPEstat.
- Identifiez l’organisation associée à l’ASN et distinguez cette information de la localisation des serveurs.
- Consultez une ou deux sources officielles pour confirmer un rôle technique ou comprendre les limites d’un service observé.
- Reliez au moins une dépendance à un acteur qui peut la modifier ou l’interrompre. Une nationalité ou un pays de registre ne constitue pas à lui seul une preuve de contrôle de toutes les données.

Pour répartir la recherche, A commence par DNS/délégation, B par web/IP/ASN, C par messagerie et documentation. Chacun réalise au moins une observation technique et en explique une limite. Faites ensuite une vérification croisée ; personne ne reste uniquement chargé de recopier les résultats.

## Confrontation — 15 minutes

Chaque étudiant dispose de deux minutes pour exposer une observation, sa preuve et une limite. Utilisez ensuite les neuf minutes restantes pour débattre :

1. Les fonctions étudiées dépendent-elles d’un acteur commun ? Qu’est-ce qui le démontre ?
2. Quel changement économique ou international pourrait affecter une de ces dépendances ? Formulez un scénario conditionnel, pas une accusation ou une règle juridique supposée.
3. Asteria pourrait-elle réduire cette dépendance ? Quelle information manque pour choisir une alternative ?

## Synthèse — 10 minutes

Produisez dans [SYNTHESE.md](../../rendus/M01/SYNTHESE.md) :

- une carte des relations observées, avec un sens de lecture et une distinction entre faits et hypothèses ;
- cinq observations sourcées ;
- trois inconnues importantes ;
- une recommandation de dix lignes maximum : décision proposée, raison, limite et vérification prioritaire.

Les positions individuelles, preuves et synthèse se trouvent dans [rendus/M01](../../rendus/M01/README.md). Les sources en ligne sont accompagnées d’une URL et d’une date ; les réponses techniques précisent la cible et le point d’observation. L’absence d’un nom de fournisseur dans un résultat n’autorise pas à inventer une attribution.

## Ce qui sera discuté

Le retour porte sur la précision, la traçabilité, l’interprétation et le lien entre dépendance technique et décision SI. Un résultat « inconnu avec une vérification pertinente » peut être meilleur qu’une conclusion catégorique non démontrée. Aucun classement de fournisseurs n’est attendu.

Le partage des accès et la prise en main de Git sont préparés avant la séance. En cas de problème réseau, utilisez les mêmes questions sur les résultats datés de secours, en signalant leur ancienneté. Le déroulé totalise 90 minutes ; il sera ajusté au rythme du groupe.
