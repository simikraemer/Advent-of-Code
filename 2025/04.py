breite = 0
länge = 0
koordinaten = []

from pathlib import Path
with open(Path(__file__).resolve().parent / "input" / "04.txt", "r") as file:
    lines = file.readlines()
    länge = len(lines)
    for line in lines:
        line = line.strip()
        breite = len(line)
        koordinaten.append(list(line))

aufgabe1 = 0
for y, zeile in enumerate(koordinaten):
    for x, ziffer in enumerate(zeile):
        koord = (x,y)
        if ziffer == "@":
            papiercount = 0
            for yvar in range(y - 1, y + 2):
                for xvar in range(x - 1, x + 2):              
                    if (0 <= xvar < breite and 0 <= yvar < länge) and not (xvar == x and yvar == y) and koordinaten[yvar][xvar] == "@":
                        papiercount += 1
            if papiercount < 4:
                aufgabe1 += 1
        
aufgabe2 = 0


print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")
