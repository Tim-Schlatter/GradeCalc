import re
import os

class Farben:
    """    
    Enthält ANSI-Farbcodes zur farbigen Darstellung von Text im Terminal.

    Die Farben können über Farben.<FARBE> verwendet werden,
    z.B. Farben.ROT oder Farben.H_GRUEN.
    """

    # Standardfarben
    SCHWARZ = "\033[30m"
    ROT = "\033[31m"
    GRUEN = "\033[32m"
    GELB = "\033[33m"
    BLAU = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WEISS = "\033[37m"

    # Helle Farben
    H_SCHWARZ = "\033[90m"
    H_ROT = "\033[91m"
    H_GRUEN = "\033[92m"
    H_GELB = "\033[93m"
    H_BLAU = "\033[94m"
    H_MAGENTA = "\033[95m"
    H_CYAN = "\033[96m"
    H_WEISS = "\033[97m"

    # Setzt alle Farben zurück
    RESET = "\033[0m"

class Stil:
    """    
    Enthält ANSI-Stilcodes zur Formatierung von Text im Terminal.

    Die Stile können über Stil.<STIL> verwendet werden,
    z.B. Stil.FETT oder Stil.UNTERSTRICHEN.
    """
    FETT = "\033[1m"
    KURSIV = "\033[3m"
    UNTERSTRICHEN = "\033[4m"
    BLINKEND = "\033[5m"
    INVERTIERT = "\033[7m"
    RESET = "\033[0m" # Wird benutzt, um die Farben und den Still zurückzusetzen! 

def farbig_center(text: str, width: int = 50) -> str:
    """    
    Zentriert einen Text im Terminal unter Berücksichtigung von ANSI-Farbcodes.

    Da ANSI-Farbcodes die Textlänge verfälschen würden, werden diese vor
    der Berechnung der Einrückung entfernt.

    Parameter:
        text (str): Der anzuzeigende Text (inkl. ANSI-Farbcodes).
        width (int): Die gewünschte Gesamtbreite der Ausgabe.

    Rückgabewert:
        str: Zentrierter Text inklusive originaler Farbcodes.
    """
    # Entfernt ANSI-Farbcodes, um die echte Textlänge zu berechnen
    sichtbarer_text = re.sub(r"\033\[[0-9;]*m", "", text)

    # Berechnung des benötigten Abstands zur Zentrierung
    padding = max((width - len(sichtbarer_text)) // 2, 0)

    # Rückgabe des zentrierten Textes mit originalen Farbcodes
    return " " * padding + text

def clear():
    """    
    Leert das Terminalfenster.

    Unter Windows wird der Befehl 'cls' verwendet,
    unter Linux/macOS der Befehl 'clear'.
    """

    # Betriebssystemabhängiger Clear-Befehl
    os.system("cls" if os.name == "nt" else "clear")
