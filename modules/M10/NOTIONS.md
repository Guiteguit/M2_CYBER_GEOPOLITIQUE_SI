# M10 — Données exportées et réversibilité démontrée

## Définir ce qui doit être récupéré

Un fichier exporté n’est pas encore un service utilisable. Il faut connaître la signification des champs, les statuts à retenir, les règles d’unicité et les contrôles métier. La transformation relie le modèle source au modèle cible. Renommer un champ ne suffit pas si ses valeurs ou sa granularité ont changé. Écrire les règles avant de transformer évite de sélectionner après coup les seules données qui réussissent.

La référence métier est indépendante du résultat produit. Si on la reconstruit à partir de l’import, une erreur peut se retrouver des deux côtés et passer inaperçue. Vérifier les lignes, leurs identifiants, leurs valeurs et les agrégats. Deux ensembles peuvent totaliser neuf unités en contenant des commandes différentes. Dans ce TP, la référence est fournie et figée ; en production, elle devrait être établie et acceptée avec les métiers.

## Importer sans masquer les erreurs

Une transaction permet ici d’annuler les insertions d’un import qui échoue. Le contrôle d’unicité empêche un second import de doubler les commandes. Le choix de rejet est explicite ; d’autres systèmes peuvent gérer une mise à jour ou une fusion avec des règles différentes. Ne pas confondre ce comportement avec une synchronisation bidirectionnelle. L’outil n’applique aucune suppression ni mise à jour implicite.

Préserver la source, conserver les sorties et utiliser une cible distincte facilitent le retour arrière de l’essai. L’outil refuse d’écraser un CSV existant : changer de nom et expliquer la nouvelle tentative. La lecture de la base ne reçoit pas le fichier source ; sa réussite après renommage de la copie source apporte une preuve limitée d’indépendance des données consultées.

## De la portabilité à une stratégie de sortie

Le test ne démontre pas la récupération des comptes, clés, journaux historiques ou interfaces, ni la gestion des écritures pendant une migration. Une sortie de production exige aussi responsables, accès, procédures, sauvegardes, contrôles de sécurité et critères de bascule ou d’annulation. Une cible locale sur le même poste conserve une dépendance au poste et à son exploitant.

Un risque international peut toucher l’accès au support, aux outils d’administration ou aux licences sans altérer immédiatement les données. Pour Asteria, formuler des exigences vérifiables : obtenir régulièrement un export documenté, prouver sa restauration et garantir des accès de secours indépendants. Ces pistes ne constituent pas une validation juridique d’un contrat réel. Terminer par ce que les preuves autorisent à décider et les conditions encore manquantes.
