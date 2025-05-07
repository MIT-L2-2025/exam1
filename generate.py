import json

def generate_restaurant_html():
    # Charger les données JSON
    with open('file.json', 'r', encoding='utf-8') as f:
        restaurants = json.load(f)
    
    # Créer le contenu HTML
    html_content = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Restaurants à Antananarivo</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 20px;
                background-color: #f5f5f5;
                color: #333;
            }
            h1 {
                color: #d35400;
                text-align: center;
                margin-bottom: 30px;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
            }
            .restaurant-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
                gap: 20px;
            }
            .restaurant-card {
                background-color: white;
                border-radius: 8px;
                padding: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease;
            }
            .restaurant-card:hover {
                transform: translateY(-5px);
            }
            .restaurant-name {
                color: #d35400;
                margin-top: 0;
                font-size: 20px;
            }
            .restaurant-info {
                margin-bottom: 15px;
            }
            .directions-btn {
                display: inline-block;
                background-color: #3498db;
                color: white;
                padding: 8px 15px;
                border-radius: 4px;
                text-decoration: none;
                font-weight: bold;
                transition: background-color 0.3s ease;
            }
            .directions-btn:hover {
                background-color: #2980b9;
            }
            .map-container {
                margin-top: 40px;
                height: 500px;
                border-radius: 8px;
                overflow: hidden;
            }
            @media (max-width: 768px) {
                .restaurant-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Restaurants à Antananarivo</h1>
            
            <div class="restaurant-grid">
    """
    
    # Ajouter chaque restaurant à la grille
    for restaurant in restaurants:
        name = restaurant['name']
        address = restaurant['address']
        contact = restaurant['contact']
        lat = restaurant['coordinates']['lat']
        lng = restaurant['coordinates']['lng']
        
        # Créer le lien pour l'itinéraire Google Maps
        directions_link = f"https://www.google.com/maps/dir/?api=1&destination={lat},{lng}"
        
        html_content += f"""
                <div class="restaurant-card">
                    <h2 class="restaurant-name">{name}</h2>
                    <div class="restaurant-info">
                        <p><strong>Adresse:</strong> {address}</p>
                        <p><strong>Contact:</strong> {contact}</p>
                        <p><strong>Coordonnées:</strong> {lat}, {lng}</p>
                    </div>
                    <a href="{directions_link}" class="directions-btn" target="_blank">Obtenir l'itinéraire</a>
                </div>
        """
    
    # Ajouter la carte Google Maps avec tous les restaurants marqués
    markers_js = ""
    for i, restaurant in enumerate(restaurants):
        name = restaurant['name'].replace("'", "\\'")
        lat = restaurant['coordinates']['lat']
        lng = restaurant['coordinates']['lng']
        markers_js += f"""
            var marker{i} = new google.maps.Marker({{
                position: {{lat: {lat}, lng: {lng}}},
                map: map,
                title: '{name}'
            }});
            
            var infowindow{i} = new google.maps.InfoWindow({{
                content: '<div><strong>{name}</strong><br><a href="https://www.google.com/maps/dir/?api=1&destination={lat},{lng}" target="_blank">Obtenir l\'itinéraire</a></div>'
            }});
            
            marker{i}.addListener('click', function() {{
                infowindow{i}.open(map, marker{i});
            }});
        """
    
    # Compléter le HTML avec la carte et le script
    html_content += f"""
            </div>
            
            <div class="map-container" id="map"></div>
            
            <script>
                function initMap() {{
                    // Coordonnées centrales d'Antananarivo
                    var antananarivo = {{lat: -18.8792, lng: 47.5079}};
                    
                    var map = new google.maps.Map(document.getElementById('map'), {{
                        zoom: 12,
                        center: antananarivo
                    }});
                    
                    // Ajouter les marqueurs pour chaque restaurant
                    {markers_js}
                }}
            </script>
            <script async defer
                src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap">
            </script>
        </div>
    </body>
    </html>
    """
    
    # Écrire le contenu HTML dans un fichier
    with open('restaurants_antananarivo.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Le fichier HTML a été généré avec succès: restaurants_antananarivo.html")

if __name__ == "__main__":
    generate_restaurant_html()