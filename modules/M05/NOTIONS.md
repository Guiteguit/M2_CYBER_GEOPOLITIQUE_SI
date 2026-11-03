# M05 — Repères

Une bascule conserve un service malgré une dépendance indisponible. Une restauration récupère un état de données. L’une ne prouve pas automatiquement l’autre.

Le RTO est un objectif de délai de reprise ; le RPO un objectif sur la perte de données acceptable, souvent exprimé en durée. Mesurer une reprise en classe donne un résultat d’essai, pas une garantie générale. Un export sans écritures intervenues ensuite ne démontre pas la récupération d’écritures futures.

L’empreinte SHA-256 permet ici de comparer un fichier au manifeste de référence. Si le fichier et son manifeste peuvent être modifiés ensemble, ce mécanisme ne prouve pas l’authenticité face à un adversaire capable de modifier les deux. Il ne remplace pas non plus un test d’import et un contrôle métier.

Le second service local permet de tester un choix logique. Il ne supprime ni l’hôte, ni le disque, ni le système, ni les compétences communes. Formuler les exigences de production correspondantes : contrôle d’accès indépendant, procédures et copies séparées, capacité de test et de sortie.


## Concevoir une démonstration de résilience

Écrire les critères de réussite avant la manipulation évite de les adapter après coup. Un repli doit conserver le parcours utile et ses contrôles ; un accès obtenu en supprimant le contrôle d’identité ne prouve pas une continuité équivalente. Le test négatif est donc essentiel : que doit refuser le système lorsque les dépendances nécessaires sont toutes indisponibles ?

Une sauvegarde utile est accessible au moment de la panne, lisible et importable. Son existence seule ne suffit pas. Dans un exemple de stock fictif, retrouver un fichier de dix lignes ne prouve pas que les dix articles attendus sont récupérés : il faut contrôler identifiants, quantités et usage par l’application. Conserver une copie vérifiée avant de simuler la perte ; si la copie est douteuse, arrêter cette étape et demander de l’aide.

## Mesurer sans généraliser

Noter l’heure de l’export, le constat de perte et le contrôle final de reprise. Le délai mesuré dépend des conditions de l’exercice et de votre préparation. Un objectif de production demanderait des scénarios, responsabilités et essais répétés. La perte potentielle concerne aussi les modifications intervenues après la copie : le laboratoire ne prouve pas leur récupération.

La dépendance géopolitique peut rendre un service ou ses outils d’administration inaccessibles sans panne physique. Une stratégie de sortie doit prévoir données, formats, clés, identités, compétences et droit d’usage. Proposer une exigence vérifiable : qui peut restaurer, avec quels outils indépendants, à partir de quelle copie et dans quel scénario ?
