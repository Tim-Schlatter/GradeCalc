# GradeCalc
GradeCalc ist ein interaktives Konsolenprogramm zur Verwaltung und Berechnung von Schul- und Modulnoten<br>
Ein Python-Projekt der FHNW (Modul Grundlagen Programmierung)

## 🎯 Ziel des Projektes
Ziel von GradeCalc ist es, Noten strukturiert zu erfassen, zu speichern und verschiedene Berechnungen darauf durchzuführen.<br>
Das Programm verbindet grundlegende Programmierkonzepte wie Funktionen, Dateien, Fehlerbahandlung und Datenstrukturen.


## 🚀 Hauptfunktionen

- **Benutzerverwaltung (Login / Registrierung)**  
  Benutzer können sich registrieren und anmelden. Die Daten werden dauerhaft gespeichert.

- **Modulverwaltung**  
  Module können hinzugefügt und entfernt werden. Jedes Modul kann mehrere Noten enthalten.

- **Notenverwaltung**  
  Noten können zu Modulen hinzugefügt oder gelöscht werden.

- **Durchschnitt berechnen**  
  Berechnung des Notendurchschnitts eines Moduls:
  - ohne Gewichtung  
  - mit Gewichtung

- **Notenberechnung nach Punkten**  
  Berechnet die Schulnote anhand der erreichten und maximal möglichen Punkte.

- **Notenskala umrechnen**  
  Umrechnung der Schweizer Notenskala in:
  - Deutschland  
  - USA

---


## 🗂 Projektstruktur

```text
GradeCalc/
│
├── Main_programm.py                # Startpunkt des Programms (Hauptmenü)
├── User_menu.py                    # Menü für angemeldete Benutzer:innen
├── Anmelden.py                     # Login und Registrierung
├── ANSI.py                         # Farben und Textformatierung (UI)
│
├── Deine_Module.py                 # Anzeige und Verwaltung der Module
├── Modul_hinzufügen_entfernen.py   # Module hinzufügen / löschen
├── Noten_hinzufügen_entfernen.py   # Noten hinzufügen / löschen
│
├── durchschnitt_berechnen.py       # Durchschnittsberechnung
├── notenberechnung.py              # Berechnung der Note anhand von Punkten
├── notenskala.py                   # Umrechnung von Notenskalen
│
├── Datenbanken/
│   └── GradeCalc.json              # Speicherung der Benutzerdaten
│
├── README.md                       # Projektdokumentation
└── Notes.md                        # Ideen und mögliche Erweiterungen
```

## 🧑‍💻 Verwendung
1. Lade das Repository herunter:
   ```bash
   git clone https://github.com/Tim-Schlatter/GradeCalc.git

2. Programm starten
   ```
   python Main_programm.py

3. Menüanweisung im Terminal folgen


## 👥 Projektteam

Dieses Projekt wurde als Gruppenarbeit im Modul **Grundlagen Programmierung (FHNW)** erstellt.

- Tim Schlatter  
- Irfan Mahmuti
- Joselyn Cabrera






