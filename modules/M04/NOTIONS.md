# M04 — Repères

Un point de dépendance commun peut exister alors que les applications ont des processus, noms, contrats ou ports distincts. La redondance doit se définir par rapport à un scénario de panne.

Un `/health` local peut confirmer que le serveur accepte une requête sans prouver que ses dépendances répondent. Tester un parcours utilisateur inclut d’autres couches. Dans ce modèle, chaque nouvelle requête d’application vérifie la validation d’identité ; il n’existe pas de session persistante qui masquerait temporairement la panne.

Le code 503 indique ici une incapacité applicative temporaire, pas une cause unique. Le code 502 du point d’entrée peut indiquer un échec de son appel amont. Le journal et un test direct permettent de distinguer les chemins.

Le contrôle de disponibilité de l’identité est simulé ; la panne HTTP et les appels entre composants sont réels dans votre machine. La résilience physique, le cloud et la juridiction ne sont pas testés par ce seul laboratoire.


## Lire une panne par couches

Raisonner du parcours utilisateur vers les composants : point d’entrée, application, dépendance d’identité, données. Une observation porte sur un chemin précis à un instant précis. Par exemple, dans un système de réservation fictif, une page de supervision verte et un achat impossible peuvent coexister : la première ne consulte pas forcément le service de paiement. Il faut comparer les chemins avant d’en déduire une cause.

Construire un tableau « test / résultat prédit / observation / interprétation / limite ». Une hypothèse utile permet de prédire plusieurs observations et de choisir un test qui la distingue d’une autre. Tester tout au hasard produit davantage de traces, sans nécessairement réduire l’incertitude. Conserver une référence avant l’incident permet de distinguer un changement de comportement d’une particularité déjà présente.

## Relier technique et stratégie SI

Deux fournisseurs peuvent partager une identité, un réseau, un opérateur ou une équipe d’administration. La diversité des marques ne prouve donc pas l’indépendance. Sur une carte, distinguer les composants observés des relations seulement supposées. Puis nommer le scénario auquel une amélioration répond : panne d’un processus, perte d’un site, rupture d’un contrat ou impossibilité d’exploiter un service.

Un résultat local ne démontre pas la localisation d’un traitement, sa juridiction ou l’autonomie d’un prestataire. Ces questions demandent d’autres preuves : architecture contractuelle, chaîne de sous-traitance, accès d’administration et exercice de sortie. Votre recommandation doit préciser ce qui est démontré ici et ce qui reste à vérifier ailleurs.
