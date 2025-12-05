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

print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")
