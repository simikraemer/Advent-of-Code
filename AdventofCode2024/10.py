from collections import deque

def pfadfinder(array, startpunkt, endpunkte, aufgabe):
    zeilen = len(array)
    spalten = len(array[0])
    richtungen = [
        (-1, 0),  # Oben
        (0, 1),   # Rechts
        (1, 0),   # Unten
        (0, -1),  # Links
    ]
    warteschlange = deque([(startpunkt[0], startpunkt[1], int(array[startpunkt[0]][startpunkt[1]]))])  # (x, y, zeichen)
    if aufgabe == 1:
        besucht = set() 
        score = 0
    elif aufgabe == 2:
        rating = 0

    while warteschlange:
        x, y, wert = warteschlange.popleft()

        for dx, dy in richtungen:
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < zeilen and 0 <= ny < spalten and # Innerhalb
                (aufgabe == 2 or (nx, ny) not in besucht) and  # Für Aufgabe 1: Nur unbesuchte Felder valid
                int(array[nx][ny]) == wert + 1  # Vom Zahlenwert um 1 aufsteigender Weg
            ):
                warteschlange.append((nx, ny, int(array[nx][ny])))
                if aufgabe == 1:
                    besucht.add((nx, ny))

                if (nx, ny) in endpunkte:
                    if aufgabe == 1:
                        score += 1
                    elif aufgabe == 2:
                        rating += 1

    if aufgabe == 1:
        return score
    elif aufgabe == 2:
        return rating


with open("AdventofCode2024/input/10.txt", "r") as file:
    lines = file.readlines()
    array = [list(line.strip()) for line in lines]

startkoord = []
endkoord = []

for x, zeile in enumerate(array):
    for y, zeichen in enumerate(zeile):
        if zeichen == "0":
            startkoord.append((x, y))
        elif zeichen == "9":
            endkoord.append((x, y))

# Aufgabe 1
counter1 = 0
for startpunkt in startkoord:
    counter1 += pfadfinder(array, startpunkt, endkoord, aufgabe=1)
print("Aufgabe 1:", counter1)

# Aufgabe 2
counter2 = 0
for startpunkt in startkoord:
    counter2 += pfadfinder(array, startpunkt, endkoord, aufgabe=2)
print("Aufgabe 2:", counter2)
