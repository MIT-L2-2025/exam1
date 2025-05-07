# 🥡 Workflow n8n – Restaurants chinois à Antananarivo

Ce workflow est utilisé pour lister les restaurants chinois à Antananarivo et générer une page HTML avec leurs informations.

## 🔧 Fonctionnement

1. **Start** : Déclenche manuellement le workflow.
2. **Search Restaurants** : Requête HTTP vers l’API Google Maps (Text Search).
3. **Extract Place IDs** : Extrait les `place_id` de chaque résultat.
4. **Get Place Details** : Récupère les infos détaillées pour chaque `place_id`.
5. **Parse & Format Data** : Formate les données en JSON lisible.
6. **Generate HTML** : Génère une page web avec style, cartes et liens.

## ✅ Résultat

Une page HTML prête à afficher :  
- Nom  
- Téléphones  
- Site web  
- Adresse  
- Image  
- Carte avec itinéraire
- Affichage 360° via Google View (peggman)

## 📂 Utilisation

1. Ouvre n8n.
2. Importe le workflow.
3. Exécute le workflow.

   (ou tout simplement ouvrir restaurants.html)
