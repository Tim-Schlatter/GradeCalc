from ANSI import Farben, Stil, farbig_center, clear
from durchschnitt_berechnen import durchschnitt_berechnen
from notenberechnung import notenberechnung
from notenskala import notenskala
from Anmelden import anmelden
import sys



def main_menu():
    
    print("="*50)
    print(farbig_center(f"{Stil.FETT}HAUPTMENÜ GradeCalc{Farben.RESET}", 50))
    print("="*50)
    print("\n1) Durchschnitt berechnen ")
    print("2) Notenberechnung nach Punkten ")
    print("3) Notenskala umrechner ")
    print("4) Anmelden / Registrieren ")
    print("5) Beenden! \n")
    
    while True: 
        try:
            function = int(input("Welche Funktion willst du ausführen? "))
            if function >=1 and function <6:
                if function == 1:
                    durchschnitt_berechnen(0,0)
                    return
                if function == 2:
                    notenberechnung(0,0)
                    return
                if function == 3: 
                    notenskala(0,0)
                    return
                if function == 4:
                    anmelden()
                    return
                if function == 5:
                    print("Programm beendet!\n")
                    sys.exit()
                    
            else:
                print(f"\n{Farben.H_ROT}Ungültige Zahl: Gib eine Zahl zwischen 1-5 ein!{Farben.RESET}\n")
        except ValueError:
            print(f"\n{Farben.H_ROT}Ungültige Eingabe: Gib eine Zahl zwischen 1-5 ein!{Farben.RESET}\n")



if __name__ == "__main__":
    main_menu()















