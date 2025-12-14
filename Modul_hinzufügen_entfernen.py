def modul_hinzufügen(username, password):
    """
    Fügt dem aktuell angemeldeten Benutzer ein neues Modul hinzu.

    Der Benutzer gibt einen Modulnamen ein. Es wird geprüft, ob das Modul
    bereits existiert. Falls nicht, wird ein neues Modul mit einer leeren
    Notenliste in der JSON-Datei gespeichert.

    Parameter:
        username (str): Benutzername des aktuell angemeldeten Benutzers.
        password (str): Passwort des aktuell angemeldeten Benutzers.

    Rückgabewert:
        None
    """
    import json, os
    from ANSI import Farben, Stil, farbig_center,clear
    from deine_Module import deine_module

    # Überschrift / Header 
    print("=" * 50)
    print(farbig_center(f"{Stil.FETT}{Farben.CYAN}Modul hinzufügen{Farben.RESET}", 50))
    print(farbig_center(f"{Stil.KURSIV}User: {username.capitalize()}{Farben.RESET}", 50))
    print("=" * 50)
    print()

    # Schleife zur Eingabe und Validierung des Modulnamens
    while True:
        
        modul_name = str(input("Gib den Modulnamen an: ")).lower()

        # Pfad zur JSON-Datenbank
        dateipfad = os.path.join(os.path.dirname(__file__), "Datenbanken", "GradeCalc.json")

        # JSON-Daten laden
        with open(dateipfad, "r", encoding="utf-8") as f:
            all_data = json.load(f)
        # Alle bestehenden Module des Users
        module = all_data[username]["module_noten"]
        # Prüfen, ob das Modul bereits existiert
        if modul_name in module:
            print(f"{Farben.H_ROT}Ungültige Eingabe: Modul existiert bereits!{Farben.RESET}")
            continue
        else:
            break

    # Neues Modul mit leerer Notenliste hinzufügen
    all_data[username]["module_noten"][modul_name] = []
    with open(dateipfad, "w", encoding="utf-8") as f:
        json.dump(all_data,f, indent=4,ensure_ascii=False)
    # Rückkehr zu deine_module
    deine_module(username,password)
    return




def modul_entfernen(username, password,modul):
    """
    Entfernt ein bestehendes Modul des Benutzers nach Bestätigung.

    Der Benutzer wird gefragt, ob das ausgewählte Modul wirklich gelöscht
    werden soll. Bei Bestätigung wird das Modul inklusive aller Noten
    aus der JSON-Datei entfernt.

    Parameter:
        username (str): Benutzername des aktuell angemeldeten Benutzers.
        password (str): Passwort des aktuell angemeldeten Benutzers.
        modul (str): Name des zu löschenden Moduls.

    Rückgabewert:
        None
    """
    import json, os
    from ANSI import Farben, Stil, farbig_center,clear
    from deine_Module import deine_module

    # Bestätigungsabfrage vor dem Löschen
    while True:
        print()
        wahl = input(f"Modul {modul.capitalize()} wirklich löschen? (j/n): ")
        if wahl != "j" and wahl != "n":
            print(f"{Farben.H_ROT}Ungültige Eingabe: Gib j/n ein!{Farben.RESET}")
            continue
        else:  
            break
    if wahl == "j":
        # Pfad zur JSON-Datenbank
        dateipfad = os.path.join(os.path.dirname(__file__), "Datenbanken", "GradeCalc.json")
        # JSON-Daten laden
        with open(dateipfad, "r",encoding="utf-8") as f:
            all_data = json.load(f)
        # Module des Benutzers
        module = all_data[username]["module_noten"]
        # Modul löschen
        del module[modul]
        # Aktualisierte Module wieder speichern
        all_data[username]["module_noten"] = module

        with open(dateipfad, "w", encoding="utf-8") as f:
            json.dump(all_data, f, indent=4, ensure_ascii=False)
    # Falls der Benutzer den Löschvorgang abbricht
    if wahl == "n":
        deine_module(username,password)
        return
        
    # Nach dem Löschen zurück zur Modulübersicht
    deine_module(username,password)
    return



