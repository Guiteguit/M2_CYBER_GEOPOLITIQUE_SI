# M01 — Qui contrôle réellement l’accès à un service numérique ?

**90 minutes · Autonomie complète · Trois étudiants · Formatif.** Commencer par le [guide du bloc autonome](../../docs/DEMARRER_AUTONOMIE.md). Le formateur est absent : toutes les explications nécessaires, les données et les vérifications sont écrites. Un navigateur suffit ; pas de VM, de Python ni de laboratoire à installer.

## Mission et résultat attendu

Asteria, entreprise fictive, veut comprendre les acteurs dont dépend l’accès à un service numérique. Votre cas d’observation est `isc.org` et `www.isc.org`, ressources publiques d’ISC, qui n’appartiennent pas à Asteria. Identifiez les dépendances visibles, leurs preuves et les informations impossibles à établir depuis l’extérieur.

Rendez une carte ou une liste de relations nommées, cinq observations sourcées, trois inconnues et une recommandation de dix lignes. Chacun garde son hypothèse initiale et une observation qu’il sait expliquer. A consigne la synthèse de ce module sur sa branche ; B et C discutent et relisent.

## Chronomètre — 90 minutes

| Minutes | Action sans intervention extérieure |
|---|---|
| 0–8 | Vérifier accès/copie, choisir A/B/C, préparer ses fichiers et noter une hypothèse |
| 8–23 | Lire [NOTIONS.md](NOTIONS.md) ; chacun reformule une distinction importante |
| 23–43 | Enquêter sur DNS, web et messagerie, avec commandes ou fichiers fournis |
| 43–60 | Relier une IP à un réseau et qualifier les acteurs/limites |
| 60–72 | Tour de parole de deux minutes chacun, puis objections croisées |
| 72–83 | Compléter la carte et la synthèse commune |
| 83–90 | [Auto-vérification](AUTO_VERIFICATION.md), retour individuel et enregistrement |

Ne dépassez pas trois minutes sur une panne d’outil : passez aux données fournies. Une inconnue documentée vaut mieux qu’une réponse inventée. À 90 minutes, sauvegardez et passez à M02 sans attendre de correction.

## 1. Avant de lire les notions

Chacun écrit dans son fichier individuel : qui pourrait empêcher l’accès à un site sans posséder son serveur ? Quelle observation aiderait à le vérifier ? Gardez cette première réponse pour pouvoir expliquer ensuite son évolution.

## 2. Le chemin garanti avec les fichiers fournis

Ouvrir le [dossier de collectes](preuves_secours/README.md), puis :

- `isc.org_NS.json` pour la délégation ;
- `isc.org_MX.json` pour la réception du courrier ;
- `isc.org_A.json`, `isc.org_AAAA.json`, `www.isc.org_A.json`, `www.isc.org_AAAA.json` et `www.isc.org_CNAME.json` pour le web ;
- les résolutions des noms NS/MX pour poursuivre une relation déjà observée ;
- `RIPE_web_network-info.json`, puis le fichier RIPE d’ASN fourni dans le dossier pour examiner l’adresse effectivement passée en paramètre.

Dans chaque pièce, relever requête ou URL source, date et champs utiles. Distinguer nom demandé, type demandé et réponses effectivement présentes. Si une section est vide ou absente, expliquez ce que cela permet — et ne permet pas — de conclure.

A commence par NS et délégation ; B par web/IP/ASN ; C par MX et documentation. Chacun réalise une lecture technique, puis vérifie une observation d’un autre. Une capture d’écran n’est pas obligatoire : un extrait cité par fichier et champ suffit.

Si vous disposez déjà d’un terminal fonctionnel, vous pouvez remplacer une partie de ces lectures par des requêtes en direct selon [AIDE.md](AIDE.md). Indiquez alors la date, le résolveur et les éventuelles différences. Limitez-vous aux noms et types du dossier, ou à la résolution des noms retournés ; aucune énumération, aucun scan ni recherche de vulnérabilité n’est demandé.

## 3. Des réponses aux dépendances

Choisir une adresse du web et vérifier que le JSON réseau fourni concerne bien cette adresse. Retrouver le préfixe et l’ASN annonçant, puis l’organisation associée. Une documentation officielle peut compléter l’analyse si Internet fonctionne ; sinon consigner le besoin de confirmation, sans attribuer un rôle au seul nom d’un domaine.

Pour chaque relation, écrire : « cet élément utilise ou s’appuie sur cet autre élément, d’après telle preuve ». Un nom de fournisseur, une IP et un pays de registre ne sont pas interchangeables. Les [notions](NOTIONS.md) et l’[aide](AIDE.md) donnent les distinctions.

## 4. Discussion à trois — douze minutes

Chacun présente une observation, la preuve et une limite pendant deux minutes. Pendant les six minutes suivantes, examinez :

1. Quelle dépendance commune peut-on démontrer, et quelle indépendance reste non prouvée ?
2. Quel changement technique, commercial ou international pourrait affecter un acteur identifié ? Formulez une possibilité conditionnelle, pas une accusation.
3. Quelle preuve Asteria devrait-elle demander avant de décider de conserver ou remplacer ce service ?

Si vous ne tranchez pas un désaccord en cinq minutes, écrivez les deux hypothèses et le test qui les départagerait. Continuez.

## 5. Remise et passage au M02

Compléter [SYNTHESE.md](../../rendus/M01/SYNTHESE.md) : carte, cinq observations, trois inconnues et recommandation. Une liste « départ — relation — arrivée — preuve » remplace une image si le dessin vous ralentit. Chacun complète son fichier individuel A/B/C.

A enregistre la synthèse sur `tp/autonomie-a`, B et C conservent leurs contributions sur leurs branches personnelles. Les trois pull requests restent ouvertes ; aucune fusion n’est nécessaire. Si GitHub bloque, conserver les fichiers localement selon le [guide commun](../../docs/DEMARRER_AUTONOMIE.md).

Terminer l’[auto-vérification](AUTO_VERIFICATION.md), noter un blocage éventuel et ouvrir [M02](../M02/README.md). M01 reste formatif ; le retour avec le formateur aura lieu à partir de M04.
