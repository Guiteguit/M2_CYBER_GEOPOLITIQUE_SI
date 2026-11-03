# M01–M03 — Commencer les trois modules en autonomie

**À lire en premier.** Vous êtes trois, le formateur est absent pendant ces trois modules. Vous disposez de **3 × 90 minutes**, soit 4 h 30 de travail effectif, hors pauses prévues par l’établissement. Vous n’avez pas à attendre une réponse, un cours oral, une autorisation de passer au module suivant ou une fusion GitHub.

## 1. Le parcours minimum est accessible sans installation

Un navigateur avec accès au dépôt suffit pour lire les fichiers et rendre le travail. Les données DNS et RIPE déjà collectées, les CSV et les offres JSON sont fournis. Les recherches en direct et les scripts Python sont des options si les outils fonctionnent déjà ; n’installez ni VM ni laboratoire pour M01–M03.

Si le réseau peut être indisponible, une copie du dépôt doit avoir été téléchargée avant le départ. Les fichiers Markdown/JSON/CSV restent lisibles dans un éditeur de texte ou un tableur. Si l’accès GitHub bloque, travaillez sur cette copie et conservez vos fichiers pour une remise ultérieure. Il n’est pas possible de télécharger les supports sans connexion : vérifier l’accès ou la copie avant de commencer.

Les pièces indiquent leur nature : collecte réelle datée ou jeu entièrement simulé. Ne présentez pas une analyse de fichier comme une commande exécutée en direct.

## 2. Choisissez A, B et C une seule fois

Si les lettres ne sont pas déjà attribuées, choisissez-les entre vous et conservez-les sur les trois modules. Chaque personne tient ses fichiers individuels. Le rapporteur consigne la synthèse du groupe ; il ne fait pas seul l’analyse.

| Module | Rapporteur et gardien du temps | Organisation de départ |
|---|---|---|
| M01 | A | A : DNS ; B : web/IP/ASN ; C : messagerie et documentation |
| M02 | B | A : mesures applicatives ; B : collecte RIPE ; C : observations de routes |
| M03 | C | A : contrats et coûts ; B : offre B ; C : offre A |

Chacun présente ensuite une observation ; un autre doit en discuter une limite. Si vous travaillez à distance sans échange vocal, rédigez ces observations et objections dans vos fichiers ou dans les commentaires de vos pull requests, selon le canal habituel de la classe. Tous contribuent aux calculs et à la décision. Un désaccord peut rester écrit si les preuves ne permettent pas de trancher.

## 3. Une branche personnelle pour tout le bloc

**Exception au fonctionnement habituel des modules suivants :** A utilise `tp/autonomie-a`, B `tp/autonomie-b`, C `tp/autonomie-c`. Chaque branche part de `main` au début de M01 et reste utilisée jusqu’à la fin de M03. Ne changez pas de branche à chaque module et ne fusionnez rien dans `main` pendant l’absence.

Sur sa branche, chacun complète ses trois fichiers individuels. Le rapporteur ajoute aussi la synthèse de son module sur **sa propre branche** :

- A : `rendus/M01/SYNTHESE.md` ;
- B : `rendus/M02/SYNTHESE.md` ;
- C : `rendus/M03/SYNTHESE.md`, puis `rendus/M03/BILAN_AUTONOMIE.md`.

Ainsi, vous n’avez jamais à attendre l’intégration d’une autre branche. Les fichiers de vos camarades visibles dans votre branche peuvent rester vierges : consultez leurs contributions sur leur branche ou leur pull request. Une preuve présente sur une autre branche se cite par son URL GitHub, en précisant la branche et, si possible, le commit. En remise locale, indiquez le nom du fichier joint.

## 4. Depuis le navigateur GitHub

