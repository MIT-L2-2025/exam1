import os
import json

def extract_json(data):
    # Crée le répertoire cible si il n'existe pas
    directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data"))
    os.makedirs(directory, exist_ok=True)

    # Chemin complet vers le fichier
    file_path = os.path.join(directory, "restaurants.json")
    print(f"[INFO] Enregistrement du JSON ici : {file_path}")

    # Sauvegarde du JSON
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
