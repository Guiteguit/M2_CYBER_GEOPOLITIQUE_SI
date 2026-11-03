# Outils et prérequis du parcours

Prévoir un ordinateur par étudiant, un navigateur, un terminal et un éditeur de texte. Git et VS Code sont pratiques pour le rendu. L’enquête peut se faire avec les fichiers JSON de secours si les outils ou le réseau sont indisponibles.

## Trois chemins possibles

| Environnement | Outils possibles | Remarque |
|---|---|---|
| Linux ou WSL déjà disponible | `dig`, navigateur, éventuellement `curl` | Vérifier `dig -v` avant la séance |
| Windows avec PowerShell | `Resolve-DnsName`, navigateur | La syntaxe d’aide figure dans le module |
| Sans outil DNS local ou hors ligne | Fichiers `modules/M01/preuves_secours` | Les requêtes et leur provenance sont enregistrées ; préciser que vous analysez une collecte antérieure |

Pas besoin de Kali, de serveur ou de VM pour M01. Pour les modules M04–M06 et M08, préparer le [laboratoire Python local](../lab/README.md) avant la séance. Si un outil manque, employer un autre chemin plutôt que consacrer le TP à une installation. La consultation de RIPEstat en ligne et des documents officiels complète les résultats DNS lorsque le réseau est disponible.

## Documents de référence

- [Manuel dig — ISC BIND](https://bind9.readthedocs.io/en/latest/manpages.html#dig-dns-lookup-utility).
- [Resolve-DnsName — Microsoft](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname).
- [API DNS JSON — Google Public DNS](https://developers.google.com/speed/public-dns/docs/doh/json).
- [RIPEstat : Network Info](https://stat.ripe.net/docs/data-api/api-endpoints/network-info).
- [RIPEstat](https://stat.ripe.net/).
- [Domaines et origines — documentation Fastly](https://www.fastly.com/documentation/guides/full-site-delivery/domains-and-origins/).
- [Présentation officielle d’ISC](https://www.isc.org/about/).
- [Cloudflare : effet du proxy sur les réponses DNS](https://developers.cloudflare.com/dns/proxy-status/).

Ces liens documentent les outils et les limites d’observation ; ils ne constituent pas des conclusions sur les domaines du TP.


## Références M02–M08

- [RIPE NCC — historique de routage](https://stat.ripe.net/docs/data-api/api-endpoints/routing-history).
- [Python 3.12 — serveurs HTTP](https://docs.python.org/3.12/library/http.server.html).
- [Python — urllib.request](https://docs.python.org/3/library/urllib.request.html).
- [Meta Engineering — détail de la panne du 4 octobre 2021](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/).

Les pièces contractuelles et les publications des dossiers synthétiques sont fictives. Les références ci-dessus documentent les outils ou un incident réel distinct ; elles ne valident pas l’ensemble des affirmations du cas Asteria.