1. Sur la page du dépôt, ouvrez le sélecteur de branche affichant `main`, saisissez votre nom de branche personnel et créez-la depuis `main`. Si elle existe déjà, sélectionnez-la.
2. Vérifiez le nom de branche avant chaque modification. Ouvrez votre fichier individuel, utilisez l’édition du fichier, complétez-le, puis enregistrez avec **Commit changes** sur cette branche. Ne choisissez pas `main` et ne créez pas une nouvelle branche à chaque fichier.
3. Le rapporteur fait de même pour sa synthèse. Une preuve peut être un extrait texte dans le rendu, accompagné de sa requête/source, date et limite ; aucune capture d’écran ou téléversement n’est obligatoire.
4. Après votre premier enregistrement, ouvrez une pull request de votre branche vers `main`, intitulée `Autonomie M01–M03 — A` (ou B/C). Vous la compléterez pendant le bloc ; inutile d’en créer neuf.
5. Laissez vos trois pull requests ouvertes. Le retour et les fusions auront lieu avec le formateur à partir de M04. Aucune approbation n’est nécessaire pour continuer à enregistrer sur votre branche.

Les libellés peuvent varier. Aides officielles : [éditer un fichier](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files), [gérer les branches](https://docs.github.com/en/pull-requests/how-tos/commit-changes/managing-branches-within-your-repository). Si les droits ne permettent pas ces opérations, passez à la remise locale après trois minutes de tentative.

## 5. Si vous utilisez déjà VS Code et Git

Au début du bloc, pour A :

```bash
git switch main
git pull --ff-only
git switch -c tp/autonomie-a
```

Après votre travail, ajouter explicitement vos fichiers, committer puis pousser :

```bash
git add rendus/M01/individuel/A.md rendus/M01/SYNTHESE.md
git commit -m "Autonomie A : travail M01"
git push -u origin tp/autonomie-a
```

Adapter les fichiers aux modules et à votre lettre ; ne pas ajouter la synthèse d’un module dont vous n’êtes pas rapporteur. Aux modules suivants, rester sur cette branche. Ne pas utiliser `push --force`, réinitialiser le travail d’un autre ou mélanger des modifications web et locales sans synchronisation. Si Git bloque, conserver les fichiers et poursuivre hors Git.

## 6. Déroulement de chaque module

Ouvrir sa mission, lancer un minuteur, écrire une hypothèse individuelle, lire les notions, investiguer, confronter les résultats puis rendre la synthèse. Les dernières minutes servent à l’auto-vérification et à l’enregistrement, pas à attendre une correction.

Le chemin est : [M01](../modules/M01/README.md) → [M02](../modules/M02/README.md) → [M03](../modules/M03/README.md). Les notions et données nécessaires sont rappelées à chaque étape ; un résultat incertain au module précédent n’interdit pas de continuer.

## 7. Règle anti-blocage

- Après **trois minutes** sur un outil, un site ou Git qui ne fonctionne pas, utiliser les fichiers fournis ou un document local.
- Si une notion manque, lire la section correspondante puis l’aide progressive du module.
- Après **cinq minutes** de désaccord sans preuve nouvelle, écrire les deux positions et la vérification qui les départagerait. Continuer.
- Quand le temps du module se termine, enregistrer le travail, même incomplet. Noter précisément le blocage ; ne pas décaler tout le bloc pour chercher une certitude impossible.

Dans votre synthèse, ajouter une ligne « blocage — tentative — solution de repli — question restante ». Aucun contact avec le formateur n’est nécessaire pour passer à l’étape suivante. Les modalités de remise en cas de réseau indisponible sont celles prévues par l’établissement ; conserver dans tous les cas vos fichiers localement.

## 8. Fin de M03

Chacun possède une trace individuelle pour M01, M02 et M03. A, B et C ont respectivement la synthèse M01, M02 et M03. C consigne le bilan collectif. Vérifiez que les fichiers sont enregistrés sur la bonne branche ou conservés dans un dossier local.

Ces trois modules restent **formatifs**. L’auto-vérification contrôle vos preuves et votre raisonnement ; elle ne vaut pas validation scientifique du diagnostic. Les questions non résolues serviront à la reprise au M04. N’entamez pas les manipulations M04 avant cette reprise.
