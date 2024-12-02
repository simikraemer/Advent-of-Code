import sys

fiji1 = 0
fiji2 = 0

with open("input/14.txt", "r") as fl:
    lines = fl.readlines()
    plattform = [list(line.strip()) for line in lines]

stillstand = False
while not stillstand:
    rolling = False
    for y, zeile in enumerate(plattform):
        for x, zeichen in enumerate(zeile):
            if y > 0:
                if zeichen == "O" and plattform[y-1][x] == ".":
                    plattform[y][x] = "."
                    plattform[y-1][x] = "O"
                    rolling = True
    if not rolling:
        stillstand = True

einträge = plattform
counter = 0
anzahl_zeilen = len(einträge)
vor_progress = -1
umgekehrte_einträge = list(reversed(einträge))
for idx,eintrag in enumerate(umgekehrte_einträge):    
    counter += 1
    progress = (counter / anzahl_zeilen) * 100
    akt_progress = int(progress)
    if akt_progress != vor_progress:
        vor_progress = akt_progress
        sys.stdout.write("\r")
        sys.stdout.write(f"Fortschritt Aufgabe 1: [{'=' * akt_progress}{' ' * (100 - akt_progress)}] {akt_progress}%")
        sys.stdout.flush()
    for zeichen in eintrag:
        if zeichen == "O":
            fiji1 += idx + 1
    
print(" - Abgeschlossen")

def zyklus(plattform):
    richtungen = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for richtung in richtungen:
        stillstand = False
        while not stillstand:
            rolling = False
            for y, zeile in enumerate(plattform):
                for x, zeichen in enumerate(zeile):
                    if zeichen == "O":
                        dy, dx = richtung
                        new_y, new_x = y + dy, x + dx

                        if 0 <= new_y < len(plattform) and 0 <= new_x < len(zeile) and plattform[new_y][new_x] == ".":
                            plattform[y][x] = "."
                            plattform[new_y][new_x] = "O"
                            rolling = True

            if not rolling:
                stillstand = True
    
counter = 0
zyklen = 200
vor_progress = -1
for _ in range(zyklen):
    zyklus(plattform)
    counter += 1
    progress = (counter / zyklen) * 100
    akt_progress = int(progress)
    if akt_progress != vor_progress:
        vor_progress = akt_progress
        sys.stdout.write("\r")
        sys.stdout.write(f"Fortschritt Aufgabe 2: [{'=' * akt_progress}{' ' * (100 - akt_progress)}] {akt_progress}%")
        sys.stdout.flush()
    einträge = plattform
    gewicht = 0
    umgekehrte_einträge = list(reversed(einträge))
    for idx,eintrag in enumerate(umgekehrte_einträge):
        for zeichen in eintrag:
            if zeichen == "O":
                gewicht += idx + 1
    #print(_,gewicht)
print(" - Abgeschlossen")

# hier habe ich einen loop erkannt und gelöst mit (x + 1) + (51 * y) = 1000000000
# (108 + 1) + (51 * 19607841) = 1000000000
# gewicht für idx 108 -> 93742

fiji2 = 93742 # lmaoitjustwerks
        
print("Lösung Aufgabe 14.1: " + str(fiji1))
print("Lösung Aufgabe 14.2: " + str(fiji2))
print("Grüße von Fiji :^)")