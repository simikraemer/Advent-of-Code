zeiger = 50 #startwert
aufgabe1 = 0
aufgabe2 = 0

from pathlib import Path
with open(Path(__file__).resolve().parent / "input" / "01.txt", "r") as file:
    lines = file.readlines()    
    
for line in lines:
    line = line.strip()
    richtung = line[0]
    wert = int(line[1:])
    i = 0
    while i < wert:
        if richtung == "R":
            zeiger += 1
        elif richtung == "L":
            zeiger -= 1
            
        if zeiger == -1:
            zeiger = 99
        elif zeiger == 100:
            zeiger = 0
            
        if zeiger == 0:
            aufgabe2 += 1
            
        i += 1
    
    if zeiger == 0:
        aufgabe1 += 1
        
print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")