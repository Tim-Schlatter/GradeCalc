def modul_hinzufügen(username, password):
    import json, os
    from ANSI import Farben, Stil, farbig_center,clear
    from User_menu import user_menu

    print("=" * 100)
    print(farbig_center(f"{Stil.FETT}{Farben.CYAN}Modul hinzufügen{Farben.RESET}", 100))
    print(farbig_center(f"{Stil.KURSIV}User: {username.capitalize()}{Farben.RESET}", 100))
    print("=" * 100)
    print()
    while True:
        
        modul_name = str(input("Gib den Modulnamen an: ")).lower()

        dateipfad = os.path.join(os.path.dirname(__file__), "Datenbanken", "GradeCalc.json")

        # JSON-Daten laden
        with open(dateipfad, "r", encoding="utf-8") as f:
            all_data = json.load(f)
        module = all_data[username]["module_noten"]
        if modul_name in module:
            print(f"{Farben.H_ROT}Ungültige Eingabe: Modul existiert bereits!{Farben.RESET}")
            continue
        else:
            break
        
    all_data[username]["module_noten"][modul_name] = []
    with open(dateipfad, "w", encoding="utf-8") as f:
        json.dump(all_data,f, indent=4,ensure_ascii=False)
    
    user_menu(username,password)
    return




def modul_entfernen(username, password,modul):
    import json, os
    from ANSI import Farben, Stil, farbig_center,clear
    from User_menu import user_menu
    from Deine_Module import deine_module

    while True:
        wahl = input(f"Modul {modul.capitalize()} wirklich löschen? (j/n): ")
        if wahl != "j" and wahl != "n":
            print(f"{Farben.H_ROT}Ungültige Eingabe: Gib j/n ein!{Farben.RESET}")
            continue
        else:  
            break
    if wahl == "j":
        dateipfad = os.path.join(os.path.dirname(__file__), "Datenbanken", "GradeCalc.json")
        with open(dateipfad, "r",encoding="utf-8") as f:
            all_data = json.load(f)
        module = all_data[username]["module_noten"]

        del module[modul]

        all_data[username]["module_noten"] = module

        with open(dateipfad, "w", encoding="utf-8") as f:
            json.dump(all_data, f, indent=4, ensure_ascii=False)

    if wahl == "n":
        deine_module(username,password)
        return
        
    
    deine_module(username,password)
    return



# modul_entfernen("tim","passwort","mathe")