# Résultats datés de secours — M01

Ces fichiers contiennent de vraies réponses collectées sur des services publics, pas des sorties simulées. Ils constituent des preuves à analyser, pas un corrigé. Les résultats peuvent différer lors d’une nouvelle séance.

## Provenance

Chaque JSON inclut `collected_at_utc`, `source_url`, `method` et `response`. La date de collecte n’est pas nécessairement la date d’observation de la donnée sous-jacente : RIPEstat expose aussi des champs de période. Les requêtes DNS ont été réalisées via l’API HTTPS de Google Public DNS ; elles ne reproduisent pas une requête depuis le réseau de la classe. Les données réseau sont issues des API publiques RIPEstat.

Les fichiers DNS couvrent `isc.org`, `www.isc.org` et les résolutions IPv4 des noms NS/MX effectivement retournés. Les données RIPE couvrent une adresse web IPv4 choisie parmi les résultats, puis l’ASN retourné. Le paramètre exact figure dans chaque URL de provenance. Cela ne constitue pas une cartographie exhaustive des routes ou des adresses.

## Fichiers disponibles

| Fichier brut | Date de collecte UTC |
|---|---|
| [RIPE_AS54113_overview.json](RIPE_AS54113_overview.json) | 2026-11-02T20:15:44.108364+00:00 |
| [RIPE_web_network-info.json](RIPE_web_network-info.json) | 2026-11-02T20:15:39.186893+00:00 |
| [isc.org_A.json](isc.org_A.json) | 2026-11-02T20:12:41.914950+00:00 |
| [isc.org_AAAA.json](isc.org_AAAA.json) | 2026-11-02T20:12:41.922250+00:00 |
| [isc.org_MX.json](isc.org_MX.json) | 2026-11-02T20:12:41.907338+00:00 |
| [isc.org_NS.json](isc.org_NS.json) | 2026-11-02T20:12:41.876300+00:00 |
| [mx.ams1.isc.org_A.json](mx.ams1.isc.org_A.json) | 2026-11-02T20:15:48.763812+00:00 |
| [mx.pao1.isc.org_A.json](mx.pao1.isc.org_A.json) | 2026-11-02T20:15:48.616082+00:00 |
| [ns.isc.afilias-nst.info_A.json](ns.isc.afilias-nst.info_A.json) | 2026-11-02T20:15:48.677608+00:00 |
| [ns1.isc.org_A.json](ns1.isc.org_A.json) | 2026-11-02T20:15:48.706143+00:00 |
| [ns2.isc.org_A.json](ns2.isc.org_A.json) | 2026-11-02T20:15:48.612583+00:00 |
| [ns3.isc.org_A.json](ns3.isc.org_A.json) | 2026-11-02T20:15:53.371541+00:00 |
| [nsp.dnsnode.net_A.json](nsp.dnsnode.net_A.json) | 2026-11-02T20:15:53.194375+00:00 |
| [www.isc.org_A.json](www.isc.org_A.json) | 2026-11-02T20:12:42.009937+00:00 |
| [www.isc.org_AAAA.json](www.isc.org_AAAA.json) | 2026-11-02T20:12:42.025939+00:00 |
| [www.isc.org_CNAME.json](www.isc.org_CNAME.json) | 2026-11-02T20:12:42.012126+00:00 |

## Travailler sans Internet

Lire les réponses DNS, puis la réponse RIPE concernant l’adresse effectivement passée en paramètre. Utiliser les champs `Question`, `Answer`, `Authority`, `Status` et les métadonnées lorsqu’ils sont présents. Ne pas inventer de section absente. Les codes de types utiles ici sont : A = 1, NS = 2, CNAME = 5, MX = 15, AAAA = 28.

Un statut DNS 0 indique que la requête a été traitée sans erreur de code DNS ; une liste de réponses vide ne démontre pas que tous les services associés au nom sont absents. Les champs de registre et d’annonce de réseau ne suffisent pas à localiser l’ensemble du traitement des données.

Pour l’étape documentaire, utiliser les repères de l’[aide](../AIDE.md) et signaler explicitement les affirmations impossibles à corroborer hors ligne. Les URL officielles à examiner plus tard sont dans les [références](../../../docs/OUTILS.md). L’absence d’accès à une documentation devient une limite, pas une confirmation par défaut.
