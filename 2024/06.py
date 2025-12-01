def simulate_guard(array, startkoord, richtungen, aufgabe2=False):
    x, y = startkoord
    richtung_index = 0  # Senkrechtstarter
    besuchte_koord = set()
    besuchte_koord_mit_richtung = set()

    while True:
        besuchte_koord.add((x, y))
        if aufgabe2:
            aktuelle_position = (x, y, richtung_index)
            if aktuelle_position in besuchte_koord_mit_richtung:
                return True  # Loop erkannt
            besuchte_koord_mit_richtung.add(aktuelle_position)

        dx, dy = richtungen[richtung_index]
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= len(array) or ny < 0 or ny >= len(array[0]):
            break

        # Verhalten basierend auf dem nächsten Feld
        if array[nx][ny] == "#":
            # Nach rechts drehen
            richtung_index = (richtung_index + 1) % len(richtungen)
        else:
            # Bewegen
            x, y = nx, ny

    return len(besuchte_koord) if not aufgabe2 else False

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

# Aufgabe 1
dist_koord = simulate_guard(array, startkoord, richtungen)
print("Aufgabe 1: " + str(dist_koord))

# Aufgabe 2
counter2 = 0
for row in range(len(array)):
    for col in range(len(array[0])):
        if array[row][col] == ".":
            array[row][col] = "#"
            counter2 += simulate_guard(array, startkoord, richtungen, aufgabe2=True)
            array[row][col] = "."

print("Aufgabe 2: " + str(counter2))