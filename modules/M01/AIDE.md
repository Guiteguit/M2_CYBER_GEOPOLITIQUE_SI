# M01 — Aides facultatives

Ces exemples servent à débloquer une recherche. Ils ne remplacent ni le choix des observations ni leur interprétation.

## DNS avec dig

```bash
dig isc.org NS
dig isc.org MX
dig isc.org A
dig isc.org AAAA
dig www.isc.org CNAME
dig www.isc.org A
dig www.isc.org AAAA
```

Pour conserver le contexte, garder la commande, le résolveur, la date, le statut et les sections utiles. `+short` donne une vue compacte mais supprime des informations utiles à une analyse de réponse vide. Un type interrogé et les types présents dans la réponse peuvent différer lorsqu’une chaîne de noms intervient.

## DNS avec PowerShell

```powershell
Resolve-DnsName -Name isc.org -Type NS -DnsOnly
Resolve-DnsName -Name isc.org -Type MX -DnsOnly
Resolve-DnsName -Name isc.org -Type A -DnsOnly
Resolve-DnsName -Name isc.org -Type AAAA -DnsOnly
Resolve-DnsName -Name www.isc.org -Type CNAME -DnsOnly
```

Adapter le type et le nom aux observations nécessaires. Les messages et la présentation diffèrent selon l’outil ; conservez l’erreur éventuelle plutôt que la traduire automatiquement en absence de service.

## RIPEstat

Ouvrir [RIPEstat](https://stat.ripe.net/) avec une IP observée. Chercher le préfixe, le ou les ASN annonçants et l’organisation associée. Les fichiers de secours peuvent fournir un exemple daté pour la même adresse.

Exemple d’API sur une adresse illustrative, sans rapport imposé avec le domaine du TP :

```bash
curl 'https://stat.ripe.net/data/network-info/data.json?resource=1.1.1.1'
```

Remplacer la valeur par une adresse réellement observée pour produire une preuve du TP. Ne pas présenter la réponse de l’exemple comme une observation du domaine étudié. L’ASN d’origine décrit une annonce de préfixe observée ; il ne constitue pas le chemin complet jusqu’au service ni une preuve de son emplacement physique.

## Si l’information est ambiguë

- Vérifier le nom, le type demandé, le statut et la date.
- Distinguer ce qu’indique un registre, un résolveur et une déclaration du fournisseur.
- Chercher une autre explication compatible avec la même observation.
- Formuler une question précise au fournisseur si la recherche externe ne suffit pas.

Un MX indique une destination pour la réception du courrier du domaine. Il ne décrit pas à lui seul l’emplacement de toutes les boîtes ni tous les flux sortants. Un DNS faisant autorité n’est pas le même rôle que le résolveur interrogé. Une IP de proxy ne doit pas être assimilée sans preuve à celle du serveur d’origine.

Références : [outils et documentation officielle](../../docs/OUTILS.md).
