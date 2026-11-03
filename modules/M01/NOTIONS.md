# M01 — Lire les dépendances numériques sans confondre les couches

**Lecture autonome : environ 15 minutes.** Votre objectif n’est pas de mémoriser une liste d’outils : vous devez pouvoir expliquer ce qu’une observation démontre et ce qu’elle laisse inconnu.

## 1. Nom, service et adresse

Un domaine organise des noms. Un service web ou de messagerie utilise certains de ces noms et peut dépendre de plusieurs acteurs. Une adresse IP désigne une destination réseau visible ; elle ne décrit pas toute l’architecture du service.

Le même service peut avoir plusieurs adresses et une adresse peut servir plusieurs noms. Ne concluez donc ni « plusieurs serveurs indépendants » à partir de plusieurs IP, ni « toutes les données sont ici » à partir d’une seule réponse.

## 2. Qui répond à quelle question DNS ?

Votre ordinateur interroge généralement un **résolveur récursif**, qui obtient ou conserve les réponses. Les **serveurs faisant autorité** publient les données d’une zone. L’outil qui vous répond et l’acteur qui publie la zone n’ont pas nécessairement le même rôle.

| Type | Ce que vous cherchez | Limite essentielle |
|---|---|---|
| NS | Serveurs annoncés comme autoritaires | Des noms différents ne prouvent pas une indépendance physique |
| MX | Noms de destinations de réception du courrier et préférences | Ne localise pas toutes les boîtes ni tous les flux sortants |
| A | Adresse IPv4 associée au nom dans la réponse | Peut être une adresse de proxy ou de CDN |
| AAAA | Adresse IPv6 associée au nom dans la réponse | Même limite ; comparer le même nom et la même date |
| CNAME | Relation d’alias d’un nom vers un autre | L’absence d’alias n’implique pas l’absence du service |

Un MX contient une préférence numérique puis un nom. Pour trouver l’adresse de ce nom, une recherche supplémentaire peut être nécessaire. Ne remplacez pas cette étape par une déduction fondée uniquement sur les lettres du nom.

## 3. Lire une réponse et une collecte

Une preuve exploitable précise le nom demandé, le type, le résultat, la source ou le résolveur et la date. La durée TTL indique combien de temps une information peut être conservée en cache selon les conditions DNS ; ce n’est pas une garantie de disponibilité.

Dans les JSON fournis, `Question` décrit la demande, `Answer` les réponses si présentes, `Status` le code DNS et l’enveloppe `collected_at_utc` la collecte. Les codes de types sont notamment A=1, NS=2, CNAME=5, MX=15, AAAA=28. Une section peut être absente. `Status: 0` sans réponse pour le type demandé ne signifie pas « aucun service n’existe ». Une erreur d’outil ou un délai dépassé doit être conservé comme tel, sans inventer de réponse.

La date de votre analyse et celle de la collecte peuvent différer. Si vous utilisez les fichiers fournis, vous analysez une observation antérieure ; vous n’avez pas exécuté une nouvelle requête.

## 4. De l’adresse au réseau

Un préfixe décrit un bloc d’adresses. Un **ASN** identifie un système autonome dans le routage inter-domaines. Une observation de routage permet de relier une adresse à un préfixe et à un ASN annonçant, selon son point d’observation et sa période.

L’organisation associée à un ASN peut être un opérateur ou un fournisseur qui distribue le contenu pour d’autres. Une adresse visible de CDN ou de proxy ne révèle pas forcément le serveur d’origine. Le pays d’un registre ne localise pas à lui seul le traitement de toutes les données.

Exemple distinct du TP : dans une entreprise fictive, le site et le portail client sont servis par le même réseau de diffusion. Cette observation justifie d’examiner une dépendance commune. Elle ne prouve pas encore que les deux origines, supports et plans de reprise sont identiques.

## 5. Passer de l’observation à la stratégie SI

Écrivez séparément : **observation → interprétation → limite → vérification utile**. Une phrase comme « le réseau X est visible pour cette adresse à cet instant » est plus précise que « l’entreprise est entièrement hébergée chez X ».

Pour Asteria, identifiez l’acteur qui peut modifier ou interrompre une dépendance et la fonction affectée. Formulez ensuite un scénario conditionnel : « si ce service devient indisponible, alors… ». Le contexte géopolitique amène à examiner contrôle, dépendances transfrontières, capacité de repli et intérêts des acteurs ; il ne prouve pas une intention hostile ou une obligation juridique.

Une recommandation utile peut être une demande de test ou de preuve, plutôt qu’un changement immédiat de fournisseur. Vos inconnues doivent indiquer quel renseignement permettrait de décider.

Références complémentaires facultatives : [outils et sources officielles](../../docs/OUTILS.md). Les apports ci-dessus suffisent à commencer même si ces sites ne sont pas accessibles.
