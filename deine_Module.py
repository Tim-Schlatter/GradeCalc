def deine_module(username,password):
    """
    Zeigt die Module des angemeldeten Benutzers an und ermöglicht die Verwaltung der Noten.

    Der Benutzer kann:
    - ein Modul auswählen und die Noten ansehen
    - Noten hinzufügen oder entfernen
    - ein Modul entfernen
    - zurück ins User-Menü wechseln

    Die Funktion lädt die Moduldaten des Users aus der JSON-Datei und validiert alle Eingaben,
    damit das Programm bei Fehleingaben nicht abstürzt.

    Parameter:
        username (str): Benutzername des aktuell angemeldeten Benutzers.
        password (str): Passwort des aktuell angemeldeten Benutzers (wird fürs Zurückspringen ins User-Menü weitergegeben).

    Rückgabewert:
        None
    """
    from ANSI import Farben,Stil,farbig_center,clear
    from user_menu import user_menu
    from noten_hinzufügen_entfernen import note_hinzufügen,note_entfernen
    from modul_hinzufügen_entfernen import modul_entfernen
    import os
    import json

    # Outer-Loop, damit "Zurück" ohne Rekursion wieder zur Modulliste springt
    while True:
        print("="*50)
        print(farbig_center(f"{Stil.FETT}{Farben.CYAN}Deine Module{Farben.RESET}",50))
        print(farbig_center(f"{Stil.KURSIV}User: {username.capitalize()}{Farben.RESET}",50))
        print("="*50)
        print()

        # Pfad zur JSON-Datenbank bestimmen (Projektordner → Datenbanken → GradeCalc.json)
        dateipfad = os.path.join(os.path.dirname(__file__), "Datenbanken", "GradeCalc.json") # Weist Pfad zu

        # JSON-Datei laden (enthält alle User inkl. Module/Noten)
        with open(dateipfad, "r",encoding="utf-8") as f:
            all_data = json.load(f)

        # Nur die Module/Noten des aktuellen Benutzers herausziehen
        user__module_daten = all_data[username]["module_noten"]

        # Module nummeriert ausgeben
        anzahl = 0
        for i, fach in enumerate(user__module_daten, start=1):
            print(f"{i}) {fach.capitalize()}", end=" "*10)
            anzahl += 1

        # Wenn noch keine Module existieren, nicht ins Auswahl-Menü laufen
        if anzahl == 0:
            print(f"\n{Farben.H_ROT}Du hast noch keine Module. Füge zuerst ein Modul hinzu.{Farben.RESET}")
            user_menu(username,password)
            return
        
        # Eingabeschleife für Modulauswahl (wiederholt sich bei ungültiger Eingabe)
        while True:
            wahl = input("\n\nWähle dein Modul / 'x' für zurück: ").strip().lower()

            # Zurück ins User-Menü
            if wahl == "x":
                user_menu(username,password)
                return

            # int(...) erst nach Digit-Check (sonst ValueError)
            if not wahl.isdigit():
                print(f"{Farben.H_ROT}Ungültige Eingabe! Gib eine Zahl (1-{anzahl}) oder 'x' ein.{Farben.RESET}")
                continue
            
            # Umwandlung ist jetzt sicher, weil wahl nur aus Ziffern besteht
            wahl_int = int(wahl)  # nur noch hier int()
            if 1 <= wahl_int <= anzahl:
                break
            else:
                print(f"{Farben.H_ROT}Ungültige Eingabe! Gib eine Zahl (1-{anzahl}) oder 'x' ein.{Farben.RESET}")
                continue
        # Aus der Nummer das richtige Modul bestimmen
        try:
            wahl_index = int(wahl) - 1
            modul = list(user__module_daten.keys())[wahl_index]
        except (ValueError, IndexError):
            # Falls irgendwas schief geht (sollte durch Validierung selten passieren)
            print(f"{Farben.H_ROT}Ungültige Eingabe – Modul existiert nicht!{Farben.RESET}")
            return

        # Neues „Noten-Detail-Menü“ anzeigen
        clear()
        print("="*50)
        print(farbig_center(f"{Stil.FETT}Noten: {modul.capitalize()}{Farben.RESET} ",50))
        print(farbig_center(f"User: {username.capitalize()}",50))
        print("="*50)
        print()

        # Noten des ausgewählten Moduls auslesen und anzeigen
        noten = user__module_daten[modul]
        anzahl_noten = 0
        summe = 0
        for i,note in enumerate(noten):
            print(f"Prüfung {i+1}: {note}")
            anzahl_noten += 1
            summe += note

        # Durchschnitt nur berechnen, wenn mindestens eine Note existiert
        print()
        if len(noten) >= 1:
            durchschnitt = summe/anzahl_noten
            if durchschnitt >=4:
                print(f"{Farben.H_GRUEN}Dein Durchschnitt: {durchschnitt:.2f} ist genügend!{Farben.RESET}")
            else:
                print(f"{Farben.H_ROT}Dein Durchschnitt: {durchschnitt:.2f} ist ungenügend!{Farben.RESET}")

        # Menü für Aktionen im ausgewählten Modul
        while True:
            print("-"*50)
            print("1) Note hinzufügen")
            print("2) Note entfernen")
            print("3) Modul entfernen")
            print("4) Zurück")
            try:
                wahl = int(input("Wähle deine Funktion: "))
            except ValueError:
                # Änderung: verhindert Absturz und fragt erneut
                print(f"{Farben.H_ROT}Ungültige Eingabe: Gib eine Zahl von 1-4 ein!{Farben.RESET}")
                continue  # Änderung: sonst wäre 'wahl' nicht gesetzt (UnboundLocalError)

            if wahl < 1 or wahl > 4:
                print(f"{Farben.H_ROT}Ungültige Eingabe: Gib eine Zahl von 1-4 ein!{Farben.RESET}")
                continue
            break
        
        # Auswahl ausführen
        if wahl == 1:
            note_hinzufügen(username,password,modul)
            return # nach der Aktion zurück (die aufgerufene Funktion steuert dann das Menü)

        if wahl == 2:
            note_entfernen(username,password,modul)
            return

        if wahl == 3:
            modul_entfernen(username,password,modul)
            return

        if wahl == 4:
            clear()
            # Änderung: zurück zur Modulliste ohne Rekursion (Sich selbst wiederholt)
            continue
