redkoords = []
from pathlib import Path
with open(Path(__file__).resolve().parent / "input" / "09.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        x, y = line.split(",")
        redkoords.append((int(x),int(y)))

def square_hammer(uno,dos):
    x1, y1 = uno
    x2, y2 = dos
    square = (abs((x2-x1))+1) * (abs((y2-y1))+1)
    return square

aufgabe1 = 0
for uno in redkoords:
    for dos in redkoords:
        if dos >= uno:
            continue
        square = square_hammer(uno,dos)
        if aufgabe1 < square:
            aufgabe1 = square

kanten = []
for i, koord in enumerate(redkoords):
    x1,y1 = koord
    if i == len(redkoords) - 1:
        x2, y2 = redkoords[0]
    else:
        x2, y2 = redkoords[i + 1]
        
    if x1 == x2: # vertikal
        if y1 <= y2:
            kanten.append(((x1,y1),(x2,y2)))
        else:
            kanten.append(((x2,y2),(x1,y1)))
    else: # horizontal
        if x1 <= x2:
            kanten.append(((x1,y1),(x2,y2)))
        else:
            kanten.append(((x2,y2),(x1,y1)))
    
            
aufgabe2 = 0
for i, uno in enumerate(redkoords):
    for dos in redkoords:
        if dos >= uno:
            continue

        square = square_hammer(uno, dos)

        if dos[0] > uno[0]:
            x1 = uno[0]
            x2 = dos[0]
        else:
            x1 = dos[0]
            x2 = uno[0]

        if dos[1] > uno[1]:
            y1 = uno[1]
            y2 = dos[1]
        else:
            y1 = dos[1]
            y2 = uno[1]

        inside = True
        for kante in kanten:
            (kx1,ky1),(kx2,ky2) = kante
            if kx2 > x1 and kx1 < x2 and ky2 > y1 and ky1 < y2:
                inside = False
                break

        if inside and aufgabe2 < square:
            aufgabe2 = square

print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")