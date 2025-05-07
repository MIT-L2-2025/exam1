const cors = require('cors');
const express = require('express');
const fs = require('fs');
const app = express();
app.use(cors());
const PORT = 3000;

app.get('/restaurants', (req, res) => {
  fs.readFile('../data.json', 'utf8', (err, data) => {
    if (err) {
      return res.status(500).json({ error: 'Erreur de lecture du fichier' });
    }
    res.json(JSON.parse(data));
  });
});

app.listen(PORT, () => {
  console.log(`API dispo sur http://localhost:${PORT}/restaurants`);
});
