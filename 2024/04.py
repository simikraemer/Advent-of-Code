with open("AdventofCode2024/input/04.txt", "r") as file:
    lines = file.readlines()
    array = [list(line.strip()) for line in lines]

ziel = "XMAS"
ziellänge = len(ziel)
zeilenlänge = len(array)
spaltenlänge = len(array[0])

richtungen = [
    (0, 1),   # Rechts
    (0, -1),  # Links
    (1, 0),   # Unten
    (-1, 0),  # Oben
    (1, 1),   # Dia R U
    (-1, -1), # Dia L O
    (1, -1),  # Dia L U
    (-1, 1)   # Dia R O
]

counter1 = 0
counter2 = 0

# Aufgabe 1: Schleife über alle Werte des Arrays
# Suche nach Startpunkt "X", dann Überprüfung nach Zielwort in alle 8 Richtungen
for zeile in range(zeilenlänge):
    for spalte in range(spaltenlänge):
        if array[zeile][spalte] == "X":
            for richtung in richtungen:
                match = True
                for i in range(ziellänge):
                    next_zeile = zeile + i * richtung[0]
                    next_spalte = spalte + i * richtung[1]
                    
                    # Noch innerhalb des Arrays?
                    if next_zeile < 0 or next_zeile >= zeilenlänge or next_spalte < 0 or next_spalte >= spaltenlänge:
                        match = False
                        break
                    
                    # Passt der Buchstabe?
                    if array[next_zeile][next_spalte] != ziel[i]:
                        match = False
                        break
                
                # Alle Buchstaben überprüft: Wort passt
                if match:
                    counter1 += 1
                    
# Aufgabe 2: Schleife nur über Werte, die nicht am direkten Rand liegen
# Suche nach Mittelpunkt des Musters "A", dann Überprüfung der Umgebung
for zeile in range(1, zeilenlänge - 1):
    for spalte in range(1, spaltenlänge - 1):
        if array[zeile][spalte] != "A":
            continue

        # Werte der relevanten Umgebung definieren
        o_l = array[zeile - 1][spalte - 1]
        o_r = array[zeile - 1][spalte + 1]
        u_l = array[zeile + 1][spalte - 1]
        u_r = array[zeile + 1][spalte + 1]
        
        # Unschön überprüfen ob einer der vier möglichen Muster trifft
        if (o_l, o_r, u_l, u_r) == ("M", "M", "S", "S") or \
           (o_l, o_r, u_l, u_r) == ("S", "S", "M", "M") or \
           (o_l, o_r, u_l, u_r) == ("M", "S", "M", "S") or \
           (o_l, o_r, u_l, u_r) == ("S", "M", "S", "M"):
            counter2 += 1

print("Aufgabe 1: " + str(counter1))
print("Aufgabe 2: " + str(counter2))