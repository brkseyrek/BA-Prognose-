
#Prognose-Anwendung

Diese Anwendung ist ein web-basiertes Prognose-Tool, das mit Flask (Backend), einer OpenAI GPT-4o-API und mehreren Query-Engines arbeitet, um Benutzern Vorhersagen und Berechnungen basierend auf CSV-Daten zu bieten. Die Anwendung kombiniert NLP-Funktionen mit verschiedenen Datensätzen, um Benutzern spezifische Antworten und Vorhersagen zu liefern.

Wenn Sie lediglich die Anwendung ausprobieren möchten, ohne sie zu installieren können sie dies über diesen Link tun:

```bash
  https://useless-koi-prognose-anwendung-e92ffb25.koyeb.app/
 
```
## Technologien

**Flask:** Web-Framework für die Erstellung des Backends und Routing.

**OpenAI GPT-4o API:** Verwendet für natürliche Sprachverarbeitung und Beantwortung von Anfragen.

**Pandas:** Datenverarbeitung und Ausführung von Abfragen auf CSV-Datensätzen.

**LlamaIndex:** Verwaltung von Query-Engines für den Zugriff auf unterschiedliche Datenquellen.

**HTML/CSS/JavaScript:** Für die Frontend-Interaktionen mit dem Benutzer.

**Jinja2:** Rendering von dynamischen HTML-Templates.

**dotenv:** Laden von Umgebungsvariablen, wie API-Schlüsseln.



## Installation

1.Klonen des Repository:

```bash
  git clone https://github.com/brkseyrek/BA-Prognose_Anwendung/
  cd RAG
```
2.Erstelle eine virtuelle Umgebung:

```bash
  python3 -m venv venv
  source venv/bin/activate  # Für Linux/Mac
  # oder
  venv\Scripts\activate  # Für Windows
```
3.Installiere Abhängigkeiten:
```bash
  pip install -r requirements.txt

```
4.Umgebungsvariablen konfigurieren: Erstelle eine .env-Datei und füge deinen OpenAI API-Schlüssel hinzu:
```bash
  OPENAI_API_KEY=dein_openai_api_schluessel

```
5.CSV-Dateien vorbereiten: Stellen Sie sicher, dass die entsprechenden CSV-Dateien im Ordner csv/ gespeichert sind. Die Dateien sollten in den Query-Engines in main.py korrekt referenziert werden.


## Konfiguration

- Umgebungsvariablen: In der .env-Datei müssen folgende Variablen definiert sein:
    - OPENAI_API_KEY: Dein API-Schlüssel für den Zugriff auf die GPT-4o-API.
- Datenquellen: Die CSV-Dateien, auf die die Query Engines zugreifen, sollten in einem Ordner csv/ im Projekt gespeichert werden. Die Dateipfade sind im Code in main.py definiert.

## Verwendung

1.Starte die Anwendung:
```bash
  flask run
```

2.Zugriff auf die Anwendung: Öffne deinen Webbrowser und gehe zu:
```bash
 http://127.0.0.1:5000
```

3.Interaktionen:
- Profilseite: Benutzer können ihre persönliche Beschreibung eingeben, die bei zukünftigen Anfragen verwendet wird.
- Anfragen stellen: Benutzer können Anfragen auf der Startseite eingeben. Die Anwendung verarbeitet die Anfragen und gibt Antworten oder Vorhersagen zurück, basierend auf den Datensätzen und dem Modell.
## Features

- Natürliche Sprachverarbeitung: Verwendet die GPT-4o-API, um Benutzeranfragen zu verstehen und Antworten zu generieren.
- Datenbasierte Prognosen: Nutzt mehrere CSV-Datensätze, um spezifische Anfragen zu bearbeiten (z.B. Horoskop, Verkehrsunfälle, Lebenserwartung).
- Sitzungsbasiertes Benutzerprofil: Speichert die Benutzerbeschreibung, um die Ergebnisse zu personalisieren.
- Dynamische HTML-Templates: Verwendung von Jinja2 zur Darstellung dynamischer Inhalte im Frontend.

