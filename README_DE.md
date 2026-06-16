# [:uk:](README_EN.md)   [:fr:](README_FR.md)   [:es:](README.md)
# Comic pages filter
### 📝 Beschreibung
Dies ist ein in Python-Fu geschriebenes Plugin für GIMP 3.0. Es automatisiert einen spezifischen Bildbearbeitungs-Workflow, indem es die folgenden Schritte mit einem einzigen Klick ausführt:
* Kopiert die Basisebene und wendet den Ölgemälde-Effekt (GEGL Oilify) an.
* Erstellt eine zweite Kopie der Ebene und ändert den Ebenenmodus auf Multiplizieren.
* Erstellt eine dritte Kopie, entsättigt sie (Luminanz-Modus), setzt sie auf Multiplizieren und wendet einen Schwellenwert-Filter an.
|  |   
| --- | --- | 
| ![Fotografía sin editar](./images/IMG_7417.webp) | ![Fotografía editada](./imagenes/page_1.webp) | 
| Unbearbeitetes Foto | Bearbeitetes Foto | 

### ⚙️ Installation
1. Kopieren Sie die Datei `gimp-tutorial-plug-in.py` in Ihr GIMP 3 Plug-ins-Verzeichnis (z. B.: `~/.config/GIMP/3.0/plug-ins/`).
2. Stellen Sie sicher, dass die Datei Ausführungsrechte hat (unter Linux/macOS: `chmod +x gimp-tutorial-plug-in.py`).
3. Starten Sie GIMP neu.

### 🚀 Verwendung
1. Öffnen Sie ein beliebiges Bild in GIMP.
2. Navigieren Sie im oberen Menü zu **Filter > Automatization**.
3. Genießen Sie das Ergebnis!