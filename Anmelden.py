from ANSI import Farben,Stil, farbig_center, clear
import json

def anmelden():
    

    #🟢 Erstellung des Menüs sowie Auswahl der Funktion
    print("="*50)
    print(farbig_center(f"{Farben.H_WEISS}{Stil.FETT}Anmelden und Registrieren{Farben.RESET}",50))
    print("="*50)
    print("\n1) Anmelden")
    print("2) Registrieren")
    print("3) Beenden")

    #🟢 Schleife zum überprüfen der Eingabe
    while True:  
        try:
            wahl = int(input("\nGib deine Gewünschte Funktion ein: "))
            if wahl == 1:
                anmeldung()
                return
            elif wahl == 2:
                registrierung()
                return
            elif wahl == 3:
                exit() #🛑 Noch prüfen
            else:
                print(f"\n{Farben.H_ROT}❌ Ungültige Zahl: Bitte eine Zahl von 1-3 eingeben!{Farben.RESET}")

        except ValueError:
            print(f"\n{Farben.H_ROT}❌ Ungültige Eingabe: Bitte eine Zahl von 1-3 eingeben!{Farben.RESET}")


def anmeldung():
    
    import os
    from User_menu import user_menu

    print("="*100)
    print(farbig_center(f"{Stil.FETT}{Farben.GRUEN}Wilkommen bei der Anmeldung{Farben.RESET}",100))
    print("="*100)

    dateipfad = os.path.join(os.path.dirname(__file__), "Datenbanken", "GradeCalc.json") # Weist Pfad zu

    while True:
        try:

            username = str(input("Username: "))
            passwort= str(input("Passwort: "))

            with open(dateipfad, "r",encoding="utf-8") as f:
                all_data = json.load(f)
            user_data = all_data[username]
            user_pw_data = user_data["password"]

            if passwort == user_pw_data:
                user_menu(username,passwort)
                return
            else: 
                print(f"{Farben.H_ROT}Ungültiges Passwort oder Username!{Farben.RESET}")
                continue
        except KeyError:
            print(f"{Farben.H_ROT}Ungültiges Passwort oder Username!{Farben.RESET}")
            continue


def registrierung():
    from Main_programm import main_menu
    import os
    from ANSI import Farben, Stil, farbig_center

    print("="*100)
    print(farbig_center(f"{Stil.FETT}{Farben.CYAN}Willkommen bei der Registrierung{Farben.RESET}",100))
    print("="*100)
    print()

    dateipfad = os.path.join(os.path.dirname(__file__), "Datenbanken", "GradeCalc.json") # Weist Pfad zu
    os.makedirs(os.path.dirname(dateipfad), exist_ok=True) # Ordner sicherstellen

    if not os.path.exists(dateipfad): # Wenn die Datei GradeCalc.json existiert ist gut sonst wird sie erstellt mit leererem Dictionary
        with open(dateipfad, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=4)

    with open(dateipfad, "r",encoding="utf-8") as f:
        all_data = json.load(f)
        names = []
        for name in all_data:
            names.append(name)

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
        break
    
    neuer_user = {
        user: {
            "password": pw,
            "module_noten": {
            }
            
        }
    }

    new_file = all_data | neuer_user

    with open(dateipfad, "w",encoding="utf-8")as f:
        json.dump(new_file,f, indent=4,ensure_ascii=False) # Schreibt den neuen Benutzer dazu. "indent" = Steuert die Einrückung (also das Layout / die Lesbarkeit) in der JSON-Datei.
    
    print(f"\n{Farben.GRUEN}Gratulation! Dein Konto wurde erstellt!{Farben.RESET}")

    main_menu()







