# Dossier 01 — Note d’organisation et fiches fournisseurs

**P1 — Activités, déclarations de la direction des opérations.** Asteria compte 180 salariés, dont 15 dans la filiale commerciale d’Estérie. Les pays et les organisations du cas sont fictifs.

| Activité | Ressource nécessaire | Tolérance d’interruption proposée par le métier | Impact de référence |
|---|---|---|---|
| Enregistrer et confirmer les commandes | Suite Orion, accès utilisateurs | 4 heures ouvrées | Au-delà, retards de confirmation et pénalités possibles |
| Produire les capteurs | Ordres de fabrication extraits d’Orion chaque matin | 1 journée avec les ordres déjà imprimés | 20 k€ de marge et pénalités exposées par jour après épuisement |
| Expédier | Liste validée, transporteur, responsable logistique | 8 heures ouvrées | Peut aggraver les mêmes retards que la production |
| Paie | Prestataire PaieClaire | 3 jours hors clôture ; 1 jour à la clôture | Salaires retardés, conséquences humaines |

Les pertes production et expédition concernent en partie les mêmes commandes : **ne pas les additionner sans retraitement**. La tolérance n’est pas une promesse de reprise fournie par la SI.

**P2 — Déclarations commerciales.** Orion est contracté auprès de NordSuite, hébergé en Valorie. L’accès est fourni par le service Identia, exploité par AccèsGlobal. NordSuite propose des exports et des sauvegardes mais ne précise pas ici qui peut les déclencher sans Identia. La paie utilise aussi Identia. Le contrat de PaieClaire est distinct de celui de NordSuite.

**P3 — Organisation interne.** La DSI a quatre personnes. Une seule possède le contact d’escalade prioritaire NordSuite ; aucun suppléant n’est renseigné. La responsable logistique peut déclencher le travail sur documents imprimés. La DAF peut autoriser une dépense exceptionnelle jusqu’à 10 k€. Au-delà, validation de la DG. Aucun compte rendu récent d’exercice de continuité n’est disponible.

**P4 — Message du commercial NordSuite.** « Votre environnement principal et votre sauvegarde sont dans deux sites différents ; vous êtes indépendants de toute panne. » Les sites utilisent le même prestataire d’identité. Le contrat disponible ne décrit pas le scénario de perte de cet acteur.

Votre carte peut être un tableau ou une liste de relations. Chaque relation importante doit citer P1, P2, P3 ou P4. Ne pas inférer une obligation juridique d’un pays fictif.
