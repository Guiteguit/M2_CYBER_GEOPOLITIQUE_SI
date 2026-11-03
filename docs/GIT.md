# Git : préparer le rendu sans y passer la séance

> **M01–M03 sans formateur :** suivre d’abord [le guide autonome](DEMARRER_AUTONOMIE.md). Une branche personnelle couvre les trois modules et aucune fusion n’est attendue. Le fonctionnement ci-dessous s’applique normalement à partir de M04.

Les accès au dépôt sont attribués par le formateur. Un dépôt privé exige une authentification autorisée ; ne jamais mettre de mot de passe ou de jeton dans les fichiers ou l’URL du dépôt.

## Préparation hors du temps d’investigation

```bash
git clone https://github.com/Guiteguit/M2_CYBER_GEOPOLITIQUE_SI.git
cd M2_CYBER_GEOPOLITIQUE_SI
```

Pour le groupe de trois, utiliser **une branche personnelle par module** ; le rapporteur utilise aussi cette branche pour la synthèse collective. Cela évite que plusieurs personnes réécrivent simultanément le même compte rendu.

Exemple pour la personne A :

```bash
git switch -c tp/m04-a
# Compléter rendus/M04/individuel/A.md et ajouter ses preuves datées.
git add rendus/M04/individuel/A.md rendus/M04/preuves/
git commit -m "M04 : observations et analyse individuelle A"
git push -u origin tp/m04-a
```

B et C utilisent respectivement `tp/m04-b` et `tp/m04-c`, et leur propre fichier. N’ajouter dans `preuves` que ses propres fichiers pour éviter les collisions. Le fichier personnel contient une hypothèse de départ puis une conclusion après l’enquête ; il n’exige pas de saisir de nouveau toutes les données collectées.

## Pull requests

Depuis GitHub, ouvrir une pull request de sa branche vers `main`. Le modèle de description propose observations, limites et recommandation. Le formateur peut discuter les conclusions dans la revue. Ne pas demander de revue à une personne extérieure au groupe sans instruction.

Le rapporteur complète `rendus/M04/SYNTHESE.md` **sur sa branche personnelle du module**, puis commit et push sur cette même branche. Il cite les preuves des autres étudiants par leur branche ou pull request. Aucune fusion n’est nécessaire pour écrire ou présenter la synthèse ; les fichiers vierges des autres participants sur sa branche ne remplacent pas leurs rendus.

Le formateur relit et intègre les contributions ultérieurement. Pour le module suivant, repartir de `main` à jour avec une nouvelle branche personnelle ; ne pas écraser les branches non fusionnées. Rapporteurs : M04 A, M05 B, M06 C, M07 A, M08 B, M09 C, M10 A. Voir [le guide d’autonomie accompagnée](AUTONOMIE_ACCOMPAGNEE.md).

Ne pas utiliser `push --force` pour résoudre un problème courant. En cas de conflit ou de droits insuffisants, conserver ses fichiers localement et demander l’aide du formateur. Si Git bloque pendant le TP, rendre les fichiers au formateur pour intégration ultérieure.
