# M05 — Repères

Une bascule conserve un service malgré une dépendance indisponible. Une restauration récupère un état de données. L’une ne prouve pas automatiquement l’autre.

Le RTO est un objectif de délai de reprise ; le RPO un objectif sur la perte de données acceptable, souvent exprimé en durée. Mesurer une reprise en classe donne un résultat d’essai, pas une garantie générale. Un export sans écritures intervenues ensuite ne démontre pas la récupération d’écritures futures.

L’empreinte SHA-256 permet ici de comparer un fichier au manifeste de référence. Si le fichier et son manifeste peuvent être modifiés ensemble, ce mécanisme ne prouve pas l’authenticité face à un adversaire capable de modifier les deux. Il ne remplace pas non plus un test d’import et un contrôle métier.

Le second service local permet de tester un choix logique. Il ne supprime ni l’hôte, ni le disque, ni le système, ni les compétences communes. Formuler les exigences de production correspondantes : contrôle d’accès indépendant, procédures et copies séparées, capacité de test et de sortie.
