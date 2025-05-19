# ChiTana - README du Workflow n8n

## 📖 Aperçu

**ChiTana** est un workflow n8n qui identifie les restaurants chinois dans un rayon de 10 km autour d’Antananarivo, Madagascar (-18.8792, 47.5079). Il collecte des données via une API, évalue les restaurants avec un modèle de score pondéré basé sur des tests statistiques, et génère une page HTML stylisée avec Tailwind CSS.

### 🎯 Objectif
Lister les restaurants chinois à Antananarivo avec une classification précise.

---

## 🏗️ Architecture

Le workflow est un **graphe acyclique dirigé (DAG)** où :
- **Nœuds** : Tâches (recherche, évaluation, etc.).
- **Arêtes** : Flux de données.

### 🔄 Flux du Workflow
```
Déclencheur → Recherche → Vérif. Page → Attente (2s) → Requête Suivante ↺
              ↓                 ↓
           Fusion Pages ←←←←←←←
              ↓
           Extraction → Formatage → Détails → Formatage Final
                                     ↓
                                  Prompt → Évaluation AI → JSON → Score
                                     ↓                        ↓
                                  Fusion -------------------→ HTML
```

### 📑 Nœuds Clés
1. **Déclencheur** : Lance le workflow.
2. **Recherche** : Collecte les restaurants avec "chinois" via API.
3. **Vérif. Page** : Vérifie les résultats supplémentaires.
4. **Attente** : Pause de 2s pour limiter les requêtes.
5. **Fusion Pages** : Combine les pages de résultats.
6. **Extraction** : Extrait nom, adresse, etc.
7. **Formatage** : Structure les données.
8. **Détails** : Ajoute téléphone, photos, horaires.
9. **Prompt** : Crée des prompts pour l’agent AI.
10. **Évaluation AI** : Attribue des scores [0,1].
11. **JSON** : Convertit en JSON.
12. **Score** : Calcule le score final.
13. **HTML** : Génère une page avec Tailwind CSS.

---

## 📈 Modèle de Score

Le nœud `CHI 2 code` classe les restaurants comme chinois via un **score pondéré**.

### 🔢 Critères et Poids
- **Nom** (poids = 5) : Détecte les termes chinois (ex. : "Dragon").
- **Horaires** (poids = 2) : Vérifie les horaires typiques.
- **Proximité** (poids = 1) : Mesure la distance aux quartiers chinois.
- **Adresse** (poids = 0) : Non utilisé (données insuffisantes).

#### 🧠 Agent AI
L’agent AI normalise les scores [0,1], simplifiant l’analyse sémantique et compensant le manque de données locales.

### 🧮 Calcul
1. **Score Total** :  
   \[ (5 \times \text{nom}) + (2 \times \text{horaires}) + (1 \times \text{proximité}) \]
2. **Score Final** :  
   \[ \frac{\text{Score Total}}{8} \]
3. **Classification** : Chinois si score ≥ 0.7 (70 %).
4. **Confiance** : Score × 100 %.

#### Exemple
- Nom : 0.9, Horaires : 0.8, Proximité : 0.6
- Score Total : \( (5 \times 0.9) + (2 \times 0.8) + (1 \times 0.6) = 6.7 \)
- Score Final : \( 6.7 / 8 \approx 0.84 \) (84 %)
- Résultat : Chinois (✅).

---

## 🛠️ Prérequis
- **n8n** : Version récente installée.
- **Configuration** : Importer le fichier JSON du workflow.

---

## 🌍 Concepts Techniques

1. **DAG** : Structure acyclique avec flux unidirectionnels.
2. **Haversine** : Calcule la distance géographique :  
   \[ d = 6371 \cdot 2 \cdot \atan2(\sqrt{a}, \sqrt{1-a}) \]  
   où \( a \) dépend des latitudes/longitudes.
3. **Score Pondéré** : Combine les critères pour une classification binaire.

---

## 📄 Sortie

Un fichier HTML (`restaurants_antananarivo.html`) avec :
- **Cartes** : Nom, adresse, téléphone, horaires, image, note, lien.
- **Badge** : ✅ (chinois) ou ❌ avec pourcentage de confiance.

### Exemple de Carte
```
[Image]
✅ 84%
Dragon d'Or
123 Rue Behoririka
+261 34 567 890
★★★★☆ (120 avis)
Lun-Dim 11:00-22:00
[Lien]
```

---

## 🚀 Utilisation
1. Importer le JSON dans n8n.
3. Exécuter via "Test workflow".
4. Vérifier l’HTML dans le nœud `Formulate HTML`.


## 🔮 Améliorations
1. **Priorité 1** : Ajuster les poids via apprentissage statistique.
2. **Priorité 2** : Intégrer une base de données locale pour les adresses.
---

## ✨ Conclusion

**ChiTana** automatise la recherche et la classification des restaurants chinois à Antananarivo, combinant efficacité et présentation visuelle. Avec des améliorations, il pourrait s’étendre à d’autres villes ou cuisines.

---
## exemple de html
![Screenshot_20250519_152726](https://github.com/user-attachments/assets/b72da780-6509-4066-8e0f-5e815204ce72)
![Screenshot_20250519_152629](https://github.com/user-attachments/assets/d4a34cf2-0c97-401f-80bd-8cec0b410396)




