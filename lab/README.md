# Laboratoire Asteria — M04, M05, M06 et M08

## Prérequis et limites

Python **3.10 ou plus récent**, bibliothèque standard uniquement. Linux, macOS ou Windows avec Python installé ; les essais d’exécution fournis pour cette version ont été réalisés sous Linux/Python 3.12. Les commandes ci-dessous partent de la racine du dépôt. Sous Windows, remplacer `python3` par `py -3` si nécessaire.

Un ordinateur par étudiant suffit ; pas de droits administrateur, Docker, VM ou installation par `pip`. Environ 256 Mo de mémoire et 50 Mo de disque libres constituent une marge pour ce petit exercice, pas un dimensionnement de production. Les ports TCP 18180–18184 doivent être libres.

Tous les serveurs écoutent uniquement sur **127.0.0.1**. Les applications, les identités et les commandes commerciales sont fictives. Ce modèle réalise de vrais appels HTTP locaux, mais la validation d’identité est un contrôle de disponibilité simulé : pas d’OIDC, de Kerberos, de mot de passe ou de sécurité SSO de production. Il ne réalise pas de routage BGP ni de requêtes DNS : M02 et M01 traitent ces protocoles séparément.

## Démarrer avant la séance

```bash
python3 scripts/preflight.py
python3 lab/asteria_lab.py init
python3 lab/asteria_lab.py start
```

Garder ce terminal ouvert. Dans un deuxième terminal, à la racine du même dépôt :

```bash
python3 lab/asteria_lab.py status
```

Ouvrir `http://127.0.0.1:18180/portail` et `http://127.0.0.1:18180/commandes`. Au départ, les deux retournent HTTP 200 ; l’application commandes contient trois lignes, quantité totale neuf. Le statut de contrôle rend le code de sortie 2 si un des deux parcours HTTP échoue ; il ne valide pas l’exactitude métier des données.

## Composants

| Rôle | Port | Fonction et parcours |
|---|---:|---|
| edge | 18180 | Point d’entrée `/portail`, `/commandes`, `/commandes/export` |
| portail | 18181 | Application `/`, dépend de l’identité |
| commandes | 18182 | Application `/` et export `/export`, dépend de l’identité et du CSV |
| idp | 18183 | Validation fictive `/validate` |
| idp_backup | 18184 | Deuxième validation fictive `/validate`, pas utilisée initialement |

Chaque composant expose `/health`, qui teste son propre état local et **ne teste pas toutes ses dépendances**. La réponse des applications indique le port d’identité utilisé. Le repli est séquentiel à chaque nouvelle requête ; il n’y a pas de session persistante à vider.

## État de travail

`lab/runtime/config.json` est relu à chaque requête ; les modifications valides prennent effet sans redémarrer. Il contient :

- `base_port` : port de départ, à ne pas modifier pendant l’exécution ;
- `disabled` : liste de rôles qui renvoient HTTP 503 pour simuler une indisponibilité applicative ;
- `routes` : ports des applications visées par edge ;
- `auth_ports` : liste ordonnée des ports d’identité consultés par chaque application.

Les commandes sont dans `lab/runtime/commandes.csv`. Le journal append-only de l’exercice est `lab/runtime/events.jsonl` ; il n’est pas cryptographiquement protégé. Ses horodatages sont ceux de votre machine. Une configuration invalide provoque une erreur explicite ; conserver une copie avant de l’éditer.

## Commandes de contrôle

```bash
# Injecteurs : chacun remet d’abord configuration et commandes à l’état initial.
# Ils ne suppriment pas les journaux existants.
python3 lab/asteria_lab.py scenario M04
python3 lab/asteria_lab.py scenario M06
python3 lab/asteria_lab.py scenario M08 --seed 27

# Export par le parcours HTTP réel du laboratoire, avec manifeste d’intégrité.
python3 lab/asteria_lab.py export --to lab/runtime/sauvegardes/mon_export.csv

# Remplace les commandes du laboratoire après contrôle du format et,
# lorsqu’il existe, du manifeste adjacent .csv.meta.json.
python3 lab/asteria_lab.py restore --from lab/runtime/sauvegardes/mon_export.csv --confirm

# Réinitialisation de démonstration : réservée au début/à la fin d’un exercice.
# Elle réécrit configuration et commandes, conserve journaux et sauvegardes.
python3 lab/asteria_lab.py reset --confirm
```

Le scénario M08 prépare une copie `lab/runtime/sauvegardes/preincident.csv` et son manifeste avant l’incident. C’est une sauvegarde initiale de simulation fournie par l’injecteur, pas la preuve d’un export précédemment réalisé par l’étudiant. Une graine identique reproduit la même famille de panne. Les mécanismes restent inspectables dans le code : il s’agit d’une évaluation de diagnostic et de preuve, pas d’un secret anti-triche.

Les chemins des options `--to` et `--from` sont des fichiers locaux. Éviter de sauvegarder sur le fichier de données courant. Exporter et restaurer ne répare ni une route ni l’accès à l’identité.

## Arrêter ou changer les ports

Ctrl+C dans le terminal serveur arrête les cinq composants. Si un port est occupé, arrêter le labo et utiliser un nouveau répertoire d’état :

```bash
python3 lab/asteria_lab.py --state-dir lab/runtime-bis init --base-port 19180
python3 lab/asteria_lab.py --state-dir lab/runtime-bis start
```

Adapter ensuite les URL et ajouter `--state-dir lab/runtime-bis` **avant** les sous-commandes `status`, `scenario`, `export` et `restore`. Les scénarios calculent leurs ports depuis ce port de base ; un éventuel port de panne `base + 9` doit aussi être libre pour conserver un refus de connexion reproductible.

## Ce que le TP ne démontre pas

Deux services d’identité sur le même ordinateur restent dépendants du même hôte, de son système et de son alimentation. Une copie sur le même disque n’est pas une sauvegarde indépendante. Les temps mesurés en classe décrivent votre essai, pas un SLA, un RTO ou un RPO garantis en production. Le laboratoire permet de tester une dépendance logique et de discuter les limites restantes.
