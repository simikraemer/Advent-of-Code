from collections import deque

with open("AdventofCode2023/input/11.txt", 'r') as fl:
    zeilen = fl.read().strip().split()

fiji1 = 0
fiji2 = 0
schritte_für_leere1 = 2
schritte_für_leere2 = 1000000
leere_zeilen = [i for i, zeile in enumerate(zeilen) if "#" not in zeile]
leere_spalten = [i for i in range(len(zeilen[0])) if "#" not in [zeilen[j][i] for j in range(len(zeilen))]]
universen_koord = [(y, x) for y, zeile in enumerate(zeilen) for x, zeichen in enumerate(zeile) if zeichen == "#"]

def wegfindung(start, ende, grid, leere_zeilen, leere_spalten, schritte_für_leere):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(start, 0)])
    besucht = set()

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == ende:
            return steps

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])) and (new_x in leere_zeilen or new_y in leere_spalten):
                if (new_x, new_y) not in besucht:
                    besucht.add((new_x, new_y))
                    queue.append(((new_x, new_y), steps + schritte_für_leere))
            elif 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] in ".#":
                if (new_x, new_y) not in besucht:
                    besucht.add((new_x, new_y))
                    queue.append(((new_x, new_y), steps + 1))

    raise ValueError("No Way!")

for i in range(len(universen_koord)):
    for j in range(i + 1, len(universen_koord)):
        start, ende = universen_koord[i], universen_koord[j]
        entfernung1 = wegfindung(start, ende, zeilen, leere_zeilen, leere_spalten, schritte_für_leere1)
        fiji1 += entfernung1
        entfernung2 = wegfindung(start, ende, zeilen, leere_zeilen, leere_spalten, schritte_für_leere2)
        fiji2 += entfernung2

print("Lösung Aufgabe 11.1: " + str(fiji1))
print("Lösung Aufgabe 11.2: " + str(fiji2))
print("Grüße von Fiji :^)")
