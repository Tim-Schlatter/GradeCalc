def deine_module(username,password):
    from ANSI import Farben,Stil,farbig_center,clear
    from User_menu import user_menu
    from Noten_hinzufügen_entfernen import note_hinzufügen,note_entfernen
    from Modul_hinzufügen_entfernen import modul_entfernen
    import os
    import json

    # ✅ Änderung: Outer-Loop, damit "Zurück" ohne Rekursion wieder zur Modulliste springt
    while True:
        print("="*100)
        print(farbig_center(f"{Stil.FETT}{Farben.CYAN}Deine Module{Farben.RESET}",100))
        print(farbig_center(f"{Stil.KURSIV}User: {username.capitalize()}{Farben.RESET}",100))
        print("="*100)
        print()

        dateipfad = os.path.join(os.path.dirname(__file__), "Datenbanken", "GradeCalc.json") # Weist Pfad zu

        with open(dateipfad, "r",encoding="utf-8") as f:
            all_data = json.load(f)

        user__module_daten = all_data[username]["module_noten"]

        anzahl = 0
        for i, fach in enumerate(user__module_daten, start=1):
            print(f"{i}) {fach.capitalize()}", end=" "*10)
            anzahl += 1

        # ✅ Änderung: Wenn noch keine Module existieren, nicht ins Auswahl-Menü laufen
        if anzahl == 0:
            print(f"\n{Farben.H_ROT}Du hast noch keine Module. Füge zuerst ein Modul hinzu.{Farben.RESET}")
            user_menu(username,password)
            return

        while True:
            wahl = input("\n\nWähle dein Modul / 'x' für zurück: ").strip().lower()

            if wahl == "x":
                user_menu(username,password)
                return

            # ✅ Änderung: int(...) erst nach Digit-Check (sonst ValueError)
            if not wahl.isdigit():
                print(f"{Farben.H_ROT}Ungültige Eingabe! Gib eine Zahl (1-{anzahl}) oder 'x' ein.{Farben.RESET}")
                continue

            wahl_int = int(wahl)  # ✅ Änderung: nur noch hier int()
            if 1 <= wahl_int <= anzahl:
                break
            else:
                print(f"{Farben.H_ROT}Ungültige Eingabe! Gib eine Zahl (1-{anzahl}) oder 'x' ein.{Farben.RESET}")
                continue

        try:
            wahl_index = int(wahl) - 1
            modul = list(user__module_daten.keys())[wahl_index]
        except (ValueError, IndexError):
            print(f"{Farben.H_ROT}Ungültige Eingabe – Modul existiert nicht!{Farben.RESET}")
            return

        clear()
        print(modul)
        print("="*100)
        print(farbig_center(f"{Stil.FETT}Noten: {modul.capitalize()}{Farben.RESET} ",100))
        print(farbig_center(f"User: {username.capitalize()}",100))
        print("="*100)
        print()

        noten = user__module_daten[modul]
        anzahl_noten = 0
        summe = 0
        for i,note in enumerate(noten):
            print(f"Prüfung {i+1}: {note}")
            anzahl_noten += 1
            summe += note

        print()
        if len(noten) >= 1:
            durchschnitt = summe/anzahl_noten
            if durchschnitt >=4:
                print(f"{Farben.H_GRUEN}Dein Durchschnitt: {durchschnitt:.2f} ist genügend!{Farben.RESET}")
            else:
                print(f"{Farben.H_ROT}Dein Durchschnitt: {durchschnitt:.2f} ist ungenügend!{Farben.RESET}")

        while True:
            print("-"*100)
            print("1) Note hinzufügen")
            print("2) Note entfernen")
            print("3) Modul entfernen")
            print("4) Zurück")
            try:
                wahl = int(input("Wähle deine Funktion: "))
            except ValueError:
                print(f"{Farben.H_ROT}Ungültige Eingabe: Gib eine Zahl von 1-4 ein!{Farben.RESET}")
                continue  # ✅ Änderung: sonst wäre 'wahl' nicht gesetzt (UnboundLocalError)

            if wahl < 1 or wahl > 4:
                print(f"{Farben.H_ROT}Ungültige Eingabe: Gib eine Zahl von 1-4 ein!{Farben.RESET}")
                continue
            break

        if wahl == 1:
            note_hinzufügen(username,password,modul)
            return

        if wahl == 2:
            note_entfernen(username,password,modul)
            return

        if wahl == 3:
            modul_entfernen(username,password,modul)
            return

        if wahl == 4:
            clear()
            # ✅ Änderung: zurück zur Modulliste ohne Rekursion
            continue
