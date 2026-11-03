# M09 — Auditer une chaîne d’approvisionnement logicielle

> **Autonomie accompagnée · 90 minutes · Python 3.10+ standard.** Le formateur aide et discute vos décisions ; aucun exposé préalable ni service externe n’est nécessaire. Lire [le fonctionnement commun](../../docs/AUTONOMIE_ACCOMPAGNEE.md), les [notions](NOTIONS.md), puis les [aides](AIDE.md). Ces travaux sont formatifs, sans modification du barème M04–M08.

## Mission

Après la reprise de M08, Asteria veut réduire les dépendances logicielles qui menacent ses deux services. Vous recevez un inventaire, des avis de sécurité et des déclarations d’exploitation **entièrement fictifs**. Choisissez deux actions pour la prochaine fenêtre, avec tests et risques résiduels. Ce module peut démarrer même si votre réparation M08 est incomplète.

## Déroulé

| Minutes | Travail conduit par les étudiants |
|---|---|
| 0–8 | Lire la mission et écrire une priorité individuelle provisoire |
| 8–20 | Lire notions et dossier ; répartir les rôles |
| 20–40 | Auditer l’inventaire et reconstruire les chemins transitifs |
| 40–60 | Tester un lot de versions sur une copie, comparer et examiner la compatibilité |
| 60–78 | Confronter les priorités, tester le scénario de forge indisponible |
| 78–90 | Auto-vérifier, défendre deux actions et déposer les preuves |

## Investigation technique

1. Lire [SCENARIO.md](donnees/SCENARIO.md), `inventaire.json`, `avis.json` et `exploitation.json` dans [donnees](donnees/). Distinguer composant direct, transitif, mainteneur et point de distribution. Chaque étudiant prédit quel service peut être concerné par chaque avis.
2. Exécuter l’auditeur depuis la racine et conserver sa sortie :

```bash
python3 scripts/auditer_dependances.py --inventory modules/M09/donnees/inventaire.json --advisories modules/M09/donnees/avis.json
```

Le code de sortie 0 indique une lecture réussie, **pas** l’absence de risque. Reconstituer un chemin complet par service ; confronter les correspondances de versions aux conditions d’exploitation.
3. Créer `lab/runtime/m09/`, y copier l’inventaire sous `inventaire_candidat.json` et modifier uniquement cette copie avec un éditeur. Choisir un lot de versions dans celles déclarées disponibles. Relancer l’auditeur en lui donnant le chemin candidat. Conserver avant/après et diff. Ne pas modifier les avis pour supprimer une alerte.
4. Vérifier séparément les contraintes de compatibilité dans `exploitation.json`. Une sortie sans correspondance peut encore décrire un lot incompatible. L’inventaire n’installe rien : le test est une comparaison statique, pas un test d’exécution de bibliothèques.
5. Décrire l’effet d’une indisponibilité de Forge-Nord : déploiement actuel, nouvelle installation, correctif et reconstruction. Proposer les preuves nécessaires pour revendiquer une reconstruction indépendante.

## Points de décision et rendu

Choisir deux actions : pourquoi celles-ci avant les autres, quelles conditions, quels tests d’acceptation et quel retour arrière ? Contester au moins une priorité avec une pièce du dossier. La sévérité d’un avis n’est pas une preuve suffisante d’exploitabilité.

Compléter le [rendu M09](../../rendus/M09/README.md), puis [l’auto-vérification](AUTO_VERIFICATION.md). **Rapporteur C**, synthèse sur sa branche `tp/m09-c` ; A et B gardent leur propre branche et leurs contributions. Conserver les aides reçues et les inconnues. Le formateur peut aider à choisir un test, puis chacun défend sa décision.
