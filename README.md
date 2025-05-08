# 📄 README – n8n Workflow: Restaurant chinois Antananarivo

Ce workflow `n8n` automatise la récupération d’informations sur les **restaurants chinois à Antananarivo** depuis le site FindGlocal. Il génère une page HTML contenant les détails et la géolocalisation de chaque restaurant.

---

## 🔁 Fonctionnement général

1. Déclenchement manuel du workflow.
2. Scraping des restaurants chinois depuis FindGlocal.
3. Extraction des liens et images.
4. Scraping des pages individuelles pour extraire :
   - Nom
   - Adresse
   - Téléphone
5. Géocodage des adresses avec l’API OpenCage.
6. Fusion des données.
7. Génération d’un fichier HTML exportable contenant les restaurants formatés.
8. Encodage du fichier HTML en base64 pour téléchargement.

---

## 🧩 Structure du Workflow

### 1. Déclenchement
- `When clicking ‘Test workflow’` : point de départ manuel

### 2. Scraping de la page principale
- `HTTP Request` : téléchargement de la page FindGlocal
- `HTML1` : extraction des liens et images
- `Code2` : reconstruction des URLs complètes

### 3. Traitement par restaurant
- `Loop Over Items` : boucle sur chaque URL
- `HTTP Request1` : téléchargement des pages individuelles
- `Wait` : pause de 0.5 sec pour éviter les restrictions
- `HTML2` : extraction du nom, téléphone et adresse

### 4. Géocodage
- `Loop Over Items1` : boucle sur les adresses extraites
- `HTTP Request2` : appel à OpenCage Geocoding API
- `Wait1` : pause de 0.05 sec
- `Code` : extraction latitude, longitude, lien Google Maps

### 5. Fusion des données
- `Code1` : combine lien et image
- `Merge` : fusionne les données des 3 sources

### 6. Génération HTML
- `Code3` : création du fichier HTML stylisé avec :
  - Image
  - Nom + lien
  - Adresse
  - Téléphone
  - Lien vers Google Maps (si coordonnées disponibles)
- Résultat encodé en base64 dans `binary.data`

---

## 🔐 API utilisée

- **OpenCage Geocoding**  
  URL : `https://api.opencagedata.com/geocode/v1/json`  
  Clé API : `ae3649d8c75b4b50810bd20fea9e605b`  
  (à remplacer par une clé propre en production)

---

## ✅ Prérequis techniques

Avant d’utiliser ce workflow, assurez-vous d’avoir :

- ✅ Une instance fonctionnelle de **n8n** (auto-hébergée ou sur n8n.cloud)
- ✅ Une **clé API valide** de [OpenCage Geocoding](https://opencagedata.com/)
- ✅ Accès à Internet (pour les requêtes HTTP)
- ✅ Les **nœuds standards n8n** (aucun nœud personnalisé requis)
- ✅ Éventuellement, un éditeur pour lire le fichier HTML généré

---

## 🚀 Instructions d’utilisation

### 🔧 Étape 1 – Configuration

1. Importez le fichier `.json` du workflow dans votre instance n8n.
2. Ouvrez le nœud `HTTP Request2` (API OpenCage).
3. Remplacez la clé API par la vôtre si nécessaire.

### ▶️ Étape 2 – Exécution

1. Cliquez sur **“Executer le workflow”** manuellement depuis l’interface.
2. Patientez pendant que le workflow :
   - Scrape les données
   - Géocode les adresses
   - Génère le fichier HTML
3. Récupérez la sortie encodée en base64 dans le nœud `Code3`.

### 💾 Étape 3 – Récupération du fichier

1. Téléchargez les données binaires encodées.
2. Convertissez-les en fichier HTML avec n8n ou via un outil externe :
   - Exemple : [Base64 to File](https://www.base64decode.org/)
3. Ouvrez le fichier HTML dans un navigateur pour visualiser les résultats.

---

## ⚠️ Conditions d’utilisation

- Ce workflow fait du **web scraping** : vous devez vous assurer que vous respectez les conditions d’utilisation de FindGlocal.
- L’**API OpenCage** impose une limite de requêtes gratuites par jour. Ne dépassez pas le quota.
- Le workflow est destiné à un usage personnel, éducatif ou en démonstration.  
  Pour une utilisation en production, optimisez les délais et sécurisez les données.

---

## 📂 Résultat attendu

- **Nom du fichier** : `restaurants_antananarivo.html`
- **Contenu** : page HTML responsive affichant tous les restaurants avec infos et carte
- **Visualisation** : directement dans n’importe quel navigateur

---

## 🧑‍💻 Auteur

Développé avec ❤️ par [Votre Nom / Équipe]  
📧 Contact : [votre-email@example.com] (optionnel)

