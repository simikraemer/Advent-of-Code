frischebereiche = []
ids = []

from pathlib import Path
with open(Path(__file__).resolve().parent / "input" / "05.txt", "r") as file:
    lines = file.readlines()
    leerzeileerreicht = False
    for line in lines:   
        line = line.strip()     
        if line == "": # Leerzeile
            leerzeileerreicht = True
            continue
        if leerzeileerreicht == False: # Fresh Bereiche
            start = int(line.split("-")[0])
            end = int(line.split("-")[1])
            frischebereiche.append((start,end))
        else: # IDs
            ids.append(int(line))
            
aufgabe1 = 0
for id in ids:
    for frischebereich in frischebereiche:
        start, end = frischebereich
        if start <= id and id <= end:
            aufgabe1 += 1
            break
            
aufgabe2 = 0
frischebereiche_sorted = sorted(frischebereiche)
frischebereiche_cleaned = []
erstereintraggesetzt = False
for frischebereich in frischebereiche_sorted:
    start, end = frischebereich
    if erstereintraggesetzt == False:
        frischebereiche_cleaned.append((start,end))
        erstereintraggesetzt = True
    else:
        last_start, last_end = frischebereiche_cleaned[-1]
        if start <= last_end:
            frischebereiche_cleaned[-1] = (last_start, max(last_end, end))
        else:
            frischebereiche_cleaned.append((start, end))
    
for frischebereich in frischebereiche_cleaned:
    start, end = frischebereich
    aufgabe2 += end - start + 1

print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")
