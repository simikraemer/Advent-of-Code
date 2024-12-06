with open("AdventofCode2024/input/06.txt", "r") as file:
    lines = file.readlines()
    array = [list(line.strip()) for line in lines]

richtungen = [
    (-1, 0),  # Oben
    (0, 1),   # Rechts
    (1, 0),   # Unten
    (0, -1),  # Links
]

# Startpunkt finden
startkoord = None
for row in range(len(array)):
    for col in range(len(array[0])):
        if array[row][col] == "^":
            startkoord = (row, col)
            break
    if startkoord:
        break

# Bewegungslogik
x, y = startkoord
richtung_index = 0  # Senkrechtstarter
besuchte_koord = set()

while True:
    besuchte_koord.add((x, y))
    
    # Nächstes Feld berechnen
    dx, dy = richtungen[richtung_index]
    nx, ny = x + dx, y + dy

    # Wenn Wache das Feld verlässt -> Abbruchbedingung
    if nx < 0 or nx >= len(array) or ny < 0 or ny >= len(array[0]):
        print(f"Wache hat das Array bei ({x}, {y}) verlassen.")
        break

    # Verhalten basierend auf dem nächsten Feld
    if array[nx][ny] == "#":
        # Nach rechts drehen
        richtung_index = (richtung_index + 1) % len(richtungen)
    else:
        # Auf nächstes Feld bewegen
        x, y = nx, ny

    print(f"Wache bewegt sich zu ({x}, {y}) in Richtung {richtungen[richtung_index]}.")

print("Aufgabe 1: " + str(len(besuchte_koord)))
#print("Aufgabe 2: " + str(counter2))