import matplotlib.pyplot as plt

def koordinatensystem(koordinaten):
    y = [-pos[0] for pos in koordinaten]
    x = [pos[1] for pos in koordinaten]

    plt.scatter(x, y)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    
fiji1 = 0
fiji2 = 0

with open("AdventofCode2023/input/18.txt", "r") as file:
    zeilen = [zeile.split() for zeile in file.read().strip().split("\n")]

richtungen = {
    "U": (-1,0),
    "D": (1,0),
    "L": (0,-1),
    "R": (0,1)
}

position = (0,0)
rahmen = set()
dirdict = {
    "U": [],
    "D": []
}
for zeile in zeilen:
    richtung, schritte, farbe = zeile
    for schritt in range(int(schritte)):
        if richtung in ("U", "D"):
            dirdict[richtung].append(position)
        position = tuple(map(sum, zip(position, richtungen[richtung])))
        rahmen.add(position)
        if richtung in ("U", "D"):
            dirdict[richtung].append(position)
        
füllung = set()
for x in range(min(p[0] for p in rahmen), max(p[0] for p in rahmen) + 1):
    print("Aufgabe 1:",x,"/",max(p[0] for p in rahmen))
    for y in range(min(p[1] for p in rahmen), max(p[1] for p in rahmen) + 1):
        frei = all((x, y) != rahmen_position for rahmen_position in rahmen)
        position = x,y
        anzahl = sum(
            1 for position in dirdict.get("U", []) + dirdict.get("D", [])
            if position[0] < x and position[1] < y
        )

        zentral = False
        if anzahl > 0:
            zentral = anzahl % 2 != 0

        #print(position,anzahl,frei,zentral)
        if frei and zentral:
            füllung.add((x,y))

#koordinatensystem(rahmen)
ergebnis = füllung | rahmen
#koordinatensystem(ergebnis)
for feld in ergebnis:
    fiji1 += 1
    

# Leck mich am Arsch!!!
# Gaußsche Trapezformel!!!

position = (0,0)
punkte = []
dirdict = {
    "U": [],
    "D": []
}
x = 0
y = 0
randpunkte = 0

for zeile in zeilen:
    falscherichtung, falscheschritte, farbe = zeile
    schritte_hex = farbe[2:7]
    richtung_hex = farbe[7:8]
    schritte = int(schritte_hex, 16)
    richtungen_mapping = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
    richtung = richtungen_mapping.get(int(richtung_hex))
    y += int(richtungen[richtung][0]) * schritte
    x += int(richtungen[richtung][1]) * schritte
    punkt = (y,x)
    punkte.append(punkt)
    randpunkte += schritte / 2
    #print("Schritte",schritte,"Punkt",punkt)
randpunkte += 1
#print(punkte)

def gausstrapez(points):
    area = 0
    for (y1, x1), (y2, x2) in zip(points, points[1:] + [points[0]]):
        area += x1 * y2 - x2 * y1
    return area / 2
#print("Randpunkte",randpunkte)
fiji2 = int(gausstrapez(punkte))
#print("Area",fiji2)
fiji2 += int(randpunkte)

print("Lösung Aufgabe 18.1: " + str(fiji1))
print("Lösung Aufgabe 18.2: " + str(fiji2))
print("Grüße von Fiji :^)")