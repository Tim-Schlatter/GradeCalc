import re
import os

class Farben:
    """Auswahl an Farben: Farben.(Gewünschte Farbe)"""
    SCHWARZ = "\033[30m"
    ROT = "\033[31m"
    GRUEN = "\033[32m"
    GELB = "\033[33m"
    BLAU = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WEISS = "\033[37m"

    H_SCHWARZ = "\033[90m"
    H_ROT = "\033[91m"
    H_GRUEN = "\033[92m"
    H_GELB = "\033[93m"
    H_BLAU = "\033[94m"
    H_MAGENTA = "\033[95m"
    H_CYAN = "\033[96m"
    H_WEISS = "\033[97m"

    RESET = "\033[0m"

class Stil:
    """Auswahl an Stillmittel: Still.(Gewünschter Still)"""
    FETT = "\033[1m"
    KURSIV = "\033[3m"
    UNTERSTRICHEN = "\033[4m"
    BLINKEND = "\033[5m"
    INVERTIERT = "\033[7m"
    RESET = "\033[0m" # Wird benutzt, um die Farben und den Still zurückzusetzen! 

def farbig_center(text: str, width: int = 50) -> str:
    """Zentriert den Text in der () nach farbig_center"""
    sichtbarer_text = re.sub(r"\033\[[0-9;]*m", "", text)
    padding = max((width - len(sichtbarer_text)) // 2, 0)
    return " " * padding + text

def clear():
    """Reinigt das Terminal, sodass nichts mehr drin steht. Für die Übersicht gedacht."""
    os.system("cls" if os.name == "nt" else "clear")
