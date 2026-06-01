"""
Baustein 01 – Grundlagen der Softwaretests
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""


# ============================================================
# Aufgabe 1 – Fehlerhafte Funktion
# ============================================================

def berechne_rabatt(preis: float, prozent: float) -> float:
    """
    Berechnet den Preis nach Rabattabzug.

    Beispiel:
        berechne_rabatt(100.0, 20) soll 80.0 zurückgeben.
    """
    # Hier ist ein Defekt eingebaut – findest du ihn?
    rabatt = preis * prozent  # <-- Zeile mit Defekt
    return preis - rabatt


# Aufgabe 1a): Beantworte folgende Fragen als Kommentar:

# Error (falsche Handlung des Entwicklers):
# TODO: Der Entwickler hat den Prozentwert direkt mit dem Preis multipliziert, anstatt ihn zuerst durch 100 zu teilen.

# Defect (fehlerhafte Stelle im Code):
# TODO: rabatt = preis * prozent

# Failure (was der Benutzer bemerken würde):
# TODO: Die Funktion liefert einen falschen Endpreis.
# Beispiel: berechne_rabatt(100.0, 20) ergibt -1900.0 statt 80.0.


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    """
    Korrigierte Version von berechne_rabatt().
    TODO: Implementiere die korrekte Logik.
    """
    rabatt = preis * (prozent / 100)
    return preis - rabatt


# Manuelle Tests (werden in Baustein 05 durch echte Unit-Tests ersetzt)
if __name__ == "__main__":
    # TODO: Ergänze mindestens 3 eigene print()-Tests für berechne_rabatt_korrigiert().
    # Überlege selbst: Was sind sinnvolle Eingaben? Was erwartest du als Ergebnis?

    print("=== Test: berechne_rabatt (fehlerhaft) ===")
    print(berechne_rabatt(100.0, 20))  # Falsche Ausgabe erwartet

    print("\n=== Test: berechne_rabatt_korrigiert ===")
    
    # Test 1: Beispiel von oben
    print("Test 1:", berechne_rabatt_korrigiert(100.0, 20))
    # ergebniss soll: 80.0

    # Test 2: Kein Rabatt
    print("Test 2:", berechne_rabatt_korrigiert(50.0, 0))
    # ergebniss soll: 50.0

    # Test 3: 50 % Rabatt
    print("Test 3:", berechne_rabatt_korrigiert(200.0, 50))
    # ergebniss soll: 100.0


# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    | ja       | nein      |
# | Programm mit Testdaten ausführen    | nein     | ja        |
# | Syntaxprüfung durch den Editor      | ja       | nein      |
# | Walkthroughs im Team                | ja       | nein      |
# | Unit-Tests laufen lassen            | nein     | ja        |
# | Checklisten für Codestruktur        | ja       | nein      |
#
# Warum reicht statisches Testen allein nicht aus?
# TODO: 
# # Durch statisches Testen können Fehler früh erkannt werden, ohne das
# Programm zu starten. Ob die Anwendung mit echten Eingaben korrekt arbeitet,
# lässt sich jedoch erst durch das Ausführen von Tests überprüfen.


# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag:
# Bei einem Online-Shop gibt es unzählige Kombinationen aus Produkten,
# Rabatten, Zahlungsmethoden und Lieferadressen. Alle möglichen Fälle
# vollständig zu testen wäre zeitlich und organisatorisch nicht machbar.

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag:
# In einer großen Anwendung treten die meisten Fehler immer wieder im
# Zahlungsmodul auf, während andere Bereiche kaum Probleme verursachen.
# Fehler häufen sich also in bestimmten Teilen der Software.

# Welches Prinzip überrascht dich? Warum?
# Mich überrascht das Prinzip des Defect Clusterings, weil man erwarten
# könnte, dass Fehler gleichmäßig im gesamten Programm verteilt sind.
# Tatsächlich entstehen jedoch viele Fehler oft in wenigen komplexen Bereichen.
