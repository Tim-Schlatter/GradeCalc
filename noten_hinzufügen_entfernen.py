def note_hinzufügen(username,passwort,modul):
    """
    Fügt dem ausgewählten Modul eine neue Note hinzu.

    Der Benutzer gibt eine Note ein, welche auf Gültigkeit (1–6) geprüft wird.
    Die Note wird anschließend in der JSON-Datei gespeichert und das Programm
    kehrt zur Modulübersicht zurück.

    Parameter:
        username (str): Benutzername des aktuell angemeldeten Benutzers.
        passwort (str): Passwort des Benutzers (für die Rückkehr zur Modulübersicht).
        modul (str): Name des Moduls, dem die Note hinzugefügt wird.

    Rückgabewert:
        None
    """
    from ANSI import Farben,Stil,farbig_center,clear
    import os
    from deine_Module import deine_module
    import json
    # Terminal leeren für bessere Übersicht
    clear()
    # Überschrift / Header
    print("=" * 50)
    print(farbig_center(f"{Stil.FETT}Note hinzufügen{Farben.RESET}", 50))
    print(farbig_center(f"{Stil.KURSIV}Modul: {modul.capitalize()}{Farben.RESET}", 50))
    print("=" * 50)
    print()

    # Eingabeschleife für die Note (mit Validierung)
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
    
    # Pfad zur JSON-Datenbank
    dateipfad = os.path.join(os.path.dirname(__file__), "Datenbanken", "GradeCalc.json")
    # JSON-Daten laden
    with open(dateipfad, "r", encoding="utf-8") as f:
        all_data = json.load(f)

    # Note zum entsprechenden Modul hinzufügen
    all_data[username]["module_noten"][modul].append(note)

    
    # Aktualisierte Daten speichern
    with open(dateipfad, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=4, ensure_ascii=False)
    # Rückkehr zur Modulübersicht
    deine_module(username,passwort)
    return

def note_entfernen(username,passwort,modul):
    """
    Entfernt eine bestehende Note aus einem Modul.

    Der Benutzer wählt aus, welche Note gelöscht werden soll.
    Vor dem Löschen wird geprüft, ob überhaupt Noten vorhanden sind.
    Nach dem Entfernen wird die aktualisierte Liste gespeichert
    und zur Modulübersicht zurückgekehrt.

    Parameter:
        username (str): Benutzername des aktuell angemeldeten Benutzers.
        passwort (str): Passwort des Benutzers.
        modul (str): Name des Moduls, aus dem eine Note entfernt werden soll.

    Rückgabewert:
        None
    """
    import os
    import json
    from ANSI import Farben,Stil,farbig_center,clear
    from deine_Module import deine_module


    # Pfad zur JSON-Datenbank
    dateipfad = os.path.join(os.path.dirname(__file__), "Datenbanken", "GradeCalc.json")
    # JSON-Daten laden
    with open(dateipfad,"r",encoding="utf-8") as f:
        all_data = json.load(f)
    # Notenliste des ausgewählten Moduls
    notenliste = all_data[username]["module_noten"][modul]

    while True:
        # Falls keine Noten vorhanden sind, abbrechen
        if not notenliste:
            clear()
            print(f"{Farben.H_ROT}Keine Noten vorhanden! {Stil.RESET}")
            deine_module(username, passwort); return
            
        try:
            # Auswahl der zu löschenden Prüfung
            print()
            wahl = int(input("Welche Prüfung willst du löschen? "))
            # Gültigkeitsprüfung der Auswahl
            if wahl >= 1 and wahl <= len(notenliste):
                break
            else:
                print(f"{Farben.H_ROT}Ungültige Eingabe: Gib eine Zahl von 1-{len(notenliste)} ein!{Farben.RESET}")
                return
        except ValueError:
            print(f"{Farben.H_ROT}Ungültige Eingabe: Gib eine Zahl von 1-{len(notenliste)} ein!{Farben.RESET}")
            return
        
    # Löschen der ausgewählten Note
    if len(notenliste) >= 1:
        geloeschte_note = notenliste.pop(wahl-1)
        print(f"{Farben.H_ROT}Note {geloeschte_note} wurde gelöscht!{Farben.RESET}")
    else:
        print("Fehlermeldung 1")

    # Aktualisierte Notenliste speichern
    all_data[username]["module_noten"][modul] = notenliste

    with open(dateipfad, "w", encoding="utf-8") as f:
        # Speichert das Dictionary all_data als JSON in der Datei f.
        # indent=4 formatiert die Datei mit Einrückungen für bessere Lesbarkeit also es hat vier stufen der Einrückung.
        # ensure_ascii=False erlaubt Sonderzeichen (z.B. Umlaute) im Klartext.
        json.dump(all_data, f, indent=4, ensure_ascii=False)

    # Rückkehr zur Modulübersicht
    deine_module(username,passwort)
    return







