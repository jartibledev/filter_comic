# [:uk:](README_EN.md) [:de:](README_DE.md) [:es:](README.md)
### 📝 Description
Il s'agit d'un plugin écrit en Python-Fu pour GIMP 3.0. Il automatise un flux de travail de retouche d'image spécifique en effectuant les étapes suivantes en un seul clic :
* Copie le calque de base et applique l'effet Peinture à l'huile (GEGL Oilify).
* Crée une deuxième copie du calque et modifie son mode de fusion sur Multiplier.
* Crée une troisième copie, la désature (mode luminosité), la met en mode Multiplier et applique un filtre de Seuil.

### ⚙️ Installation
1. Copiez le fichier `gimp-tutorial-plug-in.py` dans votre répertoire de plugins GIMP 3 (par exemple : `~/.config/GIMP/3.0/plug-ins/`).
2. Assurez-vous que le fichier dispose des autorisations d'exécution (sur Linux/macOS : `chmod +x gimp-tutorial-plug-in.py`).
3. Redémarrez GIMP.

### 🚀 Utilisation
1. Ouvrez n'importe quelle image dans GIMP.
2. Dans le menu supérieur, allez dans **Filtres > Automatization**.
3. Profitez du résultat !