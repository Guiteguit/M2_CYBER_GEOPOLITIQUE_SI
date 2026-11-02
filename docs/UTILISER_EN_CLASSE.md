# Travailler avec ce dépôt — guide de classe

Ce dépôt privé contient les supports étudiants et les rendus du groupe. Les corrections, notes confidentielles et scénarios commentés du formateur restent dans un autre espace. Tous les collaborateurs du dépôt peuvent lire ses fichiers et son historique : un dossier ou une branche nommés « formateur » n’assurent aucune confidentialité.

## 1. Avant la première séance — formateur

1. Recueillir les identifiants GitHub exacts des trois étudiants. Dans le dépôt : **Settings → Collaborators → Add people** (les libellés peuvent varier selon l’interface). Inviter les trois comptes et leur faire accepter l’invitation. Ne pas rendre le dépôt public pour contourner un problème d’accès.
2. Associer A, B et C à ces trois personnes pour toute la durée du cours. Garder les notes nominatives ailleurs ; les fichiers de contribution utilisent seulement ces lettres.
3. Leur faire ouvrir la page du dépôt avec leur propre compte. Vérifier qu’ils peuvent cloner et pousser une branche de test contenant un fichier de démonstration, puis retirer cette branche de test après intégration ou abandon.
4. Faire vérifier Python 3.10+, l’éditeur, le terminal et Git. Pour M01–M03 et M07, les fichiers locaux et un tableur peuvent suffire ; pour M04–M06 et M08, tester [le labo](../lab/README.md) avant le temps de TP.
5. Annoncer le [barème](EVALUATION.md) au plus tard avant M04 et confirmer son adéquation aux règles de l’école.

Un dépôt personnel comporte des droits de collaborateur permettant de contribuer ; la règle « seul le formateur intègre sur main » est une convention tant qu’une protection de branche ne l’impose pas. Si l’offre du compte permet les protections nécessaires, les configurer séparément avant le cours. Ce dépôt n’a pas reçu de modification de permissions ou de protections automatique lors de sa préparation.

Référence : [GitHub — inviter des collaborateurs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository).

## 2. Organisation conseillée pour trois étudiants

- Un clone par étudiant ; chacun exécute son laboratoire sur sa propre machine.
- Une branche par contribution : `tp/m02-a`, `tp/m02-b`, `tp/m02-c`, puis même principe aux modules suivants.
- Un fichier personnel A/B/C par module pour les hypothèses initiales, une preuve et la révision finale.
- Une branche de synthèse `tp/m02-synthese` tenue par un rapporteur, après intégration des contributions utiles.
- Des preuves nommées avec participant, date et objet, dans le dossier du module. Éviter trois personnes éditant le même fichier pendant une séance.

Rotation du rapporteur : A pour M01/M04/M07, B pour M02/M05/M08, C pour M03/M06. Pendant un test collectif, faire tourner pilote, observateur et contradicteur ; la fonction de rapporteur ne dispense pas d’un test individuel.

M08 peut aussi être réalisé sur une instance collective, si le formateur l’annonce au départ et observe les contributions de chacun. L’objectif est une évaluation individuelle de raisonnement, même avec un livrable commun.

## 3. Début de chaque module — étudiants

```bash
git switch main
git pull --ff-only
git switch -c tp/m02-a
```

Adapter `m02` et la lettre. Si la branche existe déjà, utiliser `git switch tp/m02-a` et vérifier son état plutôt que recréer son nom. Avant de changer de branche, conserver ou committer son travail en cours ; ne pas supprimer des fichiers pour faire disparaître une erreur Git.

Ouvrir `modules/M02/README.md`, prendre connaissance des livrables, puis écrire ses hypothèses. L’aide se consulte au besoin. Les commandes techniques sont exécutées depuis la racine du dépôt, pas depuis le dossier du module.

## 4. Pendant l’enquête

Le formateur demande : « Quelle preuve ? », « Quelle limite ? », « Quelle autre explication ? », « Quelle décision cela change ? ». Les étudiants distinguent leurs mesures, les captures publiques datées et les jeux synthétiques.

Copier uniquement les preuves choisies depuis le laboratoire vers `rendus/Mxx/preuves/`. Le répertoire `lab/runtime` reste hors de Git : il contient l’état local, les injections, les journaux et les exports de travail. Pas de mot de passe, jeton ou données d’entreprise dans les rendus.

Les modules constituent douze heures effectives hors pauses. La configuration de Git et du laboratoire doit être faite avant les séquences ; sinon prévoir un créneau supplémentaire ou le mode secours annoncé, sans prétendre avoir exécuté une manipulation non réalisée.

## 5. Remettre et discuter une contribution

Exemple pour A au M02 :

```bash
git add rendus/M02/individuel/A.md
# Ajouter explicitement les fichiers de preuve que vous avez créés.
git commit -m "M02 A : observations et hypothèses"
git push -u origin tp/m02-a
```

Sur GitHub, ouvrir une pull request vers `main` et compléter le modèle. Inclure module, preuves, conclusion et limites. Le formateur lit l’onglet des différences et laisse un retour ciblé. A corrige dans la même branche, committe et pousse ; la pull request se met à jour. Aucun nouveau dépôt ni fork n’est nécessaire pour ce groupe.

Une pull request individuelle peut rester courte : quelques lignes et une preuve bien interprétée suffisent. Les preuves collectives peuvent être déposées une seule fois et citées par tous.

## 6. Faire la synthèse

Le formateur intègre les contributions après discussion. Le rapporteur repart de `main` à jour, crée `tp/m02-synthese`, puis complète `rendus/M02/SYNTHESE.md` avec les autres. Ouvrir la pull request collective pour la restitution.

Si les contributions ne sont pas encore intégrées, rédiger temporairement la synthèse dans un document commun, puis la déposer après la séance. Les 90 minutes comprennent la restitution pédagogique, pas une longue attente de fusion Git.

Le formateur vérifie preuves, cohérence et participation, puis intègre. Un historique de commits ne mesure pas à lui seul le travail intellectuel : s’appuyer aussi sur les hypothèses et les réponses à l’oral.

## 7. Fin de séance

- Conserver la synthèse et le retour individuel.
- Arrêter les serveurs par Ctrl+C ; sauvegarder les preuves avant tout reset.
- Noter les inconnues utiles pour la séance suivante.
- Le formateur conserve séparément sa grille nominative et son feedback confidentiel.

L’ensemble des modules étudiants est visible dès leur présence dans ce dépôt. Ce n’est pas un mécanisme de publication progressive ni un coffre pour une surprise d’examen.

## 8. Si Git ou le réseau bloque

Conserver les fichiers localement et remettre le dossier au formateur. L’analyse peut continuer à partir des ressources du module. Le formateur peut déposer les fichiers en indiquant clairement leur auteur ; ne pas attribuer au déposant tout le raisonnement des autres.

Si un étudiant n’a pas d’accès GitHub, il peut travailler sur une copie fournie par le formateur en attendant la résolution de l’accès. Pour le labo, un serveur déjà lancé par un autre étudiant n’est pas accessible via son propre `127.0.0.1` : utiliser une instance locale ou travailler à deux sur la même machine.

## 9. Ce qu’il reste à faire manuellement

Inviter les trois comptes, attribuer A/B/C, valider le barème avec l’école, choisir les graines de M08 et effectuer le prévol sur les postes. Aucun étudiant n’a été invité et aucune identité n’a été devinée lors de la construction du cours.
