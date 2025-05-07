# Restaurants Chinois à Antananarivo

Projet listant les restaurants chinois à Antananarivo, Madagascar, avec un workflow n8n pour automatiser la génération et l’envoi d’un fichier HTML.

## Contenu
- **restaurants_chinois.html** : Fichier HTML affichant une liste de restaurants chinois (ex. : Le Jasmin, O Loft Chinois) avec adresse, téléphone et liens Google Maps.
- **restaurants_workflow.json** : Workflow n8n qui génère, enregistre (`/tmp/restaurants_chinois.html`), envoie (vers `https://httpbin.org/post`) et archive le HTML.

## Utilisation
 **Voir le HTML** : Ouvrez `restaurants_chinois.html` dans un navigateur pour voir la liste.
 **Exécuter le Workflow** :
   - Importez `restaurants_workflow.json` via **Importer depuis un fichier**.
   - Créez `/tmp/sent/` sur votre serveur (`mkdir -p /tmp/sent; chmod -R 777 /tmp/sent`).
   - Exécutez le workflow pour générer, envoyer et archiver le HTML.


## Licence
Sans licence. Utilisation libre.
