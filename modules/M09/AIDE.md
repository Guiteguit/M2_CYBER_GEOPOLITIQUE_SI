# M09 — Aides progressives

Toutes les commandes partent de la racine du dépôt. Sous Windows, remplacer `python3` par `py -3` si nécessaire. Copier les fichiers avec l’explorateur ou VS Code ; créer le répertoire `lab/runtime/m09` sans toucher aux données fournies.

1. **Lire un chemin :** partir du nom du service, suivre `depends_on` jusqu’aux composants sans dépendance. Relever les composants retrouvés depuis plusieurs services.
2. **Comparer :** pour chaque correspondance composant/version, consulter la condition de l’avis puis les paramètres du service. L’auditeur n’effectue pas cette comparaison.
3. **Choisir un lot :** copier l’inventaire, modifier les versions d’un lot puis comparer la sortie. Vérifier chaque contrainte de compatibilité déclarée dans le dossier. Une absence d’avis n’est pas un test fonctionnel.

```bash
python3 scripts/auditer_dependances.py --inventory lab/runtime/m09/inventaire_candidat.json --advisories modules/M09/donnees/avis.json
```

Conserver la sortie affichée dans une preuve texte, ou ajouter `> lab/runtime/m09/audit_candidat.json` pour la rediriger. Le JSON candidat reste dans le runtime ; copier seulement les preuves choisies dans le rendu.

Si une clé ou un JSON est invalide : comparer avec la copie intacte, vérifier virgules et guillemets, conserver l’erreur. Après trois à cinq minutes sans progrès, montrer au formateur objectif, hypothèse, tentative et erreur. Après un indice, choisir et expliquer vous-mêmes le test suivant.

**Secours sans Python :** suivre les relations et croiser avis/version/conditions dans un tableau. Écrire les modifications proposées et leurs résultats prédits ; ne pas les présenter comme un audit exécuté. Le formateur aide à distinguer les compétences démontrées.
