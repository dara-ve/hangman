# Hangman - Plan
#
# 1. Geheimes Wort beim Start einlesen (python hangman.py apfel)
# 2. Leere Liste für geratene Buchstaben, Fehler = 0
# 3. Solange nicht gewonnen und Fehler < 8:
#      - Wort anzeigen, z.B. _ p _ _ _
#      - Galgen anzeigen
#      - Buchstaben einlesen
#      - Buchstabe im Wort? -> merken
#        sonst -> Fehler + 1
# 4. Gewonnen oder verloren ausgeben

import sys

wort = sys.argv[1]

import sys

wort = sys.argv[1]
geraten = []

anzeige = ""
for buchstabe in wort:
    if buchstabe in geraten:
        anzeige = anzeige + buchstabe + " "
    else:
        anzeige = anzeige + "_ "
print(anzeige)

#neuer Kommentar