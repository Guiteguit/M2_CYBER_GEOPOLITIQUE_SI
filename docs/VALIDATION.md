# Vérifications de préparation

Version du parcours préparée le 2 novembre 2026. Ces vérifications portent sur le matériel livré ; elles ne remplacent pas un essai de séance avec les trois étudiants.

## Exécution

Les contrôles suivants ont réussi sous Linux avec Python 3.12, dans un répertoire d’état temporaire et une plage de ports locale distincte :

- démarrage des cinq composants et réponses des deux parcours ;
- contenu initial de trois commandes et neuf unités ;
- indisponibilité de l’identité commune et santé locale des applications ;
- repli vers la seconde validation, puis échec lorsque les deux validations sont indisponibles ;
- export CSV, perte des lignes, restauration et contrôle du contenu ;
- rejet d’une copie modifiée dont l’empreinte ne correspond plus au manifeste ;
- reproduction d’une erreur de configuration d’identité et correction ;
- trois familles d’incident final, avec reprise technique et métier après intervention.

Les aides de calcul des offres, les fractions du CSV BGP et les vérifications des manifestes M06/M07 ont également été exécutées. La syntaxe Python et JSON, la présence des supports de chaque module et les liens locaux ont été contrôlés.

## Périmètre restant à vérifier en classe

Faire le prévol sur chaque poste et vérifier les commandes Python/Git. L’exécution Windows et macOS n’a pas été testée dans cette préparation ; les commandes et scripts sont conçus avec la bibliothèque standard, sans dépendance au shell pour le laboratoire lui-même. L’aide fournit les variantes Windows.

Les quatre-vingt-dix minutes sont réparties dans chaque mission ; le rythme réel de lecture et de restitution reste à mesurer. Les observations publiques pourront changer ; les fichiers datés et les corpus simulés fournissent une base reproductible.

Les tests locaux ne démontrent ni haute disponibilité physique, ni SSO de production, ni sécurité d’un hébergement Internet. Les limites font partie des discussions demandées aux étudiants.
