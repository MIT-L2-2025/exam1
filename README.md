


# 🍜 Projet de Scraping Google Maps + Interface Web

Ce projet permet de scraper des données depuis Google Maps (restaurants, etc.) et de visualiser les résultats dans une interface web.

---

Une version déployée est disponible sur :
🔗 [https://chinese-resto.vercel.app/](https://chinese-resto.vercel.app/)

---

## ⚙️ Prérequis

- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js 16+ et npm](https://nodejs.org/)
- Google Chrome installé (utilisé par Playwright pour le scraping)

---

## 📦 Installation du projet

### 1. Cloner le dépôt

```bash
git clone https://github.com/Tomefy5/Chinese-Resto
cd /chemin/du/repository
```

Remplacer **/chemin/du/repository** par le chemin où vous avez placé le clone de ce repository.

### 2. Configuration de l'environnement Python

#### a. Créer et activer un environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate         # Sous Linux/macOS
# ou
venv\Scripts\activate            # Sous Windows
```

#### b. Installer les dépendances

```bash
pip install -r requirements.txt
```

> 💡 Assurez-vous d’avoir `playwright` installé et initialisé si ce n’est pas encore fait :

```bash
playwright install
```

---

## 🛰️ Lancement du Scraping

### Activer l'environnement (si non encore activé)

```bash
source venv/bin/activate         # ou le chemin vers votre environnement
```

### Lancer le script principal

```bash
python3 main.py
```

⏳ *Cette opération peut prendre quelques minutes selon le volume de données à scraper.*

---

## 🌐 Lancement de l'interface Web (Visualisation)

### 1. Accéder au dossier du frontend

```bash
cd ./tana-chinese-web
```

### 2. Installer les dépendances Node.js

```bash
npm install
```

### 3. Démarrer le serveur de développement

```bash
npm run dev
```

🌍 Accédez ensuite à l'application sur : [http://localhost:8080](http://localhost:8080)

---

## ⚙️ Personnalisation du scraping

Vous pouvez modifier les paramètres dans le fichier :

```
src/scraping/google_map_scraper.py
```

### 🔧 Paramètres modifiables

* `max_result` : nombre maximum de résultats à scraper.
* `scroll iterations` : nombre de défilements pour charger plus de résultats.

#### Exemple de boucle de scroll :

```python
scroll_container = page.locator("div[role='feed']")
for _ in range(3):  # Ajustez ce nombre selon la profondeur souhaitée
    await scroll_container.evaluate("(el) => el.scrollBy(0, 1000)")
    await asyncio.sleep(1)
```

---

## 🌍 Version en ligne

Une version déployée est disponible sur :
🔗 [https://chinese-resto.vercel.app/](https://chinese-resto.vercel.app/)

---

## 🛠️ Développement & Contributions

Les contributions sont les bienvenues !
Veuillez créer une branche ou un fork pour proposer vos améliorations.

---

## 📝 Licence

Ce projet est sous licence MIT — voir le fichier `LICENSE` pour plus de détails.

```

Souhaites-tu aussi que je t’ajoute un badge de build ou un `Makefile` pour automatiser les commandes ?
```
