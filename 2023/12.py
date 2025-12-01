import sys
from functools import cache

with open("2023/input/12.txt", 'r') as fl:
    src = fl.read().strip().split()

fiji1 = 0
fiji2 = 0

zeilen1 = []
for i in range(0, len(src), 2):
    src_zeichen = src[i].strip()
    src_zahlen = tuple(map(int, src[i + 1].strip().split(',')))
    zeilen1.append((src_zeichen, src_zahlen))
    
zeilen2 = []
for zeile in zeilen1:
    new_zeichen = '?'.join([zeile[0]] * 5)
    new_zahlen = ','.join([','.join(map(str, zeile[1]))] * 5)
    converted_zahlen = tuple(map(int, new_zahlen.split(',')))
    zeilen2.append((new_zeichen, converted_zahlen))
    
@cache
def möglichkeiten_abzählen(zeichen, zahlen):
    if len(zeichen) == 0 and len(zahlen) == 0:
        return 1
    elif len(zeichen) == 0:
        return 0

    if zeichen[0] == "?":
        return möglichkeiten_abzählen("#" + zeichen[1:], zahlen) + möglichkeiten_abzählen("." + zeichen[1:], zahlen)
    
    elif zeichen[0] == "#":
        if len(zahlen) == 0 or len(zeichen) < zahlen[0] or "." in zeichen[0 : zahlen[0]] or zeichen[zahlen[0] :].startswith("#"):
            return 0
        elif len(zeichen) > zahlen[0] and zeichen[zahlen[0]] == "?":
            return möglichkeiten_abzählen("." + zeichen[zahlen[0] + 1 :].lstrip("."), zahlen[1:])
        else:
            return möglichkeiten_abzählen(zeichen[zahlen[0] :].lstrip("."), zahlen[1:])
        
    elif zeichen[0] == ".":
        return möglichkeiten_abzählen(zeichen.lstrip("."), zahlen)
    
counter = 0
anzahl_zeilen = len(zeilen1)
vor_progress = -1
for eintrag in zeilen1:
    counter += 1        
    progress = (counter / anzahl_zeilen) * 100
    akt_progress = int(progress)
    if akt_progress != vor_progress:
        vor_progress = akt_progress
        sys.stdout.write("\r")
        sys.stdout.write(f"Fortschritt Aufgabe 1: [{'=' * akt_progress}{' ' * (100 - akt_progress)}] {akt_progress}%")
        sys.stdout.flush()
    fiji1 += möglichkeiten_abzählen(eintrag[0], eintrag[1])
print(" - Abgeschlossen")

counter = 0
anzahl_zeilen = len(zeilen2)
vor_progress = -1
for eintrag in zeilen2:
    counter += 1        
    progress = (counter / anzahl_zeilen) * 100
    akt_progress = int(progress)
    if akt_progress != vor_progress:
        vor_progress = akt_progress
        sys.stdout.write("\r")
        sys.stdout.write(f"Fortschritt Aufgabe 2: [{'=' * akt_progress}{' ' * (100 - akt_progress)}] {akt_progress}%")
        sys.stdout.flush()
    fiji2 += möglichkeiten_abzählen(eintrag[0], eintrag[1])
print(" - Abgeschlossen")

print("Lösung Aufgabe 12.1: " + str(fiji1))
print("Lösung Aufgabe 12.2: " + str(fiji2))
print("Grüße von Fiji :^)")