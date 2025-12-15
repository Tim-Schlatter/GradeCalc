from ANSI import Farben,Stil, farbig_center, clear

import json
import sys

def anmelden():
    """
    Zeigt das Anmelde- und Registrierungsmenü an und verarbeitet die Benutzerauswahl.

    Der Benutzer kann:
    1) sich anmelden
    2) sich registrieren
    3) das Programm beenden

    Die Funktion prüft die Benutzereingaben und ruft je nach Auswahl
    die entsprechende Funktion auf.
    """
    clear()
    # Schleife zum überprüfen der Eingabe. Input für welche Funktion man sich entscheidet
    while True:
        print("="*50)
        print(farbig_center(f"{Farben.H_WEISS}{Stil.FETT}Anmelden und Registrieren{Farben.RESET}",50))
        print("="*50)
        print("\n1) Anmelden")
        print("2) Registrieren")
        print("3) Beenden")

    
        try:
            wahl = int(input("\nGib deine Gewünschte Funktion ein: "))
            if wahl == 1:
                anmeldung()          
                continue
            elif wahl == 2:
                registrierung()
                continue
            elif wahl == 3:
                sys.exit()
            else:
                print(f"\n{Farben.H_ROT}❌ Ungültige Zahl: Bitte 1-3 eingeben!{Farben.RESET}")
                input("Enter...")
        except ValueError:
            print(f"\n{Farben.H_ROT}❌ Ungültige Eingabe: Bitte 1-3 eingeben!{Farben.RESET}")
            input("Enter...")


def anmeldung():
    """
    Führt die Benutzeranmeldung durch.

    Die Funktion fordert den Benutzer zur Eingabe von Username und Passwort auf,
    lädt die gespeicherten Benutzerdaten aus der JSON-Datei und überprüft,
    ob die eingegebenen Zugangsdaten korrekt sind.

    Bei erfolgreicher Anmeldung wird das User-Menü geöffnet.
    Bei falschen Zugangsdaten wird eine Fehlermeldung ausgegeben und
    die Eingabe erneut abgefragt.
    """
    import os
    from user_menu import user_menu

    # Anzeige des Anmelde-Headers
    print("="*50)
    print(farbig_center(f"{Stil.FETT}{Farben.GRUEN}Wilkommen bei der Anmeldung{Farben.RESET}",50))
    print("="*50)

    # Ermittlung des Dateipfads zur JSON-Datenbank
    # __file__ → aktueller Speicherort der Datei
    dateipfad = os.path.join(os.path.dirname(__file__), "Datenbanken", "GradeCalc.json") 

    # Schleife zur wiederholten Eingabe bei falschen Zugangsdaten. 
    while True:
        try:

            username = str(input("Username: "))
            passwort= str(input("Passwort: "))

            # Laden der gespeicherten Benutzerdaten aus der JSON-Datei
            with open(dateipfad, "r",encoding="utf-8") as f:
                all_data = json.load(f)
            # Zugriff auf die Daten des eingegebenen Benutzers
            user_data = all_data[username]
            user_pw_data = user_data["password"]
            # Überprüfung des Passworts
            if passwort == user_pw_data:
                user_menu(username,passwort)
                return
            else: 
                print(f"{Farben.H_ROT}Ungültiges Passwort oder Username!{Farben.RESET}")
                continue
        except KeyError:
            print(f"{Farben.H_ROT}Ungültiges Passwort oder Username!{Farben.RESET}")
            continue
        except FileNotFoundError:
            print(f"{Farben.H_ROT}Keine Datenbank gefunden. Bitte zuerst registrieren{Farben.RESET}")
            return


def registrierung():
    """
    Führt die Benutzerregistrierung durch.

    Die Funktion ermöglicht es einem neuen Benutzer, ein Konto zu erstellen.
    Dabei wird überprüft, ob der Benutzername bereits existiert und ob
    Benutzername sowie Passwort die Mindestanforderungen erfüllen.

    Nach erfolgreicher Registrierung werden die Benutzerdaten in der
    JSON-Datei gespeichert und der Benutzer zurück ins Hauptmenü geleitet.
    """
    from main_menu import main_menu
    import os
    from ANSI import Farben, Stil, farbig_center

    # Anzeige des Registrierungs-Headers
    print("="*50)
    print(farbig_center(f"{Stil.FETT}{Farben.CYAN}Willkommen bei der Registrierung{Farben.RESET}",50))
    print("="*50)
    print()

    # Pfad zur JSON-Datenbank bestimmen
    dateipfad = os.path.join(os.path.dirname(__file__), "Datenbanken", "GradeCalc.json") 
    os.makedirs(os.path.dirname(dateipfad), exist_ok=True) # Ordner sicherstellen

    if not os.path.exists(dateipfad): # Wenn die Datei GradeCalc.json existiert ist gut sonst wird sie erstellt mit leererem Dictionary
        with open(dateipfad, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=4)

    # Laden aller bestehenden Benutzerdaten
    with open(dateipfad, "r",encoding="utf-8") as f:
        all_data = json.load(f)

        # Liste aller vorhandenen Benutzernamen erstellen
        names = []
        for name in all_data:
            names.append(name)

    # Schleife zur Eingabe und Überprüfung der Registrierungsdaten sowie Prüfung der Mindestanforderung für Username und Passwort
    while True: 
        user = str(input("Username: ")).lower()
        if len(user) < 3:
            print(f"{Farben.H_ROT}Ungültige Eingabe: Username muss mehr als 2 Zeichen haben!{Farben.RESET}")
            continue
        if user in names:
            print(f"{Farben.H_ROT}Ungültige Eingabe: Username ist bereits vergeben!{Farben.RESET}")
            continue
        pw = str(input("Passwort: "))
        if len(pw) < 8:
            print(f"{Farben.H_ROT}Ungültige Eingabe: Passwort muss mehr als 7 Zeichen haben!{Farben.RESET}")
            continue
        break # Eingabe Gültig die Schleife wird verlassen

    # Neuer Benutzer wird als Dictionary vorbereitet
    neuer_user = {
        user: {
            "password": pw,
            "module_noten": {
            }
            
        }
    }

    # Zusammenführen der bestehenden Daten mit dem neuen Benutzer
    # "|" = Dictionary Merge
    new_file = all_data | neuer_user
    
    # Speichern der aktualisierten Daten in der JSON-Datei
    with open(dateipfad, "w",encoding="utf-8")as f:
        json.dump(new_file,f, indent=4,ensure_ascii=False) # Schreibt den neuen Benutzer dazu. "indent" = Steuert die Einrückung (also das Layout / die Lesbarkeit) in der JSON-Datei.
    
    print(f"\n{Farben.GRUEN}Gratulation! Dein Konto wurde erstellt!{Farben.RESET}")

    main_menu()







