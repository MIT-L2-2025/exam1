# Projet : Restaurant chinois à Antananarivo

## Objectif:
__ Collecter les restaurants chinois à Antananarivo avec les informations : nom, adresse, latitude, longitude, contact, itinéraire et carte
__ Classer les listes des restaurants en: Vraiment chinois, Moyennement chinois et Pas chinois

## Technologie utilisée: 
__ Workflow n8n : pour la collecte des données et la classification

__ Langage de programmation : - python: graph construction
                              - java script: dans les noeuds code de n8n
## Description des fichiers présents dans ce projet

### Fichier 1: Data_extraction_workflow.json
- C'est un workflow fait à partir du programme n8n pour collecter les données depuis des sites web.
- Elle génère automatiquemEllent le fichier **restaurant.json** dans votre repertoire personnel contenant toutes les informations sur les restaurants chinois collecter.

### Fichier 2: Analyse_sur_la classification.md
- C'est un fichier markdown qui explique le fonctionnement et les étapes à suivre pour parvenir à la classification (analyse mathématiques)
- Je vous recommende de lire attentivement ce fichier pour comprendre comment le workflow de classification fonctionne 
- Cela explique l'utilisation du fichier **graph.py** avec **restaurant_extrait.json** (extrait de restaurant.json) 

### Fichier 3: classification_workflow.json
- Ce workflow fait la classification des restaurants obtenus en utilisant les données du **restaurant.json** et suit la méthode décrite dans **Analyse_sur_la classification.md**
- De plus ce workflow génère automatiquement le fichier **classification.html**

### Fichier 4: classification.html
 C'est une page web pour une visualisation des classifications des restaurants et aussi voir les informations concernant les restaurants

- Cette page constitue un tableau montrant les classifications des restaurants: leurs probabilités pour pouvoir affirmer que c'est un restaurant chinois; les scores attribuées à chaque variable
- Elle constitue aussi un diagramme de répartition des classifications (à la fin du tableau)
- Pouvez aussi chercher un restaurant spécifique et voir les informations à partir de la barre de recherche
- Vous pouvez aussi appuyer sur la cage des tableaux pour voir les informations concernant le restaurant
- Veuillez le télécharger et voir ses fonctionnalités

Auteur : ANJARAVONJISOA Mandresy Clémence
