from ANSI import Farben, Stil, farbig_center, clear

def notenskala(user,pw):
    """
    Funktion für das Umrechnen einer Note in eine andere Notenskala
    Umrechnen in DE-Note und USA-Note von CH-Note aus möglich
    Parameter sind für die Anmeldung nötig. 
    """
    def deutschland(user,pw):
        """
        Funktion für das Umrechnen von CH-Note in die Notenskala von Deutschland
        """
        note = (6.67 - ch_note) / 0.67 # Funktion für das Umrechnen in die deutsche Notenskala 
        print(f"\nCH-Note: {ch_note:.2f}")
        print(f"DE-Note: {note:.2f}")

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
                    from notenskala import notenskala
                    notenskala(0,0)
                    return
                else:
                    print(f"{Farben.H_ROT}Ungültiger Buchstabe! Bitte (j/n) eingeben.{Farben.RESET}")
            except ValueError:
                print(f"{Farben.H_ROT}Ungültige Eingabe: Bitte (j/n) eingeben{Farben.RESET}")

    def usa(user,pw):
        """
        Funktion für das Umrechnen von CH-Note in die Notenskala von der USA
        """
        gpa = 0.8 * ch_note - 0.8 # Funktion für das Umrechnen in die Notenskala der USA 
        print(f"\nCH-Note: {ch_note:.2f}")
        print(f"US-Note: {gpa:.2f}")
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
                    from notenskala import notenskala
                    notenskala(0,0)
                    return
                else:
                    print(f"{Farben.H_ROT}Ungültiger Buchstabe! Bitte (j/n) eingeben.{Farben.RESET}")
            except ValueError:
                print(f"{Farben.H_ROT}Ungültige Eingabe: Bitte (j/n) eingeben{Farben.RESET}")

    print("\n", "="*50)
    print(farbig_center(f"{Farben.GELB}{Stil.KURSIV}Notenskala umrechner{Farben.RESET}"))
    print("="*50)

    while True:
        try:
            ch_note = float(input("\nGib deine CH Note ein: "))
            if 0 < ch_note <= 6:
                break
            print(f"\n{Farben.H_ROT}Ungültige Zahl: Gib eine Zahl von 1-6 ein!{Farben.RESET}")
            
        except ValueError:
            print(f"\n{Farben.H_ROT}Ungültige Eingabe: Gib eine Zahl von 1-6 ein!{Farben.RESET}")

    print(f"\n{Stil.FETT}In welches Notensystem möchtest du umrechnen?{Farben.RESET}\n")
    print("1) Deutschland")
    print("2) USA\n")

    while True:
        try:
            auswahl = int(input("Auswahl: "))
            if auswahl > 0 and auswahl <= 2:

                if auswahl == 1:
                    deutschland(user,pw)
                    return

                if auswahl == 2:
                    usa(user,pw)
                    return
                
            else:
                print(f"\n{Farben.H_ROT}Ungültige Zahl: Gib eine Zahl von 1-2 ein!{Farben.RESET}\n")
        except ValueError:
            print(f"\n{Farben.H_ROT}Ungültige Eingabe: Gib eine Zahl von 1-2 ein!{Farben.RESET}\n")

