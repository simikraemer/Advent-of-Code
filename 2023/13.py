import sys

fiji1 = 0
fiji2 = 0

with open("2023/input/13.txt", "r") as fl:
    einträge = []
    akt_eintrag = []
    for zeile in map(str.strip, fl):
        if zeile == "":
            einträge.append(akt_eintrag)
            akt_eintrag = []
        else:
            akt_eintrag.append(zeile)
    einträge.append(akt_eintrag)

def achsefinden(eintrag, voriges_result):
    for idx in range(len(eintrag[0]) - 1):
        sym = True
        for x_dist in range(min(idx + 1, len(eintrag[0]) - 1 - idx)):
            for y_dist in range(len(eintrag)):
                if eintrag[y_dist][idx - x_dist] != eintrag[y_dist][idx + 1 + x_dist]:
                    sym = False
                    break
            if not(sym):
                break
        if sym:
            result = idx + 1
            if result != voriges_result:
                return result
    for idx in range(len(eintrag) - 1):
        sym = True
        for y_dist in range(min(idx + 1, len(eintrag) - 1 - idx)):
            if eintrag[idx - y_dist] != eintrag[idx + 1 + y_dist]:
                sym = False
                break
        if sym:
            result = (idx + 1) * 100
            if result != voriges_result:
                return result
    return 0

results = []
counter = 0
anzahl_zeilen = len(einträge)
vor_progress = -1
for eintrag in einträge:
    counter += 1
    progress = (counter / anzahl_zeilen) * 100
    akt_progress = int(progress)
    if akt_progress != vor_progress:
        vor_progress = akt_progress
        sys.stdout.write("\r")
        sys.stdout.write(f"Fortschritt Aufgabe 1: [{'=' * akt_progress}{' ' * (100 - akt_progress)}] {akt_progress}%")
        sys.stdout.flush()
    result = achsefinden(eintrag, 0)
    results.append(result)
    fiji1 += result
print(" - Abgeschlossen")

counter = 0
anzahl_zeilen = len(einträge)
vor_progress = -1
for idx, eintrag in enumerate(einträge):    
    counter += 1
    progress = (counter / anzahl_zeilen) * 100
    akt_progress = int(progress)
    if akt_progress != vor_progress:
        vor_progress = akt_progress
        sys.stdout.write("\r")
        sys.stdout.write(f"Fortschritt Aufgabe 2: [{'=' * akt_progress}{' ' * (100 - akt_progress)}] {akt_progress}%")
        sys.stdout.flush()
    for zeile in range(len(eintrag)):
        doppelbreak = False
        for zeichen in range(len(eintrag[0])):
            temp_eintrag = list(eintrag)
            temp_eintrag[zeile] = list(temp_eintrag[zeile])
            temp_eintrag[zeile][zeichen] = "." if temp_eintrag[zeile][zeichen] == "#" else temp_eintrag[zeile][zeichen]
            temp_eintrag[zeile] = "".join(temp_eintrag[zeile])
            temp_eintrag = tuple(temp_eintrag)
            result = achsefinden(temp_eintrag, results[idx])
            if result != 0:
                fiji2 += result
                doppelbreak = True
                break
        if doppelbreak == True:
            break
print(" - Abgeschlossen")
        
print("Lösung Aufgabe 13.1: " + str(fiji1))
print("Lösung Aufgabe 13.2: " + str(fiji2))
print("Grüße von Fiji :^)")