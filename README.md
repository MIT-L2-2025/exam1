# 🍜 Workflow n8n - Recherche Restaurants Chinois à Antananarivo

Ce workflow **n8n** recherche automatiquement des restaurants chinois à **Antananarivo** en utilisant le web scraping sur un site spécifique et récupère leurs coordonnées GPS via **Google Maps API**.

---

## ⚙️ Fonctionnalités

- Scraping des restaurants chinois sur [findglocal.com]  
- Récupération des coordonnées (latitude, longitude) avec Google Maps  
- Export des résultats au format HTML

---

## 📦 Nodes utilisés

- HTTP Request → pour scrapper  
- HTML Extract → pour extraire les infos (nom, adresse, téléphone)  
- Google Maps API → pour géolocalisation  

---

## 📄 Résultat attendu

| Nom           | Adresse               | Téléphone   | Latitude  | Longitude |
|--------------|-----------------------|-------------|-----------|-----------|
| Dragon Rouge | 10 rue Ravelojaona    | 034 12 345 | -18.8792 | 47.5079  |

---

## 🚀 Usage

1. Importer le workflow `.json` dans n8n  
2. Configurer la clé Google Maps API  
3. Lancer le workflow

---

## 👤 Auteur

Ronhy RAKOTONDRAFARA

