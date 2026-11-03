# M04 — Deux applications, une dépendance commune

**90 min · Manipulation HTTP locale · Évaluation annoncée avant démarrage : voir [barème](../../docs/EVALUATION.md).** Prérequis : laboratoire installé et vérifié avant la séance, Python 3.10+, navigateur ou client HTTP. [Préparation et limites](../../lab/README.md).

## Mission

Vous devez vérifier l’affirmation de la direction : « Nous avons deux applications sur deux ports différents, donc l’une restera disponible si l’autre rencontre un problème. » Identifiez le périmètre exact dans lequel cette affirmation tient ou échoue.

Le laboratoire représente deux applications et une validation d’identité fictive commune. Il ne réalise pas de véritable fédération SSO et ne reproduit pas le SI d’une entreprise réelle.

## Déroulé

| Temps | Activité |
|---|---|
| 0–10 | Hypothèse individuelle et prédiction de l’effet d’une panne |
| 10–25 | [Notions](NOTIONS.md) : graphe de dépendances et santé locale/de bout en bout |
| 25–40 | État initial, carte et preuves HTTP sur les deux parcours |
| 40–60 | Injection M04, observations, explications concurrentes |
| 60–75 | Comparer les trois diagnostics et envisager une amélioration |
| 75–90 | Démontrer les résultats, compléter le rendu et le retour individuel |

## Travail technique

1. Avant l’injection, vérifier les deux parcours utilisateur, les `/health` et la configuration. Conserver des preuves datées. Une capture de cinq statuts sans URL ne suffit pas.
2. Dessiner les appels de chaque application. Prédire les effets d’une indisponibilité de l’identité principale puis appliquer le fichier d’incident remis au lancement de l’activité selon l’[aide](AIDE.md).
3. Observer les codes, les réponses et `events.jsonl`. Localiser la couche qui échoue et une couche qui continue à répondre. Démontrer la différence entre disponibilité du processus HTTP et service utilisable.
4. Proposer au moins deux améliorations, dont une conserve le composant commun mais réduit son risque. Expliquer les dépendances qu’une amélioration ne supprime pas.
5. Conserver vos preuves avant de revenir à l’état initial pour la séance suivante. Le reset n’est pas une preuve de diagnostic ; il sert ici uniquement à ranger l’environnement après la démonstration.

Les étudiants tournent entre trois fonctions pendant la manipulation : pilote du terminal, observateur des journaux, contradicteur. Chacun garde une prédiction individuelle et une preuve qu’il sait expliquer.

## Sens stratégique

Si deux fournisseurs ou deux régions partagent un service d’identité, dans quel scénario une mesure affectant cet acteur pourrait-elle toucher les deux ? Quelles informations faudrait-il obtenir avant de présenter cette situation comme une restriction réelle ? Une panne locale démontre une dépendance technique, pas une intention d’un pays.

## Livrables

[Rendu M04](../../rendus/M04/SYNTHESE.md) : carte, tableau avant/pendant/après avec HTTP et effet métier, extrait de journal, deux améliorations comparées. La position individuelle de chacun est l’une des pièces de l’évaluation. Ne pas modifier le code du serveur pour faire disparaître un symptôme.
