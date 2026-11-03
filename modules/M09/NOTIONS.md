# M09 — Dépendances logicielles et autonomie de maintenance

## Inventaire, chaîne et risque

Un inventaire décrit les composants connus dans un périmètre donné. Il peut manquer des dépendances de construction, des extensions ou un service distant. Une SBOM vise une description structurée de composants et de relations ; le JSON de ce TP simplifie cette idée sans prétendre respecter un format industriel. Une dépendance directe est appelée par le composant étudié ; une dépendance transitive est atteinte par une autre. Des applications distinctes peuvent ainsi partager la même bibliothèque.

Le mainteneur, la forge, le distributeur et l’exploitant sont des rôles différents. Deux noms de fournisseurs ne prouvent pas deux chaînes de contrôle indépendantes. Un composant disponible dans une archive peut toujours dépendre d’un service d’identité ou d’un outil de construction absent. Une affirmation d’autonomie doit nommer le scénario et les ressources indispensables.

## Un avis ne remplace pas un diagnostic

Une correspondance composant/version indique un problème à examiner. Il faut encore comparer les conditions décrites, la configuration active, les entrées accessibles et l’impact métier. Une sévérité ne mesure pas seule la priorité pour Asteria. Une condition déclarée absente dans ce dossier réduit une hypothèse ; en production, elle demanderait une vérification sur le déploiement concerné.

Une version corrigée peut imposer un changement dans son appelant. En supprimant une correspondance d’avis tout en rompant une contrainte de compatibilité, on n’a pas démontré un état exploitable. Distinguer audit statique et test fonctionnel. Le script ne télécharge et n’exécute aucune bibliothèque ; un résultat candidat nécessite donc des tests supplémentaires avant un déploiement réel.

## Continuer aujourd’hui et maintenir demain

La disparition d’une forge n’arrête pas nécessairement un binaire déjà installé. Elle peut cependant empêcher de reconstruire, corriger ou agrandir le service. Une copie indépendante des sources, dépendances, outils et droits nécessaires est une piste, à éprouver par reconstruction dans un environnement séparé. Les aspects contractuels restent des demandes de preuves, pas des conclusions juridiques du TP.

Pour chaque action, écrire : dépendance réduite, hypothèse, test d’acceptation, moyen de retour arrière et risque non traité. Un lot technique cohérent peut être prioritaire malgré une sévérité moindre si l’exposition et l’impact sont mieux établis. Accepter le débat, puis borner la recommandation avec les éléments réellement disponibles.
