# Contrat de données fictif

Asteria demande de reprendre **les commandes confirmées uniquement**. Une commande annulée doit être exclue et son exclusion explicitée ; aucune donnée ne doit disparaître sans règle métier.

La cible est une table SQLite `orders` avec `id` unique non vide, `client` non vide et `quantity` entier strictement positif. L’échange intermédiaire est un CSV UTF-8 avec l’en-tête exact `id,client,quantity`. Le nom client est une donnée fictive ; il doit être conservé à l’identique.

Le fichier `reference_metier.csv` représente le contrôle métier convenu avant la migration. Il ne doit pas être recalculé à partir du résultat importé, ni modifié pour faire réussir un test. Il contient les trois commandes C001/C002/C003, neuf unités au total. Comparer seulement le total est insuffisant : contrôler aussi chaque identifiant, client et quantité.

Un second import du même fichier doit être rejeté sans doubler les commandes ni laisser un import partiel. La cible n’offre ici ni HTTP ni authentification. L’exercice démontre une portabilité des données et une consultation locale, pas le remplacement de toutes les fonctions du SI ni une bascule de production.

Conserver une copie source intacte et créer une nouvelle base cible pour revenir en arrière. Ne toucher ni à `lab/runtime/commandes.csv` ni aux données de M08. Aucune coupure ou suppression du système source réel n’est demandée.
