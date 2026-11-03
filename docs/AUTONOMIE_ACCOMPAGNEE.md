# M04–M08 — Travailler en autonomie avec un formateur en soutien

Vous conduisez l’enquête et les manipulations. Le formateur est présent pour aider, poser des questions, apporter une explication ciblée et vous aider à examiner une décision. Il ne déroule pas la solution à votre place et son accord n’est pas nécessaire à chaque étape.

**M01–M03 restent organisés sans sa présence** selon le [guide dédié](DEMARRER_AUTONOMIE.md). Ce document s’applique à partir de M04. Chaque mission dispose de notions à lire, d’aides progressives, d’un chronomètre et d’une auto-vérification.

## Avant de démarrer

Lire la mission et les critères. Vérifier le laboratoire et disposer du fichier d’incident du module concerné avant son application. La préparation du poste et la remise de ce fichier sont prévues en amont ; le choix des pannes reste dans l’espace formateur. Ne pas ouvrir un ancien incident d’un autre module pour remplacer celui prévu.

Les manipulations restent dans votre laboratoire local et portent sur des données fictives. Si le poste ou un fichier indispensable manque, solliciter immédiatement le formateur pour définir un mode de travail ou le secours. L’autonomie ne consiste pas à perdre la séance sur une installation.

## Votre cycle de travail

1. Écrire une hypothèse individuelle avant la lecture ou les tests.
2. Lire les notions, puis choisir une première observation utile.
3. Prédire l’effet d’un test, l’exécuter et conserver sa preuve.
4. Comparer le résultat à la prédiction, discuter avec les autres et choisir la suite.
5. Vérifier les critères métier et les limites avant de conclure.

Une réponse intermédiaire peut rester incertaine. Documenter l’inconnue et proposer une vérification plutôt qu’attendre que le formateur choisisse votre diagnostic. Les points de décision de chaque mission sont des traces à consigner, pas des demandes d’autorisation.

## Répartition des rôles

| Module | Rapporteur | Point de vigilance |
|---|---|---|
| M04 | A | Distinguer santé locale et usage |
| M05 | B | Vérifier repli, copie et données restaurées |
| M06 | C | Comparer hypothèses, causalité et attribution |
| M07 | A | Relier chaque affirmation à ses preuves |
| M08 | B | Démontrer la reprise et défendre une décision |

Pendant les manipulations, faites tourner pilote, observateur des preuves et contradicteur. Sur trois postes, chacun réalise ses tests puis confronte ses résultats. Sur une instance collective, changer le pilote entre les phases et garder les hypothèses individuelles. Le rapporteur consigne ; il ne fait pas tout le travail.

## Quand demander de l’aide

Commencer par les notions, l’aide du module et une vérification par un camarade. Si vous ne progressez plus après trois à cinq minutes, solliciter le formateur. En cas de risque de perdre une preuve ou de modifier autre chose que le labo, demander immédiatement une aide ; il n’y a aucun délai à respecter pour cela.

Une demande utile présente quatre éléments :

- **But :** ce que vous cherchez à vérifier.
- **Hypothèse :** ce que vous pensez observer et pourquoi.
- **Preuve :** commande, fichier, réponse, erreur et résultat déjà obtenu.
- **Besoin :** une notion, une méthode de test ou une explication d’outil.

Le formateur peut répondre par une question, un indice ou une démonstration ciblée. Après l’aide, vous choisissez ou expliquez le test suivant et vérifiez vous-mêmes son effet. Demander une aide ne conduit pas automatiquement à une pénalité ; indiquez cependant ce que l’aide vous a apporté pour distinguer votre raisonnement personnel.

## Confronter une décision

Avant un changement, écrire : « Nous pensons que… ; ce test devrait montrer… ; nous conserverons… ; nous conclurons seulement si… ». Puis chercher un contre-argument. Un camarade peut défendre l’autre hypothèse ; le formateur peut challenger une déduction ou rappeler une contrainte métier.

L’échange final présente la preuve et sa limite, pas seulement la commande. Le formateur peut demander une justification individuelle et reste responsable du retour pédagogique et de l’évaluation. Une auto-vérification ne remplace pas son appréciation.

## Rendre sans attendre une fusion

À partir de M04, créer une branche personnelle par module (`tp/m04-a`, `tp/m04-b`, `tp/m04-c`, etc.). Chacun complète son fichier individuel et ses preuves. Le rapporteur ajoute la synthèse collective sur **sa branche personnelle du module**, en citant les contributions des autres par lien de branche ou de pull request. Il n’a pas à attendre leur intégration dans `main`.

Ouvrir les pull requests vers `main` et laisser la revue/intégration au formateur. L’activité et le module suivant ne dépendent pas d’une fusion ; une preuve peut être citée depuis la branche qui la contient. Le [guide Git](GIT.md) et [PARTICIPER.md](PARTICIPER.md) donnent les commandes. En cas de blocage Git, conserver les fichiers localement et continuer l’analyse.

## Terminer la séance

Utiliser l’auto-vérification du module, sauvegarder les preuves, enregistrer les fichiers et écrire une hypothèse révisée. Noter toute aide déterminante et les questions restantes. Ne pas utiliser un reset ou une nouvelle application d’incident comme preuve de réparation. Le formateur peut ensuite vous aider à tirer une conclusion ou à préparer le module suivant.
