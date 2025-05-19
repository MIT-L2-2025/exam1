# ChiTana - README du Workflow n8n

## 📋 Aperçu

**ChiTana** recherche les restaurants chinois dans un rayon de 10 km autour d’Antananarivo (-18.8792, 47.5079). Il traite les données, évalue si un restaurant est chinois via un modèle de score pondéré basé sur des **tests statistiques** (seuillage, moyenne pondérée), et génère une page HTML stylisée.

### 🎯 Objectif
Rechercher tous les restaurants chinois d’Antananarivo.

---

## 🛠️ Structure

Workflow en **graphe acyclique dirigé (DAG)** :
- **Nœuds** : Tâches (ex. : extraction, formatage).
- **Arêtes** : Flux de données.

### Nœuds Principaux
1. **Déclencheur** : Lance le workflow.
2. **Recherche Initiale** : Liste les restaurants avec "chinois".
3. **Vérif. Page Suivante** : Cherche d’autres résultats.
4. **Attente** : Pause de 2s.
5. **Requête Suivante** : Récupère plus de résultats.
6. **Fusion Pages** : Combine les résultats.
7. **Extraction** : Extrait les données.
8. **Formatage Initial** : Structure les données.
9. **Détails** : Ajoute infos (téléphone, photos).
10. **Formatage Final** : Prépare images, liens, horaires.
11. **Prompt** : Crée des prompts d’évaluation.
12. **Évaluation** : Score les critères (AI Agent).
13. **JSON** : Convertit en JSON.
14. **Score Pondéré** : Calcule le score final.
15. **Fusion Finale** : Combine données et scores.
16. **HTML** : Génère une page avec Tailwind CSS.

### Flux (DAG)
```
Déclencheur → Recherche → Vérif. Page → Attente →wamy → Recherche → Vérif. Page → Attente → Requête ↺
              ↓                 ↓
           Fusion Pages ←←←←←←←
              ↓
           Extraction → Formatage → Détails → Formatage Final
                                     ↓
                                  Prompt → Évaluation → JSON → Score
                                     ↓                        ↓
                                  Fusion -------------------→ HTML
```

---

## 📊 Modèle de Score Pondéré

Le nœud `CHI 2 code` évalue si un restaurant est chinois via des tests statistiques.

### Critères et Poids
Les critères forment un **graphe pondéré** où chaque nœud (critère) a un poids influençant le score final. Les arêtes relient les critères au score global, avec des poids reflétant leur importance, établis par analyse statistique de pertinence.

- **Nom (`name_score`)** : Poids = **5**. Vérifie si le nom semble chinois (ex. : pinyin, caractères).
- **Adresse (`address_score`)** : Poids = **0**. Non utilisé (données insuffisantes).
- **Horaires (`opening_hours_score`)** : Poids = **2**. Évalue les horaires typiques (ex. : ouvert tard).
- **Proximité (`location_proximity_score`)** : Poids = **1**. Mesure la distance aux quartiers chinois.
- **Évaluation (`Noters`, `Specialist`)** : Utilise un **AI Agent** pour attribuer des scores [0,1], évitant le traitement complexe de langage naturel dans n8n et compensant l’absence de base de données locale en fournissant des valeurs normalisées.

#### Décision des Poids
Les poids sont choisis via une analyse statistique de pertinence :
- **Nom (5)** : Plus discriminant (noms chinois sont distinctifs).
- **Horaires (2)** : Moins spécifique mais indicatif (horaires typiques).
- **Proximité (1)** : Utile mais moins fiable (données géographiques limitées).
- **Adresse (0)** : Non utilisé faute de données sur les quartiers chinois.

#### Visualisation du Graphe Pondéré
```
   [Nom, 5] → [Score Final]
   [Adresse, 0] → [Score Final]
   [Horaires, 2] → [Score Final]
   [Proximité, 1] → [Score Final]
```

#### Pourquoi l’AI Agent ?
- **Éviter le traitement de texte** : Simplifie l’analyse des noms/horaires en fournissant des scores [0,1], sans parsing complexe dans n8n.
- **Compenser le manque de données** : Fournit des estimations fiables malgré l’absence de base de données locale sur les restaurants chinois.
- **Précision** : Réduit les erreurs en normalisant les critères (ex. : détecte "Dragon" comme chinois).
- **Efficacité** : Automatise l’évaluation sémantique, économisant des règles manuelles.

### Calcul du Score
1. **Score Total** :  
   \[ \text{Score Total} = (5 \times \text{name_score}) + (0 \times \text{address_score}) + (2 \times \text{opening_hours_score}) + (1 \times \text{location_proximity_score}) \]
2. **Poids Total** : 5 + 0 + 2 + 1 = 8
3. **Score Final** :  
   \[ \text{Score Final} = \frac{\text{Score Total}}{8} \]
4. **Test Statistique** : Seuil à 0.7 (70 %) pour classer comme chinois.
5. **Confiance** : `Math.round(Score Final * 100)` %.

### Exemple
Pour un restaurant :
- `name_score = 0.9`
- `address_score = 0`
- `opening_hours_score = 0.8`
- `location_proximity_score = 0.6`

\[ \text{Score Total} = (5 \times 0.9) + (0 \times 0) + (2 \times 0.8) + (1 \times 0.6) = 6.7 \]  
\[ \text{Score Final} = \frac{6.7}{8} \approx 0.8375 \]  
\[ \text{Confiance} = 84\% \]  
**Résultat** : Chinois (✅).

---

## 🌐 Concepts de Graphe

Le workflow est un **DAG** :
- **Nœuds** : Tâches.
- **Arêtes** : Flux de données.
- **Acyclique** : Boucle contrôlée pour pagination.
- **Dirigé** : Données à sens unique.

---

## ➗ Concepts Mathématiques

### 1. Haversine (Proximité)
Calcule la distance aux quartiers chinois :  
\[ a = \sin^2\left(\frac{\Delta \phi}{2}\right) + \cos(\phi_1) \cdot \cos(\phi_2) \cdot \sin^2\left(\frac{\Delta \lambda}{2}\right) \]  
\[ c = 2 \cdot \atan2\left(\sqrt{a}, \sqrt{1-a}\right) \]  
\[ d = 6371 \cdot c \]  
**Score** : \(\max(0, 1 - \frac{d}{1.0}) \cdot \text{poids}\).

### 2. Moyenne Pondérée
Combine les critères avec leurs poids.

### 3. Seuillage
Seuil de 0.7 pour classification binaire.

---

## 📄 Sortie

Fichier HTML (`restaurants_antananarivo.html`) :
- **Cartes** : Nom, adresse, téléphone, horaires, image, note, lien.
- **Badge** : ✅ (chinois) ou ❌ avec confiance.
- **Style** : Tailwind CSS.

### Exemple de Carte
```
[Image]
✅ 84%
Nom : Dragon d'Or
Adresse : 123 Rue Behoririka
Téléphone : +261 34 567 890
Note : ★★★★☆ (120 avis)
Horaires : Lun-Dim 11:00-22:00
[Lien]
```

---

## 🚀 Utilisation
1. Importer le JSON dans n8n.
2. Configurer les paramètres.
3. Exécuter "Test workflow".
4. Vérifier l’HTML dans `Fomulate html`.

---

## ⚠️ Limites
- Précision des données.
- Adresse non utilisée.
- Délais de pagination.

---

## 🔮 Améliorations
- Analyse automatique de la pertinence des variables.
- Intégrer l’adresse dans le score.
- Optimiser la pagination.