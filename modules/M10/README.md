# M10 — Prouver la réversibilité d’un fournisseur

> **Autonomie accompagnée · 90 minutes · Python 3.10+ standard.** Le formateur aide et discute vos décisions ; aucun exposé préalable ni service externe n’est nécessaire. Lire [le fonctionnement commun](../../docs/AUTONOMIE_ACCOMPAGNEE.md), les [notions](NOTIONS.md), puis les [aides](AIDE.md). Ces travaux sont formatifs, sans modification du barème M04–M08.

## Mission

Asteria dispose d’un export propriétaire fictif et veut récupérer ses commandes dans une cible exploitable sans l’outil source. Vous devez construire la correspondance de données, exécuter la migration, vérifier le métier et proposer les conditions d’une véritable sortie fournisseur. Ce TP n’utilise ni serveur ni capsule et ne modifie pas le laboratoire M08.

## Déroulé

| Minutes | Travail conduit par les étudiants |
|---|---|
| 0–8 | Définir les critères de sortie et écrire les risques anticipés |
| 8–20 | Lire notions, export et contrat cible ; attribuer les rôles |
| 20–40 | Compléter le mapping et produire un CSV intermédiaire |
| 40–60 | Importer puis contrôler les lignes et le rejet d’un second import |
| 60–75 | Consulter sans la source, préparer retour arrière et limites |
| 75–90 | Auto-vérifier, soutenir la décision de sortie et déposer |

## Manipulations

1. Lire [le contrat cible](donnees/CONTRAT_CIBLE.md), l’[export](donnees/export_source.json) et les [notions](NOTIONS.md). Le référentiel métier fixe les résultats attendus ; il reste intact. Écrire les correspondances de champs et la règle d’inclusion avant d’utiliser l’outil.
2. Créer `lab/runtime/m10/`. Copier l’export en `source.json` et le [mapping à compléter](donnees/mapping_a_completer.json) en `mapping.json` dans ce répertoire. Compléter le mapping dans un éditeur. L’outil applique votre choix : il ne devine ni les champs ni le statut à retenir.
3. Exécuter les commandes de [AIDE.md](AIDE.md) : transformer vers `commandes.csv`, importer dans une **nouvelle** base `cible.sqlite`, puis vérifier contre `reference_metier.csv`. Une erreur exige une explication et une correction de la copie, pas du référentiel.
4. Rejouer le même import : il doit échouer. Vérifier ensuite que la base contient toujours exactement les lignes attendues. En option, créer un CSV avec doublon sur une copie et contrôler le rejet sans import partiel dans une autre base.
5. Renommer **uniquement la copie** `lab/runtime/m10/source.json` en `source_hors_ligne.json`. Relancer `inspect` et `verify` sur la cible : ces commandes ne reçoivent aucun chemin vers l’export. Conserver les sorties. Ne pas renommer les fichiers fournis dans `modules/`.
6. Préparer le retour arrière : source intacte, preuves conservées, nouvelle cible distincte si nouvelle tentative. Aucun effacement n’est requis. Le test prouve une consultation locale de données, sans démontrer identité, interfaces applicatives, nouvelles écritures, performance ou continuité en production.

## Décision de sortie

Présenter un avis **sortie possible / sous conditions / non démontrée**, étayé par les tests. Ajouter trois exigences vérifiables : contrôle des données et accès, indépendance opérationnelle, délai et procédure de sortie. Relier chaque exigence à un acteur qui contrôle encore une ressource. Le contrat fictif n’est pas une analyse juridique réelle.

Compléter le [rendu M10](../../rendus/M10/README.md) et [l’auto-vérification](AUTO_VERIFICATION.md). **Rapporteur A**, synthèse sur `tp/m10-a`. Chaque étudiant défend un contrôle et une limite. La restitution termine le parcours de dix modules ; le barème existant de M04–M08 reste inchangé.
