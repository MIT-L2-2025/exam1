# Projet Restaurants Chinois à Antananarivo 🍜

## Description

Ce projet est une **automatisation** qui permet de rechercher tous les restaurants chinois à **Antananarivo**, Madagascar, à l'aide de l'outil d'automatisation **open-source n8n** et de l'API **Google Maps**. L'objectif est de faciliter la recherche de restaurants chinois dans cette ville, avec des informations détaillées sur chaque restaurant, telles que le **nom**, l'**adresse**, le **contact**, la **note**, et les **coordonnées GPS** 📍.

Le projet permet également de **générer une page HTML interactive** qui affiche une carte pour chaque restaurant, avec la possibilité de visualiser les informations détaillées lorsqu'on clique sur les marqueurs sur la carte 🗺️.

## Fonctionnalités ✨

- **Recherche automatique des restaurants chinois** : Utilisation de l'API Google Maps pour rechercher et extraire une liste de restaurants chinois à Antananarivo 🍜.
- **Génération dynamique de cartes** : Pour chaque restaurant, une carte Google Maps est générée, affichant sa localisation et permettant une interaction (clic pour voir les détails) 🖱️.
- **Données exportables** : Les résultats de la recherche peuvent être téléchargés sous forme de fichier HTML contenant les informations et les cartes des restaurants 📑.

## Technologies utilisées 💻

- **n8n** : Outil d'automatisation open-source pour la création de workflows visuels 🔄.
- **Google Maps API** : Utilisée pour rechercher les restaurants et afficher leurs emplacements sur une carte 🗺️.
- **HTML/CSS** : Génération de la page web interactive avec des cartes et des informations sur les restaurants 🖥️.
- **JavaScript** : Logique de génération dynamique de la page HTML et d'interaction avec l'API Google Maps 🔧.

## Prérequis 🚀

Avant de pouvoir utiliser ce projet, vous devez disposer des éléments suivants :

- Un compte **Google Cloud** avec une clé API pour **Google Maps Places API** 🔑.
- **n8n** installé sur votre machine ou sur un serveur (ou bien utiliser n8n en ligne) 🌐.
  
### Installation de n8n

Si vous n'avez pas encore installé **n8n**, vous pouvez le faire en suivant les instructions sur la [documentation officielle de n8n](https://docs.n8n.io/getting-started/installation/) ⚙️.

## Configuration du projet ⚙️

### Étape 1 : Créer un workflow dans n8n

1. Créez un nouveau **workflow** dans n8n 🎉.
2. Ajoutez un **Google Maps API Node** dans votre workflow 🗺️.
3. Configurez-le pour interroger l'API Google Maps et rechercher tous les restaurants chinois à **Antananarivo** (vous pouvez spécifier les paramètres de la recherche, comme "restaurant chinois" et "Antananarivo") 🔍.
4. Utilisez les **résultats renvoyés** par l'API pour extraire les informations pertinentes sur chaque restaurant (nom, adresse, coordonnées GPS, téléphone, note, etc.) 📝.

### Étape 2 : Générer le fichier HTML

1. Utilisez le **Node HTML Generator** dans n8n pour générer un fichier HTML contenant les informations sur chaque restaurant 🏷️.
2. Intégrez une carte Google Maps dynamique pour chaque restaurant en utilisant l'API Google Maps pour afficher le lieu sur une carte 📍.
3. Personnalisez le fichier HTML selon vos préférences (couleurs, polices, design) 🎨.

### Étape 3 : Télécharger ou partager le fichier HTML

Une fois le fichier HTML généré, il peut être téléchargé et partagé avec d'autres personnes 📤. Vous pouvez également configurer n8n pour envoyer ce fichier par email 📧 ou le stocker dans un service cloud comme **Google Drive** ☁️.

## Utilisation 🏃‍♂️

1. **Accédez à n8n** : Une fois le workflow configuré, vous pouvez l'exécuter à tout moment pour mettre à jour la liste des restaurants chinois à Antananarivo 🔄.
2. **Recevez un fichier HTML** : Après l'exécution du workflow, vous recevrez un fichier HTML contenant les informations des restaurants, ainsi qu'une carte interactive pour chaque restaurant 📂.

## Exemple de page HTML générée

Une fois le fichier HTML généré, vous pourrez visualiser une page élégante avec des informations comme le **nom**, l'**adresse**, le **contact**, la **note**, et un **marqueur interactif** sur la carte pour chaque restaurant chinois à Antananarivo 🗺️✨.

## Contribuer 🤝

Si vous souhaitez contribuer à ce projet, vous pouvez :

1. **Forker** le projet 🍴.
2. Apporter vos **améliorations** (ajouter de nouvelles fonctionnalités, améliorer le design, etc.) ✨.
3. Soumettre une **pull request** avec vos changements 🔀.

## Licence 📜

Ce projet est sous licence **MIT**. Vous pouvez l'utiliser, le modifier et le redistribuer selon les termes de cette licence 🎉.

---

### Remarques 🔔

N'oubliez pas de remplacer la **clé API** par la vôtre dans le code de génération de la page HTML, et assurez-vous que votre clé API est bien configurée pour l'API **Google Maps Places** 🗝️.

Si vous avez des questions ou des suggestions d'améliorations, n'hésitez pas à ouvrir un **issue** ou à soumettre une **pull request** ! 💬
