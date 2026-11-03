# M04 — Deux applications, une dépendance commune

> **Autonomie accompagnée :** vous conduisez ce module à partir des supports. Le formateur est présent en soutien, pour une aide ciblée et pour challenger vos décisions ; aucun exposé oral n’est nécessaire pour commencer. Lire [le fonctionnement commun](../../docs/AUTONOMIE_ACCOMPAGNEE.md). Les apports sont dans [NOTIONS.md](NOTIONS.md), les aides dans [AIDE.md](AIDE.md), puis utiliser [AUTO_VERIFICATION.md](AUTO_VERIFICATION.md).

**90 min · Manipulation HTTP locale · Évaluation annoncée avant démarrage : voir [barème](../../docs/EVALUATION.md).** Prérequis : laboratoire installé et vérifié avant la séance, Python 3.10+, navigateur ou client HTTP. [Préparation et limites](../../lab/README.md).

## Mission

Vous devez vérifier l’affirmation de la direction : « Nous avons deux applications sur deux ports différents, donc l’une restera disponible si l’autre rencontre un problème. » Identifiez le périmètre exact dans lequel cette affirmation tient ou échoue.

Le laboratoire représente deux applications et une validation d’identité fictive commune. Il ne réalise pas de véritable fédération SSO et ne reproduit pas le SI d’une entreprise réelle.

## Déroulé

| Minutes | Travail conduit par les étudiants |
|---|---|
| 0–8 | Lire la mission, écrire une prédiction et répartir les rôles |
| 8–20 | Lire les notions et reformuler la différence santé/usage |
| 20–40 | Mesurer l’état initial et construire la carte |
| 40–60 | Appliquer l’incident, tester et comparer les hypothèses |
| 60–75 | Confronter les preuves et deux améliorations |
| 75–90 | Présenter, auto-vérifier et enregistrer les rendus |

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

## Points de décision à consigner

- Avant l’incident : quelle dépendance commune prévoyez-vous de tester, et quels résultats l’infirmeraient ?
- Après les observations : quelle couche fonctionne encore, quelle couche échoue et quelle preuve les distingue ?
- Avant de recommander : quelle amélioration traite le scénario observé et quelle dépendance laisse-t-elle en place ?

Ces traces ne sont pas des demandes d’autorisation. Après une aide ou une objection, expliquez vous-mêmes la décision retenue et testez-la. À la fin, le rapporteur consigne la synthèse sur sa branche personnelle du module, sans attendre une fusion ; chacun garde son fichier individuel.
