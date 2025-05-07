# Restaurants Chinois à Antananarivo

Projet listant les restaurants chinois à Antananarivo, Madagascar, avec un workflow n8n pour automatiser la génération et l’envoi d’un fichier HTML.

## Contenu
- **restaurants_chinois.html** : Fichier HTML affichant une liste de restaurants chinois (ex. : Le Jasmin, O Loft Chinois) avec adresse, téléphone et liens Google Maps.
- **restaurants_workflow.json** : Workflow n8n qui génère, enregistre (`/tmp/restaurants_chinois.html`), envoie (vers `https://httpbin.org/post`) et archive le HTML.
- **.gitignore** : Exclut les fichiers temporaires.

## Utilisation
1. **Voir le HTML** : Ouvrez `restaurants_chinois.html` dans un navigateur pour voir la liste.
2. **Exécuter le Workflow** :
   - Installez n8n (https://n8n.io/).
   - Importez `restaurants_workflow.json` via **Importer depuis un fichier**.
   - Créez `/tmp/sent/` sur votre serveur (`mkdir -p /tmp/sent; chmod -R 777 /tmp/sent`).
   - Exécutez le workflow pour générer, envoyer et archiver le HTML.
3. **Personnaliser** :
   - Modifiez le nœud **Send File** dans n8n avec votre URL d’API (remplacez `https://httpbin.org/post`).
   - Ajoutez des en-têtes d’authentification si nécessaire (ex. : `Authorization: Bearer votre_token`).
   - Étendez la liste des restaurants dans le nœud **Set Data** (contactez le mainteneur pour la liste complète).

## Remarques
- Le HTML inclut deux restaurants exemples. Le workflow peut générer la liste complète (42 restaurants) si mis à jour.
- Sécurisez `/tmp/` et `/tmp/sent/` en production.
- Pour automatiser, ajoutez un nœud **Schedule Trigger** dans n8n.

## Licence
Sans licence. Utilisation libre.

## Contact
Pour des questions ou la liste complète des restaurants, ouvrez une issue GitHub.