import json
import networkx as nx
import matplotlib.pyplot as plt
import re
from math import radians, sin, cos, sqrt, atan2

# Fonction pour calculer la distance haversine (en km)
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Rayon de la Terre en km
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    a = sin(dLat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dLon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Fonctions pour calculer les probabilités p
def name_chineseness(name):
    positive_keywords = ['chinois', 'china', 'qing', 'dragon', 'panda', 'jasmine', 'wan', 'lotus', 'jade', 'shi fu', 'hao', 'rouge', 'empire', 'dynasty', 'tsang', 'chinese', 'hong kong', 'fleur', 'orient', 'oriental']
    negative_keywords = ['malagasy', 'gargotte', 'sushi', 'thai']
    score = 0
    if re.search(r'[\u4e00-\u9fff]', name):  # Caractères chinois
        score += 0.7
    name_lower = name.lower()
    for keyword in positive_keywords:
        if keyword in name_lower:
            score += 0.3
            break
    for keyword in negative_keywords:
        if keyword in name_lower:
            score -= 0.2
            break
    return max(0, min(1, score))

def location_chineseness(lat, lon, vicinity):
    neighborhoods = [
        {'name': 'Behoririka', 'lat': -18.9000, 'lon': 47.5200, 'score': 0.6},
        {'name': 'Analakely', 'lat': -18.9100, 'lon': 47.5250, 'score': 0.5},
        {'name': 'Andrahavoangy', 'lat': -18.8900, 'lon': 47.5100, 'score': 0.5},
        {'name': 'Ankorondrano', 'lat': -18.8700, 'lon': 47.5300, 'score': 0.5},
        {'name': 'Ivato', 'lat': -18.8000, 'lon': 47.4800, 'score': 0.6}
    ]
    proximity_radius = 2  # km
    score = 0.1  # Par défaut
    for neighborhood in neighborhoods:
        distance = haversine_distance(lat, lon, neighborhood['lat'], neighborhood['lon'])
        if distance <= proximity_radius:
            score = neighborhood['score']
            break
       	if neighborhood['name'].lower() in vicinity:
       	    score = neighborhood['score']
       	    break 
    return score

def authors_chineseness(authors):
    if not authors or authors.strip() == 'Unknown':
        return 0
    chinese_names = ['li', 'chen', 'wang', 'zhang', 'liu', 'yang', 'huang', 'ying']
    authors_lower = authors.lower()
    score = 0
    for name in chinese_names:
        if name in authors_lower:
            score += 0.5
            break
        if re.search(r'[\u4e00-\u9fff]', authors_lower):
            score += 0.7
            break
    return min(score, 1)

def text_chineseness(text):
    if not text or text.strip() == '':
        return 0
    positive_keywords =['yum cha', 'dim sum', 'canard laqué', 'mapo tofu', 'xiaolongbao', 'authentique chinois','cuisine sichuanaise', 'cuisine cantonaise', 'wonton', 'raviolis chinois', '飲茶', 'authentique', 'authentic', 'tofu', 'noodle','noodles', 'chinois', 'chinese', 'cantonais', 'the', 'pao', 'tea', 'nouilles', 'cantonese', 'cantonese rice']
    negative_keywords = ['malagasy', 'vazaha', 'ravitoto']
    score = 0
    text_lower = text.lower()
    for keyword in positive_keywords:
        if keyword in text_lower:
            score += 0.4
            break
    for keyword in negative_keywords:
        if keyword in text_lower:
            score -= 0.2
            break
    return max(0, min(1, score))

def rating_chineseness(rating):
    if not rating or rating.strip() == '':
        return 0
    ratings = [float(r) for r in rating.split('.') if r.strip().isdigit()]
    if not ratings:
        return 0
    avg_rating = sum(ratings) / len(ratings)
    if avg_rating >= 4:
        return 0.7
    elif avg_rating >= 3:
        return 0.4
    else:
        return 0.1

# Fonction pour abréger les noms longs
def shorten_name(name, max_length=15):
    return (name[:max_length] + '...') if len(name) > max_length else name

# Charger les données depuis data.json
try:
    with open('restaurant_extrait.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    restaurants = data[0]['restaurants']
except FileNotFoundError:
    print("Erreur : Le fichier restaurant_extrait.json n'a pas été trouvé.")
    exit(1)
except json.JSONDecodeError:
    print("Erreur : Le fichier restaurant_extrait.json est mal formaté.")
    exit(1)
except KeyError:
    print("Erreur : La structure du JSON ne contient pas 'restaurants'.")
    exit(1)

# Créer le graphe biparti
G = nx.Graph()

# Ensembles X (restaurants) et Y (attributs)
X = [r['name'] for r in restaurants]
Y = ['Nom chinois', 'Emplacement', 'Clients chinois', 'Avis authentiques', 'Score élevé']
attributes = ['name', 'location', 'authors', 'text', 'rating']

# Ajouter les sommets
G.add_nodes_from(X, bipartite=0)  # Restaurants
G.add_nodes_from(Y, bipartite=1)  # Attributs

# Ajouter les arcs avec poids p
for i, restaurant in enumerate(restaurants):
    r_name = restaurant['name']
    scores = [
        name_chineseness(restaurant['name']),
        location_chineseness(restaurant['latitude'], restaurant['longitude'], restaurant['vicinity']),
        authors_chineseness(restaurant['all_authors']),
        text_chineseness(restaurant['all_text']),
        rating_chineseness(restaurant['all_rating'])
    ]
    for j, score in enumerate(scores):
        if score >= 0.1:  # Arc existe si p >= 0.1 pour réduire le bruit
            G.add_edge(r_name, Y[j], weight=score)

# Visualisation
plt.figure(figsize=(14, 10), facecolor='white')  # Taille plus grande, fond blanc

# Disposition bipartie
pos = nx.bipartite_layout(G, X, scale=1.5)

# Dessiner les sommets
nx.draw_networkx_nodes(
    G, pos, nodelist=X, node_color='#87CEEB', node_shape='o', node_size=800,
    edgecolors='black', linewidths=0.5, label='Restaurants'
)
nx.draw_networkx_nodes(
    G, pos, nodelist=Y, node_color='#90EE90', node_shape='o', node_size=1000,
    edgecolors='black', linewidths=0.5, label='Attributs'
)

# Dessiner les arcs avec une échelle de couleur basée sur le poids
edges = G.edges(data=True)
weights = [d['weight'] for u, v, d in edges]
nx.draw_networkx_edges(
    G, pos, edge_color=weights, edge_cmap=plt.cm.Blues, width=2,
    edge_vmin=0, edge_vmax=1, alpha=0.7
)

# Dessiner les étiquettes des poids pour p >= 0.3
edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in edges if d['weight'] >= 0.3}
nx.draw_networkx_edge_labels(
    G, pos, edge_labels=edge_labels, font_size=8, font_color='darkblue',
    label_pos=0.6, rotate=False
)

# Dessiner les étiquettes des sommets (noms abrégés pour restaurants)
labels = {node: shorten_name(node) for node in X}
labels.update({node: node for node in Y})
nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_weight='normal')


# Sauvegarder l'image
plt.savefig('bipartite_graph.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()
