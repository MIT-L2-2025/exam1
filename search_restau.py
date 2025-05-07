import urllib.parse
from apify_client import ApifyClient

# Clé API Apify
API_KEY = 'apify_api_AARwLtemfW0arwYIL0BxnWvt72J7pK3y6tqD'  

# Fonction pour effectuer la recherche avec Apify
def search_restaurants():
    # Initialiser le client Apify
    client = ApifyClient(API_KEY)
    
    # Coordonnées d'Antananarivo, Madagascar
    antananarivo_coords = {
        'lat': -18.8792,  # Latitude d'Antananarivo
        'lng': 47.5079    # Longitude d'Antananarivo
    }
    
    # Configurer les paramètres de l'acteur
    actor_id = 'compass~crawler-google-places'
    run_input = {
        'searchStringsArray': ['chinese restaurant'],  # Terme de recherche
        'lat': antananarivo_coords['lat'],            # Latitude
        'lng': antananarivo_coords['lng'],            # Longitude
        'zoom': 12,                                   # Zoom pour limiter la zone
        'maxCrawledPlaces': 20,                       # Limite de résultats
        'language': 'fr',                             # Langue des résultats
        'includeGoogleReviews': False,                 # Exclure les avis pour accélérer
        'includePhotos': True,                        # Inclure les photos
        'scrapePhoneNumbers': True,                   # Extraire les numéros de téléphone
    }
    
    try:
        # Exécuter l'acteur et attendre les résultats
        run = client.actor(actor_id).call(run_input=run_input)
        
        # Récupérer les résultats depuis le dataset
        if run.get('defaultDatasetId'):
            dataset = client.dataset(run['defaultDatasetId']).list_items()
            results = dataset.items
            # Journaliser les résultats pour débogage
            print("Résultats bruts :", results)
            return results
        else:
            print("Aucun résultat trouvé dans le dataset.")
            return []
    except Exception as e:
        print(f"Erreur lors de la recherche : {e}")
        return []

# Fonction pour filtrer les restaurants à Antananarivo
def is_in_antananarivo(place):
    address = place.get('address', '').lower()
    # Vérifier si l'adresse contient "Antananarivo" ou "Madagascar"
    return 'antananarivo' in address or 'madagascar' in address

# Modèle HTML avec CSS intégré (accolades échappées)
html_template = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restaurants Chinois à Antananarivo</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 20px;
            color: #333;
        }}
        h1 {{
            text-align: center;
            color: #2c3e50;
            margin-bottom: 30px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .restaurant-card {{
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
            padding: 20px;
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }}
        .restaurant-card img {{
            max-width: 200px;
            border-radius: 8px;
            object-fit: cover;
        }}
        .restaurant-info {{
            flex: 1;
            min-width: 250px;
        }}
        .restaurant-info p {{
            margin: 10px 0;
            line-height: 1.6;
        }}
        .restaurant-info strong {{
            color: #2c3e50;
        }}
        .restaurant-info a {{
            color: #007bff;
            text-decoration: none;
        }}
        .restaurant-info a:hover {{
            text-decoration: underline;
        }}
        .no-results {{
            text-align: center;
            font-size: 1.2em;
            color: #e74c3c;
        }}
        @media (max-width: 600px) {{
            .restaurant-card {{
                flex-direction: column;
                align-items: center;
            }}
            .restaurant-card img {{
                max-width: 100%;
            }}
        }}
    </style>
</head>
<body>
    <h1>Restaurants Chinois à Antananarivo, Madagascar</h1>
    <div class="container">
        {restaurants_html}
    </div>
</body>
</html>
"""

# Fonction pour générer le HTML pour chaque restaurant
def generate_restaurant_html(place):
    name = place.get('title', 'Nom non disponible')
    address = place.get('address', 'Adresse non disponible')
    
    # Vérifier plusieurs clés pour les contacts
    phone_keys = ['phoneNumber', 'phone', 'formattedPhoneNumber', 'contact']
    phone = 'Contact non disponible'
    for key in phone_keys:
        if place.get(key):
            phone = place.get(key)
            break
    
    coordinates = place.get('location', {'lat': 'Non disponible', 'lng': 'Non disponible'})
    categories = place.get('categoryName', 'Chinese Restaurant').split(', ')
    
    # Gestion des images
    thumbnail = place.get('thumbnailUrl', None)
    photos = place.get('photos', [])  # Vérifier si des photos sont disponibles
    if photos and len(photos) > 0:
        # Utiliser la première photo si disponible
        thumbnail = photos[0].get('url', None)
    # Vérifier d'autres clés d'image possibles
    image_keys = ['image', 'imageUrl', 'mainImage']
    for key in image_keys:
        if place.get(key):
            thumbnail = place.get(key)
            break
    photo_html = f'<img src="{thumbnail}" alt="{name}">' if thumbnail else '<p>Photo non disponible</p>'
    
    categories_str = ', '.join(categories)
    coordinates_str = f"Latitude {coordinates['lat']}, Longitude {coordinates['lng']}"
    
    # Générer le lien Google Maps
    if coordinates['lat'] != 'Non disponible' and coordinates['lng'] != 'Non disponible':
        maps_link = f"https://www.google.com/maps?q={coordinates['lat']},{coordinates['lng']}"
    else:
        # Encoder l'adresse pour l'URL
        encoded_address = urllib.parse.quote(address)
        maps_link = f"https://www.google.com/maps?q={encoded_address}"
    
    maps_html = f'<p><strong>Localisation :</strong> <a href="{maps_link}" target="_blank">Voir sur Google Maps</a></p>'
    
    return f"""
        <div class="restaurant-card">
            {photo_html}
            <div class="restaurant-info">
                <p><strong>Nom :</strong> {name}</p>
                <p><strong>Adresse :</strong> {address}</p>
                <p><strong>Contact :</strong> {phone}</p>
                <p><strong>Coordonnées :</strong> {coordinates_str}</p>
                <p><strong>Spécialités :</strong> {categories_str}</p>
                {maps_html}
            </div>
        </div>
    """

# Effectuer la recherche et générer le HTML
data = search_restaurants()
restaurants_html = ""

if data:
    # Filtrer les restaurants pour ne garder que ceux à Antananarivo
    filtered_data = [place for place in data if is_in_antananarivo(place)]
    if filtered_data:
        for place in filtered_data:
            restaurants_html += generate_restaurant_html(place)
    else:
        restaurants_html = '<p class="no-results">Aucun restaurant chinois trouvé à Antananarivo, Madagascar.</p>'
else:
    restaurants_html = '<p class="no-results">Aucun restaurant chinois trouvé.</p>'

# Générez le fichier HTML
with open('rest.html', 'w', encoding='utf-8') as f:
    f.write(html_template.format(restaurants_html=restaurants_html))

print("Fichier HTML généré : rest.html")