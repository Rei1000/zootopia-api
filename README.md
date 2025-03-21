# Zootopia API Web Generator

## English

### Project Description
This project is a simple web generator that fetches animal information from an external API and generates an HTML page displaying the results. It allows users to search for animals dynamically and handles cases where no results are found.

### Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/Rei1000/zootopia-api
   cd zootopia-api
   ```
2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up the API key:
   - Create a `.env` file in the project root and add your API key:
     ```sh
     API_KEY="your_api_key_here"
     ```

### Usage
1. Run the script:
   ```sh
   python animals_web_generator.py
   ```
2. Enter the name of an animal when prompted.
3. The generated HTML file (`animals.html`) will display the animal information.
4. If no data is found, a message will be shown instead.

### Project Structure
- `animals_web_generator.py` - Main script to fetch data and generate HTML
- `data_fetcher.py` - Handles API requests
- `.env` - Stores the API key (excluded from Git)
- `requirements.txt` - Lists dependencies
- `animals_template.html` - HTML template
- `animals.html` - Generated website

### API Source
This project retrieves data from [API Ninjas - Animals](https://api-ninjas.com/api/animals).

## Credits
Many thanks to Masterschool for offering these valuable tasks that helped structure this project!
---

## Deutsch

### Projektbeschreibung
Dieses Projekt ist ein einfacher Web-Generator, der Tierinformationen von einer externen API abruft und eine HTML-Seite generiert, die die Ergebnisse anzeigt. Benutzer können nach Tieren suchen, und das Programm behandelt Fälle, in denen keine Ergebnisse gefunden werden.

### Installation
1. Klone dieses Repository:
   ```sh
   git clone https://github.com/Rei1000/zootopia-api
   cd zootopia-api
   ```
2. Installiere die Abhängigkeiten:
   ```sh
   pip install -r requirements.txt
   ```
3. API-Schlüssel einrichten:
   - Erstelle eine `.env` Datei im Projektverzeichnis und füge deinen API-Schlüssel hinzu:
     ```sh
     API_KEY="dein_api_schluessel"
     ```

### Nutzung
1. Führe das Skript aus:
   ```sh
   python animals_web_generator.py
   ```
2. Gib den Namen eines Tieres ein, wenn du dazu aufgefordert wirst.
3. Die generierte HTML-Datei (`animals.html`) zeigt die Tierinformationen an.
4. Falls keine Daten gefunden werden, erscheint eine entsprechende Meldung.

### Projektstruktur
- `animals_web_generator.py` - Hauptskript zum Abrufen von Daten und Generieren von HTML
- `data_fetcher.py` - Verantwortlich für API-Anfragen
- `.env` - Speichert den API-Schlüssel (von Git ausgeschlossen)
- `requirements.txt` - Listet die Abhängigkeiten auf
- `animals_template.html` - HTML-Vorlage
- `animals.html` - Generierte Webseite

### API-Quelle
Dieses Projekt ruft Daten von [API Ninjas - Animals](https://api-ninjas.com/api/animals) ab.

---

## Credits

Vielen Dank an Masterschool für die Bereitstellung dieser wertvollen Aufgaben, die zur Strukturierung dieses Projekts beigetragen haben!
