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

## Appliquer l’état d’un exercice

Pour les activités avec incident, placer le JSON remis dans un dossier local `incidents/`, puis l’appliquer une seule fois au lancement de l’activité :

```bash
python3 lab/asteria_lab.py incident --from incidents/m04.json --confirm
```

Adapter le nom du fichier au module concerné. L’import valide le format et le port de base, puis remplace les données et la configuration fictives de travail ; les journaux existants restent conservés. Il ne lance aucun code reçu et n’accepte pas de chemin de sortie dans la capsule. Une capsule peut fournir une copie préincident sous `lab/runtime/sauvegardes/preincident.csv`, avec manifeste. Cette copie est fournie pour l’exercice, pas un export que vous auriez déjà démontré.

Ne pas réappliquer le fichier après une correction pour faire disparaître une panne. Le choix des scénarios n’est pas dans ce dépôt.

## Exporter, restaurer et réinitialiser

```bash
python3 lab/asteria_lab.py export --to lab/runtime/sauvegardes/mon_export.csv
python3 lab/asteria_lab.py restore --from lab/runtime/sauvegardes/mon_export.csv --confirm
python3 lab/asteria_lab.py reset --confirm
```

Le reset réécrit configuration et commandes, conserve journaux et sauvegardes et sert uniquement à préparer ou ranger une démonstration. Il ne remplace pas une restauration depuis votre export. Les options `--to` et `--from` désignent des fichiers locaux. Éviter d’exporter sur le fichier de données courant. Une restauration ne répare ni une route ni l’accès à l’identité.

## Arrêter ou changer les ports

Ctrl+C dans le terminal serveur arrête les cinq composants. Si un port est occupé, arrêter le labo et utiliser un nouveau répertoire d’état :

```bash
python3 lab/asteria_lab.py --state-dir lab/runtime-bis init --base-port 19180
python3 lab/asteria_lab.py --state-dir lab/runtime-bis start
```

Adapter ensuite les URL et ajouter `--state-dir lab/runtime-bis` **avant** les sous-commandes `status`, `incident`, `export` et `restore`. Demander une capsule préparée pour cette même base de ports. Le prévol examine aussi le port de réserve `base + 9` pour les exercices.

## Ce que le TP ne démontre pas

Deux services d’identité sur le même ordinateur restent dépendants du même hôte, de son système et de son alimentation. Une copie sur le même disque n’est pas une sauvegarde indépendante. Les temps mesurés en classe décrivent votre essai, pas un SLA, un RTO ou un RPO garantis en production. Le laboratoire permet de tester une dépendance logique et de discuter les limites restantes.
