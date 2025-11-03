

def durchschnitt_berechnen(user,pw):
    from ANSI import Farben, Stil, farbig_center, clear


    print("=" * 50)
    print(farbig_center(f"{Farben.BLAU}{Stil.FETT}Durchschnitts Berechner{Farben.RESET}", 50))
    print("=" * 50)
    print("\n1) Normal")
    print("2) Mit Gewichtung\n")
    while True:
        try:
            wahl = int(input("Wähle deine Funktion: "))
            if wahl == 1:
                normal(user,pw)
                return
            elif wahl == 2:
                gewichtung(user, pw)
                return
            else:
                print(f"\n{Farben.H_ROT}Gib eine Zahl zwischen 1-2 ein!{Farben.RESET}\n")
        except ValueError:
            print(f"\n{Farben.H_ROT}Ungültige Eingabe! Bitte eine ganze Zahl eingeben.{Farben.RESET}\n")

def gewichtung(user, pw):
    from ANSI import Farben, Stil, farbig_center,clear

    
    print("="*50)
    print(farbig_center(f"{Farben.BLAU}{Stil.FETT}Durchschnitts Berechner{Farben.RESET}", 50))
    print(farbig_center(f"{Stil.KURSIV}Mit Gewichtung{Farben.RESET}", 50))
    print("="*50)
    
    while True:
        try:
            anzahl = int(input("\nAnzahl der Noten: "))
            if anzahl > 0:
                break
            print(f"\n{Farben.H_ROT}Bitte > 0 eingeben.{Farben.RESET}")
        except ValueError:
            print(f"\n{Farben.H_ROT}Ungültige Eingabe! Bitte eine ganze Zahl eingeben.{Farben.RESET}")

    noten_summe = 0
    gewichtung_summe = 0

    for i in range(anzahl):

        while True:
            try:
                note = float(input(f"Note {i+1}: "))
                if 1 <= note <= 6:
                    break
                print(f"\n{Farben.H_ROT}Ungültig; Zahl zwischen 1-6 eingeben.{Farben.RESET}\n")
            except ValueError:
                print(f"\n{Farben.H_ROT}Bitte eine Zahl eingeben.{Farben.RESET}\n")

        while True:
            try:
                gewichtung = float(input(f"Gewichtung Note {i+1} (%): "))
                if 1 <= gewichtung <= 100:
                    gewichtung = gewichtung/100
                    break
                print(f"\n{Farben.H_ROT}Ungültig: Zahl zwischen 1-100 eingeben.{Farben.RESET}\n")
            except ValueError:
                print(f"\n{Farben.H_ROT}Bitte eine Zahl eingeben / Die Prozenzahl ohne % schreiben.{Farben.RESET}\n")



        noten_summe += note*gewichtung
        gewichtung_summe += gewichtung

        # Durchschnitt berechnen
    durchschnitt = noten_summe / gewichtung_summe
    if durchschnitt >= 4:
        print(f"\n{Farben.H_GRUEN}Dein Durchschnitt ist: {durchschnitt:.2f}{Farben.RESET}\n")
    else:
        print(f"\n{Farben.H_ROT}Dein Durchschnitt ist: {durchschnitt:.2f}{Farben.RESET}\n")

    while True:
        try:

            zurück = input("Zurück zum Hauptmenü? (j/n): ").lower()
            if zurück == "j":
                from Main_programm import main_menu
                from User_menu import user_menu
                if user == 0 and pw == 0:
                    main_menu()
                    return
                else:
                    user_menu(user,pw)
                    return
            if zurück == "n":
                from durchschnitt_berechnen import durchschnitt_berechnen
                durchschnitt_berechnen(user,pw)
                return
            else:
                print(f"{Farben.H_ROT}Ungültiger Buchstabe! Bitte (j/n) eingeben.{Farben.RESET}")
        except ValueError:
            print(f"{Farben.H_ROT}Ungültige Eingabe: Bitte (j/n) eingeben{Farben.RESET}")

def normal(user,pw):
    from ANSI import Farben, Stil, farbig_center, clear

    print("="*50)
    print(farbig_center(f"{Farben.BLAU}{Stil.FETT}Durchschnitts Berechner{Farben.RESET}", 50))
    print(farbig_center(f"{Stil.KURSIV}Ohne Gewichtung{Farben.RESET}", 50))
    print("="*50)
    noten_summe = 0
        # Eingabe wiederholen bis gültige Zahl
    while True:
        try:
            anzahl = int(input("\nAnzahl der Noten: "))
            if anzahl <= 0:
                print(f"\n{Farben.H_ROT}Bitte eine Zahl größer als 0 eingeben.{Farben.RESET}")
            else:
                break  # gültige Zahl → Schleife beenden
        except ValueError:
            print(f"\n{Farben.H_ROT}Ungültige Eingabe! Bitte eine ganze Zahl eingeben.{Farben.RESET}")

        # Eingabe der Noten
    for i in range(anzahl):
        while True:
            try:
                note = float(input(f"\nNote {i + 1}: "))
                if 1 <= note <= 6:
                    noten_summe += note
                    break  # gültig → nächste Note
                else:
                    print(f"\n{Farben.H_ROT}Ungültige Note! Bitte Zahl zwischen 1 und 6 eingeben.{Farben.RESET}")
            except ValueError:
                print(f"\n{Farben.H_ROT}Ungültige Eingabe! Bitte eine Zahl eingeben.{Farben.RESET}")

        # Durchschnitt berechnen
    durchschnitt = noten_summe / anzahl
    if durchschnitt >= 4:
        print(f"\n{Farben.H_GRUEN}Dein Durchschnitt ist: {durchschnitt:.2f}{Farben.RESET}\n")

    else:
        print(f"\n{Farben.H_ROT}Dein Durchschnitt ist: {durchschnitt:.2f}{Farben.RESET}\n")

    while True:
        try:

            zurück = input("Zurück zum Hauptmenü? (j/n): ").lower()
            if zurück == "j":
                from Main_programm import main_menu
                from User_menu import user_menu
                if user == 0 and pw == 0:
                    main_menu()
                    return
                else:
                    user_menu(user,pw)
                return
            if zurück == "n":
                from durchschnitt_berechnen import durchschnitt_berechnen
                durchschnitt_berechnen(user,pw)
                return
            else:
                print(f"{Farben.H_ROT}Ungültiger Buchstabe! Bitte (j/n) eingeben.{Farben.RESET}")
        except ValueError:
            print(f"{Farben.H_ROT}Ungültige Eingabe: Bitte (j/n) eingeben{Farben.RESET}")







