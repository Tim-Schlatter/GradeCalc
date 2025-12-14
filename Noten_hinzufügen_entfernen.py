def note_hinzufügen(username,passwort,modul):
    from ANSI import Farben,Stil,farbig_center,clear
    import os
    from Deine_Module import deine_module
    import json
    clear()

    print("=" * 100)
    print(farbig_center(f"{Stil.FETT}Note hinzufügen{Farben.RESET}", 100))
    print(farbig_center(f"{Stil.KURSIV}Modul: {modul.capitalize()}{Farben.RESET}", 100))
    print("=" * 100)
    print()

    while True:
        try:
            note = float(input("Note: "))

            if note >= 1 and note <= 6:
                break
            else:
                print(f"{Farben.H_ROT}Gib eine Zahl zwischen 1-6 ein!{Farben.RESET}")
                continue
        except ValueError:
            print(f"{Farben.H_ROT}Gib eine Zahl zwischen 1-6 ein!{Farben.RESET}")
            continue
    
    dateipfad = os.path.join(os.path.dirname(__file__), "Datenbanken", "GradeCalc.json")

    with open(dateipfad, "r", encoding="utf-8") as f:
        all_data = json.load(f)

    all_data[username]["module_noten"][modul].append(note)

    

    with open(dateipfad, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=4, ensure_ascii=False)
        
    deine_module(username,passwort)
    return

def note_entfernen(username,passwort,modul):
    import os
    import json
    from ANSI import Farben,Stil,farbig_center,clear
    from Deine_Module import deine_module



    dateipfad = os.path.join(os.path.dirname(__file__), "Datenbanken", "GradeCalc.json")

    with open(dateipfad,"r",encoding="utf-8") as f:
        all_data = json.load(f)
    notenliste = all_data[username]["module_noten"][modul]


    while True:
        try:
            
            wahl = int(input("Welche Prüfung willst du löschen? "))
            if wahl >= 1 and wahl <= len(notenliste):
                break
            else:
                print(f"{Farben.H_ROT}Ungültige Eingabe: Gib eine Zahl von 1-{len(notenliste)} ein!{Farben.RESET}")
                return
        except ValueError:
            print(f"{Farben.H_ROT}Ungültige Eingabe: Gib eine Zahl von 1-{len(notenliste)} ein!{Farben.RESET}")
            return

    if len(notenliste) >= 1:
        geloeschte_note = notenliste.pop(wahl-1)
        print(f"{Farben.H_ROT}Note {geloeschte_note} wurde gelöscht!{Farben.RESET}")
    else:
        print("Fehlermeldung 1")

    all_data[username]["module_noten"][modul] = notenliste

    with open(dateipfad, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=4, ensure_ascii=False)
    
    deine_module(username,passwort)
    return







