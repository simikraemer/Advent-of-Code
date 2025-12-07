matrix = []
splitter = []
from pathlib import Path
with open(Path(__file__).resolve().parent / "input" / "07.txt", "r") as file:
    lines = file.readlines()
for y, line in enumerate(lines):
    line = line.strip()
    breite = len(line)
    linearray = []
    leerzeile = True
    for x, eintrag in enumerate(line):
        linearray.append(eintrag)
        if eintrag == "S":
            leerzeile = False
            start = (x,y)
        if eintrag == "^":
            leerzeile = False
            splitter.append((x,y))
    if not leerzeile:
        matrix.append(linearray)

höhe = len(matrix)

aufgabe1 = 0
takyon = []
takyon.append(start)
for y, line in enumerate(matrix):
    for x, eintrag in enumerate(line):
        if (x,y) in takyon:
            if y == höhe-1:
                break
            if matrix[y+1][x] != "^":
                if (x,y+1) not in takyon:
                    takyon.append((x,y+1))
            else:
                aufgabe1 += 1
                if (x-1,y+1) not in takyon:
                    takyon.append((x-1,y+1)) 
                if (x+1,y+1) not in takyon:
                    takyon.append((x+1,y+1))
            
aufgabe2 = 1
takyon = {}
takyon[start] = 1
for y, line in enumerate(matrix):
    for x, eintrag in enumerate(line):
        if (x,y) in takyon:
            anzahl = takyon[(x, y)]
            if y == höhe-1:
                break
            if matrix[y+1][x] != "^":
                if ((x,y+1) not in takyon):
                    takyon[(x,y+1)] = 0
                takyon[(x,y+1)] += anzahl
            else:
                aufgabe2 += anzahl
                if ((x-1,y+1) not in takyon):
                    takyon[(x-1,y+1)] = 0
                if ((x+1,y+1) not in takyon):
                    takyon[(x+1,y+1)] = 0
                takyon[(x-1,y+1)] += anzahl
                takyon[(x+1,y+1)] += anzahl           
    
print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")