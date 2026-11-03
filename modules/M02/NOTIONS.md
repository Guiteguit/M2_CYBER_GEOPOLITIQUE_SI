# M02 — Repères pour l’analyse

Une annonce BGP décrit une possibilité de routage connue d’un observateur. L’ASN d’origine est l’AS qui présente le préfixe comme issu de son réseau ; l’AS_PATH est une information de contrôle de routage, pas un traceroute physique.

Les collecteurs RIS reçoivent les observations de leurs pairs. Une disparition chez un collecteur ne démontre pas à elle seule une disparition mondiale. Une fraction de pairs observants ne mesure pas directement le nombre de clients affectés.

Séparer trois questions : la route est-elle observée ? Un chemin permet-il d’atteindre la destination depuis une sonde donnée ? L’application répond-elle correctement ? DNS, caches, authentification et autres dépendances peuvent compliquer la reprise.

Le contexte international peut rendre une dépendance opérateur importante. Il ne transforme pas automatiquement un retrait d’annonce en censure ou en attaque étatique. Préciser les preuves de causalité et l’acteur capable de confirmer un changement.

Référence méthodologique : [RIPE NCC — Routing History](https://stat.ripe.net/docs/data-api/api-endpoints/routing-history).

## Lire le JSON réel sans outil supplémentaire

Vous pouvez ouvrir le fichier dans GitHub et rechercher les noms de champs. Une enveloppe contient la provenance et `response` la réponse de l’API. Commencez par `source_url`, `collected_at_utc`, puis `response.data.query_starttime` et `query_endtime`. Une fenêtre demandée dans l’URL peut différer de la période effectivement disponible : votre analyse doit citer cette dernière.

Dans `by_origin`, chaque groupe contient une valeur `origin`, des préfixes et leurs périodes. Quand `include_first_hop=true`, le format de cette collecte peut associer premier saut puis origine, par exemple fictif `64501 64520`. Une autre ligne `64502 64520` change le premier saut, sans nécessairement changer l’origine. Ne pas confondre les groupes et les ASN d’origine distincts. Si le format reste ambigu, citez la valeur brute et marquez l’interprétation comme à vérifier.

Les champs de visibilité portent sur les pairs des collecteurs, selon les filtres. `-1`, si présent pour la visibilité normalisée, ne signifie pas une visibilité négative à interpréter : c’est une valeur non exploitable dans ce contexte. Ne la transformez pas en proportion d’utilisateurs.

## Lire les CSV de l’exercice

Les CSV ont leur propre scénario fictif. Les colonnes sont décrites dans [les données](donnees/README.md). Lisez chaque ligne avec quatre repères : instant, observateur, objet observé et résultat. R1/R2 sont des collecteurs ; A/B des sondes applicatives différentes. Le dossier ne donne pas une correspondance entre ces machines ou leurs lieux.

Exemple d’apprentissage distinct : six pairs sur huit observent un préfixe, soit `6 / 8 = 0,75 = 75 %` des pairs examinés. Cela ne prouve ni 75 % des utilisateurs connectés ni 25 % d’utilisateurs en panne. Une sonde qui reçoit HTTP 503 a reçu une réponse HTTP ; l’application peut néanmoins ne pas fournir le service demandé.

Pour comparer deux instants, gardez le même préfixe et le même observateur, puis examinez la population de pairs. Pour comparer les couches, ajoutez les résultats applicatifs à la même chronologie sans supposer qu’un événement a causé tous les autres.

## Construire deux hypothèses et les surveiller

Une hypothèse décrit un mécanisme possible sous des conditions. Une bonne analyse donne un fait qui la soutient, une autre explication et une preuve à demander pour les départager. Les seules traces fournies peuvent ne pas suffire à attribuer la cause ; ce constat ne bloque pas le module.

Un indicateur utile associe source, responsable, fréquence, déclencheur et action. « Surveiller Internet » est trop vague. Exemple distinct : « si deux contrôles successifs d’un parcours métier échouent, le pilote SI vérifie la portée depuis un second point et consulte les événements de changement ». Le seuil est une proposition à justifier, pas un engagement du fournisseur.

Avant de passer à l’exercice, expliquez à un autre pourquoi « route visible », « destination joignable » et « service métier utilisable » sont trois résultats différents.
