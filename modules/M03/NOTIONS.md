# M03 — Repères

Localiser le stockage ne décrit pas nécessairement le plan de contrôle : administration, identité, clés, DNS et support peuvent rester dépendants d’autres acteurs. Un contrat avec une société locale ne suffit pas à décrire toute la sous-traitance.

La réversibilité demande des données exploitables, des accès, une destination, des compétences et un temps compatible avec l’activité. Un export disponible dans un contrat n’est pas encore une restauration testée.

Une alternative peut réduire une concentration et introduire d’autres coûts ou risques. Justifier le choix par les dépendances prioritaires, pas par le nombre de logos ou de régions. Préciser les scénarios dans lesquels les services resteraient communément affectés.

Les deux offres sont fictives. Aucune conclusion de conformité ou d’extraterritorialité réelle n’est attendue : une question juridique précise peut être transmise à une fonction compétente.

## Lire un manifeste d’architecture

Dans chaque JSON, `composants` liste des fonctions. `provider_id` sert à identifier un acteur ; comparez sa valeur exacte entre les fonctions et entre les offres. Une fonction peut dépendre de l’application d’un fournisseur et de l’identité d’un autre. L’existence de deux contrats n’implique donc pas deux chaînes indépendantes.

Construisez un tableau : fonction, acteur, relation avec un autre acteur, localisation déclarée, preuve et inconnue. Une carte peut ensuite représenter ces mêmes relations. Les lieux non renseignés restent inconnus ; ne pas déduire tous les accès de la seule valeur `hebergement_declare`.

## Distinguer données, contrôle et exploitation

Le plan de données concerne notamment les traitements et le stockage. Le contrôle comprend les moyens d’administrer et d’autoriser l’accès ; l’exploitation dépend aussi des procédures et des compétences. Ce sont des angles de lecture, pas des catégories qui garantissent une indépendance.

Exemple distinct : un export est stocké dans une seconde région, mais sa console demande la même identité que l’application. La copie peut exister alors que son accès reste dépendant du même service. Il faut vérifier les comptes de secours et le test de reprise, sans conclure automatiquement que la copie serait inutilisable.

## Comparer les prix et la capacité

Pour une durée en mois : `mise en place + nombre de mois × récurrent mensuel + frais de sortie applicables`. Exemple indépendant du dossier : 1 100 € de mise en place et 80 € par mois pendant douze mois donnent 2 060 €, avant un éventuel coût de sortie décrit au contrat.

Dans le cas Asteria, le contrat indique quand les frais de sortie sont dus et ce que couvrent les jours d’équipe. Utilisez cette convention. N’ajoutez pas de prix de personnel, de taxes ou de double exploitation non fournis. Les vingt jours disponibles constituent une contrainte différente de l’argent : une option peut être financièrement possible mais demander trop de travail.

Chaque résultat présente sa formule et sa source. Un autre étudiant refait le calcul. Si deux résultats diffèrent, vérifier durée, inclusion de la sortie et périmètre des jours avant de débattre du choix.

## Écrire une décision utile malgré des inconnues

Une note d’arbitrage comporte : choix ou condition, dépendance réduite, dépendance conservée, faisabilité, preuve manquante et point de réexamen. Le déplacement géographique peut réduire une exposition tout en conservant un acteur de contrôle ou de support ; il faut nommer précisément lequel d’après les données.

Demander une preuve ne signifie pas refuser toute décision. On peut retenir une option sous réserve d’un test, ou préférer l’autre en expliquant le risque conservé. Les deux choix peuvent être argumentés : une conformité supposée à partir d’un pays ne remplace pas les preuves techniques ou contractuelles.

À la fin de la lecture, chacun explique comment une même option peut gagner en autonomie sur une fonction et rester dépendante sur une autre.
