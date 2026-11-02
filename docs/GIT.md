# Git : préparer le rendu sans y passer la séance

Les accès au dépôt sont attribués par le formateur. Un dépôt privé exige une authentification autorisée ; ne jamais mettre de mot de passe ou de jeton dans les fichiers ou l’URL du dépôt.

## Préparation hors du temps d’investigation

```bash
git clone https://github.com/Guiteguit/M2_CYBER_GEOPOLITIQUE_SI.git
cd M2_CYBER_GEOPOLITIQUE_SI
```

Pour le groupe de trois, utiliser **une branche par contribution individuelle**, puis une branche de synthèse collective. Cela évite que plusieurs personnes réécrivent simultanément le même compte rendu.

Exemple pour la personne A :

```bash
git switch -c tp/m01-a
# Compléter rendus/M01/individuel/A.md et ajouter ses preuves datées.
git add rendus/M01/individuel/A.md rendus/M01/preuves/
git commit -m "M01 : observations et analyse individuelle A"
git push -u origin tp/m01-a
```

B et C utilisent respectivement `tp/m01-b` et `tp/m01-c`, et leur propre fichier. N’ajouter dans `preuves` que ses propres fichiers pour éviter les collisions. Le fichier personnel contient une hypothèse de départ puis une conclusion après l’enquête ; il n’exige pas de saisir de nouveau toutes les données collectées.

## Pull requests

Depuis GitHub, ouvrir une pull request de sa branche vers `main`. Le modèle de description propose observations, limites et recommandation. Le formateur peut discuter les conclusions dans la revue. Ne pas demander de revue à une personne extérieure au groupe sans instruction.

Après intégration des contributions, une personne se charge de la synthèse :

```bash
git switch main
git pull --ff-only
git switch -c tp/m01-synthese
# Compléter rendus/M01/SYNTHESE.md avec le groupe.
git add rendus/M01/SYNTHESE.md
git commit -m "M01 : synthèse collective et décision SI"
git push -u origin tp/m01-synthese
```

Ouvrir ensuite la pull request de synthèse. Si les contributions ne sont pas encore intégrées, attendre leur intégration ou travailler provisoirement dans un document commun : la gestion Git ne doit pas empêcher la restitution pédagogique.

Ne pas utiliser `push --force` pour résoudre un problème courant. En cas de conflit ou de droits insuffisants, conserver ses fichiers localement et demander l’aide du formateur. Si Git bloque pendant le TP, rendre les fichiers au formateur pour intégration ultérieure.
