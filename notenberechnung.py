def notenberechnung(user, pw):
    """
    Funktion für die Notenberechnung
    Man gibt eine Maximale Punktzahl sowie die Erreichte an. 
    Parameter sind für die Anmeldung nötig. 
    """
    from ANSI import Farben, Stil, farbig_center, clear
    print("\n", "="*50)
    print(farbig_center(f"{Farben.GRUEN}{Stil.KURSIV}Notenberechnung nach Punkten{Farben.RESET}", 50))
    print("="*50 + "\n")

    while True:
        try:
            max_points = float(input("Maximal mögliche Punktzahl: "))
            if max_points > 0: # Prüft ob die Maximale Punktzahl über 0 ist falls True wird die Schleife mit Break durchbrochen. 
                break
            print(f"{Farben.H_ROT}Gib eine Zahl über 0 ein!{Farben.RESET}\n")
        except ValueError:
            print(f"{Farben.H_ROT}Ungültige Eingabe: Bitte eine Zahl eingeben!{Farben.RESET}\n")

    while True:
        try:
            points = float(input("Erzielte Punktzahl: "))
            if points < 0:
                print(f"{Farben.H_ROT}Gib eine Zahl ≥ 0 ein!{Farben.RESET}\n")
                continue
            if points > max_points:
                print(f"{Farben.H_ROT}Erzielte Punkte dürfen nicht größer als die Maximalpunkte sein!{Farben.RESET}\n")
                continue
            break
        except ValueError:
            print(f"{Farben.H_ROT}Ungültige Eingabe: Bitte eine Zahl eingeben!{Farben.RESET}\n")


    # Errechnet die Note die man erhalten wird. 
    note = (points * 5 / max_points)+1

    # Gibt den Durchschnitt an. Rot = Ungenügend, Grün = Genügend 
    if note >= 1 and note <= 6:
        if note >= 4:
            print(f"\n{Farben.GRUEN}Sehr gut deine Note {Stil.FETT}{note:.2f}{Farben.RESET}{Farben.GRUEN} ist genügend!{Farben.RESET}\n")
        else:
            print(f"\n{Farben.ROT}Schade, deine Note {Stil.FETT}{note:.2f}{Farben.RESET}{Farben.ROT} ist ungenügend!{Farben.RESET}\n")

    while True:
        try:

            zurück = input("Zurück zum Hauptmenü? (j/n): ").lower()
            if zurück == "j":
                from main_menu import main_menu
                from user_menu import user_menu
                if user == 0 and pw == 0:
                    main_menu()
                    return
                else:
                    user_menu(user,pw)
                return
            if zurück == "n":
                from notenberechnung import notenberechnung
                notenberechnung(0,0)
                return
            else:
                print(f"{Farben.H_ROT}Ungültiger Buchstabe! Bitte (j/n) eingeben.{Farben.RESET}")
        except ValueError:
            print(f"{Farben.H_ROT}Ungültige Eingabe: Bitte (j/n) eingeben{Farben.RESET}")

