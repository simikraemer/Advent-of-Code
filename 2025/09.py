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

aufgabe2 = 0       
    
print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")