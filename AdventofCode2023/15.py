import sys

fiji1 = 0
fiji2 = 0
einträge = []

with open("input/15.txt", "r") as fl:
    data = fl.read().replace('\n', '')
    einträge = data.split(',')

def hashaa1a(string):
    val = 0
    for char in string:
        val += ord(char)
        val *= 17
        val %= 256
    return val

counter = 0
anzahl_zeilen = len(einträge)
vor_progress = -1
for eintrag in einträge:
    fiji1 += hashaa1a(eintrag)
    counter += 1
    progress = (counter / anzahl_zeilen) * 100
    akt_progress = int(progress)
    if akt_progress != vor_progress:
        vor_progress = akt_progress
        sys.stdout.write("\r")
        sys.stdout.write(f"Fortschritt Aufgabe 1: [{'=' * akt_progress}{' ' * (100 - akt_progress)}] {akt_progress}%")
        sys.stdout.flush()
print(" - Abgeschlossen")

boxes = [[] for _ in range(256)]

def hashmap(box_val, label, entfernen, focallength):
    if entfernen:
        for idx,box in enumerate(boxes):
            for eintrag in box:
                if label in eintrag:
                    boxes[idx].remove(eintrag)
    else:
        for idx, eintrag in enumerate(boxes[box_val]):
            if label in eintrag:
                boxes[box_val][idx] = [label, focallength]
                break
        else:
            boxes[box_val].append([label, focallength])
        
counter = 0
anzahl_zeilen = len(einträge)
vor_progress = -1
for eintrag in einträge:
    if '=' in eintrag:
        sliced_eintrag = eintrag.split('=')
        label = sliced_eintrag[0]
        focallength = sliced_eintrag[1]
        entfernen = False
    else:
        sliced_eintrag = eintrag.split('-')
        label = sliced_eintrag[0]
        focallength = None
        entfernen = True
    box_val = hashaa1a(label)
    hashmap(box_val,label,entfernen,focallength)        
    
    counter += 1
    progress = (counter / anzahl_zeilen) * 100
    akt_progress = int(progress)
    if akt_progress != vor_progress:
        vor_progress = akt_progress
        sys.stdout.write("\r")
        sys.stdout.write(f"Fortschritt Aufgabe 1: [{'=' * akt_progress}{' ' * (100 - akt_progress)}] {akt_progress}%")
        sys.stdout.flush()
print(" - Abgeschlossen")

for idx_box, box in enumerate(boxes):
    for idx,eintrag in enumerate(box):
        fiji2 += (idx_box + 1) * (idx + 1) * int(eintrag[1])
    
print("Lösung Aufgabe 15.1: " + str(fiji1))
print("Lösung Aufgabe 15.2: " + str(fiji2))
print("Grüße von Fiji :^)")