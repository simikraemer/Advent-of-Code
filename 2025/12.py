regionen = []
from pathlib import Path
with open(Path(__file__).resolve().parent / "input" / "12.txt", "r") as file:
    lines = file.readlines()
    for i,line in enumerate(lines):
        line = line.strip()
        if i < 30 or line == "":
            continue
        area, geschenke = line.split(":")
        breite, höhe = area.split("x")
        geschenkeanzahl = list(map(int, geschenke.split()))
        regionen.append(((int(breite), int(höhe)), geschenkeanzahl))
        
aufgabe1 = 0
for region in regionen:
    fläche = region[0][0] * region[0][1]
    geschenkfläche = 0
    for i,geschenkanzahl in enumerate(region[1]):
        geschenkfläche += 9 * (geschenkanzahl)
    if geschenkfläche <= fläche:
        aufgabe1 += 1 

print(f"Aufgabe 1: {aufgabe1}")

print(f"Aufgabe 2 ist geschenkt :^)")