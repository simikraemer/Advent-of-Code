matrix = []
splitter = []
from pathlib import Path
with open(Path(__file__).resolve().parent / "input" / "07.txt", "r") as file:
    lines = file.readlines()
for y, line in enumerate(lines):
    line = line.strip()
    höhe = len(lines)
    breite = len(line)
    linearray = []
    for x, eintrag in enumerate(line):
        linearray.append(eintrag)
        if eintrag == "S":
            start = (x,y)
        if eintrag == "^":
            splitter.append((x,y))
    matrix.append(linearray)
#print(start)
#print(splitter)
#print(breite)
#print(höhe)

aufgabe1 = 0

takyon = []
takyon.append(start)
for y, line in enumerate(matrix):
    for x, eintrag in enumerate(line):
        if (x,y) in takyon:
            if y == höhe - 1:
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
            
aufgabe2 = 0

        
print(takyon)
            
    
print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")