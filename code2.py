import json
import os
from datetime import datetime

# Charger les données JSON
with open('file.json', 'r', encoding='utf-8') as file:
    restaurants = json.load(file)

# Fonction pour formater les horaires d'ouverture
def format_opening_hours(hours):
    if not hours:
        return "Non disponible"
    formatted = ""
    for entry in hours:
        day = entry.get('day', 'Inconnu')
        hours_str = entry.get('hours', 'Non disponible')
        formatted += f"<p><strong>{day}:</strong> {hours_str}</p>"
    return formatted

# Générer le contenu HTML
html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liste des Restaurants Chinois à Antananarivo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .restaurant-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
        }
        .restaurant-card {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            width: 300px;
            padding: 15px;
            margin: 10px;
            transition: transform 0.2s;
        }
        .restaurant-card:hover {
            transform: scale(1.05);
        }
        .restaurant-card img {
            max-width: 100%;
            height: auto;
            border-radius: 5px;
        }
        .restaurant-card h2 {
            font-size: 1.5em;
            margin: 10px 0;
            color: #d32f2f;
        }
        .restaurant-card p {
            margin: 5px 0;
            color: #555;
        }
        .restaurant-card a {
            color: #1e88e5;
            text-decoration: none;
        }
        .restaurant-card a:hover {
            text-decoration: underline;
        }
        .score {
            font-weight: bold;
            color: #388e3c;
        }
    </style>
</head>
<body>
    <h1>Restaurants Chinois à Antananarivo</h1>
    <div class="restaurant-container">
"""

# Ajouter chaque restaurant au HTML
for restaurant in restaurants:
    title = restaurant.get('title', 'Nom inconnu')
    address = restaurant.get('address', 'Adresse inconnue')
    total_score = restaurant.get('totalScore', 'N/A')
    phone = restaurant.get('phone', 'Non disponible')
    opening_hours = restaurant.get('openingHours', [])
    image_url = restaurant.get('imageUrl', '')
    maps_url = restaurant.get('url', '#')
    category = restaurant.get('categoryName', 'Non spécifié')
    
    # Formater les horaires
    hours_formatted = format_opening_hours(opening_hours)
    
    # Ajouter la carte du restaurant
    html_content += f"""
        <div class="restaurant-card">
            {f'<img src="{image_url}" alt="{title}">' if image_url else ''}
            <h2>{title}</h2>
            <p><strong>Catégorie:</strong> {category}</p>
            <p><strong>Adresse:</strong> {address}</p>
            <p><strong>Note:</strong> <span class="score">{total_score}/5</span></p>
            <p><strong>Téléphone:</strong> {phone}</p>
            <p><strong>Horaires:</strong></p>
            {hours_formatted}
            <p><a href="{maps_url}" target="_blank">Voir sur Google Maps</a></p>
        </div>
    """

# Fermer les balises HTML
html_content += """
    </div>
</body>
</html>
"""

# Écrire le fichier HTML
output_file = 'restaurants.html'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(html_content)

print(f"Fichier HTML généré : {output_file}")
