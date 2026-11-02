# M02 — Repères pour l’analyse

Une annonce BGP décrit une possibilité de routage connue d’un observateur. L’ASN d’origine est l’AS qui présente le préfixe comme issu de son réseau ; l’AS_PATH est une information de contrôle de routage, pas un traceroute physique.

Les collecteurs RIS reçoivent les observations de leurs pairs. Une disparition chez un collecteur ne démontre pas à elle seule une disparition mondiale. Une fraction de pairs observants ne mesure pas directement le nombre de clients affectés.

Séparer trois questions : la route est-elle observée ? Un chemin permet-il d’atteindre la destination depuis une sonde donnée ? L’application répond-elle correctement ? DNS, caches, authentification et autres dépendances peuvent compliquer la reprise.

Le contexte international peut rendre une dépendance opérateur importante. Il ne transforme pas automatiquement un retrait d’annonce en censure ou en attaque étatique. Préciser les preuves de causalité et l’acteur capable de confirmer un changement.

Référence méthodologique : [RIPE NCC — Routing History](https://stat.ripe.net/docs/data-api/api-endpoints/routing-history).
