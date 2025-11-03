def user_menu(username,password):
    from ANSI import Farben,Stil,farbig_center,clear
    from durchschnitt_berechnen import durchschnitt_berechnen
    from notenberechnung import notenberechnung
    from notenskala import notenskala
    from Deine_Module import deine_module
    from Modul_hinzufügen_entfernen import modul_hinzufügen
    import sys
    
    print("="*50)
    print(farbig_center(f"{Stil.FETT}HAUPTMENÜ GradeCalc{Farben.RESET}", 50))
    print(farbig_center(f"{Stil.KURSIV}Wilkommen {username.capitalize()}{Farben.RESET}", 50))
    print("="*50)
    print()
    print("1) Deine Module")
    print("2) Module hinzufügen")
    print("3) Durchschnitt berechnen")
    print("4) Notenberechnung nach Punkten")
    print("5) Notenskala umrechner")
    print("6) Beenden!")

    while True:
        try:
            wahl = int(input("Wähle deine Funktion (1-6): "))
            if wahl > 6 or wahl < 1:
                print(f"{Farben.H_ROT}Ungültige Eingabe: Wähle eine Zahl zwischen (1-6)!{Farben.RESET}")
                continue
            else:
                break

        except ValueError:
            print(f"{Farben.H_ROT}Ungültige Eingabe: Wähle eine Zahl zwischen (1-6)!{Farben.RESET}")
    
    if wahl == 1:
        deine_module(username, password)
        return
    if wahl == 2:
        modul_hinzufügen(username,password)
        return
    if wahl == 3: 
        durchschnitt_berechnen(username,password)
        return
    if wahl == 4:
        notenberechnung(username,password)
        return
    if wahl == 5:
        notenskala(username,password)
        return
    if wahl == 6:
        print("Programm beendet!\n")
        sys.exit()

