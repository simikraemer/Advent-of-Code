geschenklines = {
    0: range(1, 4),
    1: range(5, 8),
    2: range(11, 14),
    3: range(16, 19),
    4: range(21, 24),
    5: range(26, 29),
}
regionen = []
blöcke = {}
for idx in geschenklines:
    blöcke[idx] = []
from pathlib import Path
with open(Path(__file__).resolve().parent / "input" / "12.txt", "r") as file:
    lines = file.readlines()
    for idx in geschenklines:
        y = 0
        for i in geschenklines[idx]:
            line = lines[i].strip()
            for x, ch in enumerate(line):
                if ch == "#":
                    blöcke[idx].append((x, y))
            y += 1
    for i,line in enumerate(lines):
        line = line.strip()
        if i < 30 or line == "" or ":" not in line:
            continue
        area, geschenke = line.split(":")
        breite, höhe = area.split("x")
        geschenkeanzahl = list(map(int, geschenke.split()))
        regionen.append(((int(breite), int(höhe)), geschenkeanzahl))
        
        
print("blöcke:")
for idx in sorted(blöcke):
    print(idx, blöcke[idx])

print()
print("regionen:")
for r in regionen:
    print(r)
    
aufgabe1 = 0
for region in regionen:
    fläche = region[0][0] * region[0][1]
    geschenkfläche = 0
    for i,geschenkanzahl in enumerate(region[1]):
        geschenkfläche += 9 * geschenkanzahl
    print(fläche, geschenkfläche)
    if geschenkfläche <= fläche:
        aufgabe1 += 1        

aufgabe2 = 0


print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")