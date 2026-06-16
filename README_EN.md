# [:fr:](README_FR.md)   [:de:](README_DE.md)   [:es:](README.md)
# Comic pages filter
### 📝 Description
This is a Python-Fu plugin developed for GIMP 3.0. It automates a specific image editing workflow by performing the following steps with a single click:
* Copies the base layer and applies the GEGL Oilify effect.
* Creates a second copy of the layer and sets its blend mode to Multiply.
* Creates a third copy, desaturates it (luminosity mode), sets it to Multiply mode, and applies a Threshold filter.

### ⚙️ Installation
1. Copy the `gimp-tutorial-plug-in.py` file to your GIMP 3 plug-ins directory (e.g., `~/.config/GIMP/3.0/plug-ins/`).
2. Ensure the script has execution permissions (on Linux/macOS: `chmod +x gimp-tutorial-plug-in.py`).
3. Restart GIMP.

### 🚀 Usage
1. Open any image in GIMP.
2. In the top menu, navigate to **Filters > Automatization**.