# M06 — Repères

Un événement concomitant peut être une cause, une conséquence ou une coïncidence. Aligner les horodatages, les composants et les identifiants avant de relier les événements. Une absence dans un journal partiel n’est pas une preuve d’absence globale.

Une tentative de connexion échouée n’est pas une connexion réussie. Une connexion réussie ne démontrerait pas encore, seule, la responsabilité d’un changement. Une cause technique et l’identité de son auteur exigent des preuves différentes.

Préserver une copie et proposer une correction minimale rend le raisonnement vérifiable. Un reset peut restaurer une démonstration sans avoir identifié ou documenté la panne. Les sauvegardes, accès et outils de diagnostic peuvent eux-mêmes dépendre du composant touché.

La reprise se valide par un parcours utilisateur et le contenu attendu, pas seulement par un processus actif. Décrire les limites avant d’affirmer qu’une crise est terminée.


## Séparer observation, hypothèse et conclusion

Une trace rapporte un événement selon le point de vue de son producteur. Elle peut être incomplète, décalée dans le temps ou dépendre d’une configuration particulière. Relever le composant, le moment, le symptôme et le contexte avant de conclure. Les dates des données synthétiques ne sont pas celles de vos essais locaux : conserver deux chronologies clairement identifiées.

Un test discriminant doit pouvoir faire évoluer le diagnostic. Exemple distinct du cas : si un service de facturation répond directement mais échoue via un relais, comparer ces deux chemins aide à localiser la rupture ; cela ne suffit pas à nommer son auteur. Formuler au moins deux explications plausibles puis choisir le test dont les résultats attendus diffèrent entre elles.

## Corriger et attribuer sont deux enquêtes

Avant une correction, sauvegarder l’état utile et expliquer ce que le changement doit produire. Modifier un élément à la fois facilite l’interprétation. Après le changement, rejouer le test en échec et un parcours auparavant fonctionnel : une réparation locale peut déplacer le problème. Un retour HTTP favorable doit encore être relié au contenu métier attendu.

Démontrer un mécanisme technique ne démontre ni intention ni identité de l’acteur. Une erreur, une action malveillante et une intervention autorisée peuvent parfois produire le même effet. L’attribution politique nécessite des éléments supplémentaires et une appréciation de leur fiabilité. Pour Asteria, une décision de reprise peut être justifiée malgré une attribution inconnue : exprimer le risque résiduel plutôt qu’inventer une certitude.
