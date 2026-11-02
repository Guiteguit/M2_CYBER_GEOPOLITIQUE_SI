# M04 — Repères

Un point de dépendance commun peut exister alors que les applications ont des processus, noms, contrats ou ports distincts. La redondance doit se définir par rapport à un scénario de panne.

Un `/health` local peut confirmer que le serveur accepte une requête sans prouver que ses dépendances répondent. Tester un parcours utilisateur inclut d’autres couches. Dans ce modèle, chaque nouvelle requête d’application vérifie la validation d’identité ; il n’existe pas de session persistante qui masquerait temporairement la panne.

Le code 503 indique ici une incapacité applicative temporaire, pas une cause unique. Le code 502 du point d’entrée peut indiquer un échec de son appel amont. Le journal et un test direct permettent de distinguer les chemins.

Le contrôle de disponibilité de l’identité est simulé ; la panne HTTP et les appels entre composants sont réels dans votre machine. La résilience physique, le cloud et la juridiction ne sont pas testés par ce seul laboratoire.
