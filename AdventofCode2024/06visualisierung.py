import matplotlib.pyplot as plt
import numpy as np

def visualize_guard_fast(array, guard_pos, besuchte_koord, richtung_index, step):
    if step % 20 != 0:
        return
    plt.clf()
    nrows, ncols = len(array), len(array[0])
    blockaden = np.zeros((nrows, ncols))
    for x in range(nrows):
        for y in range(ncols):
            if array[x][y] == "#":
                blockaden[x, y] = 1
    plt.imshow(blockaden, cmap="Reds", origin="upper", interpolation="none")
    if besuchte_koord:
        besuchte_coords = np.array(list(besuchte_koord))
        plt.scatter(besuchte_coords[:, 1], besuchte_coords[:, 0], c="red", s=5, alpha=0.5)
    if guard_pos:
        px, py = guard_pos
        guard_char = "^>v<"[richtung_index]
        plt.text(py, px, guard_char, ha="center", va="center", fontsize=10, color="red")
    plt.axis("off")
    plt.pause(0.01)

def simulate_guard_fast(array, startkoord, richtungen, aufgabe2=False):
    x, y = startkoord
    richtung_index = 0
    besuchte_koord = set()
    besuchte_koord_mit_richtung = set()
    step = 0
    while True:
        besuchte_koord.add((x, y))
        visualize_guard_fast(array, (x, y), besuchte_koord, richtung_index, step)
        step += 1
        if aufgabe2:
            aktuelle_position = (x, y, richtung_index)
            if aktuelle_position in besuchte_koord_mit_richtung:
                return True
            besuchte_koord_mit_richtung.add(aktuelle_position)
        dx, dy = richtungen[richtung_index]
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= len(array) or ny < 0 or ny >= len(array[0]):
            break
        if array[nx][ny] == "#":
            richtung_index = (richtung_index + 1) % len(richtungen)
        else:
            x, y = nx, ny
    return len(besuchte_koord) if not aufgabe2 else False

with open("AdventofCode2024/input/06.txt", "r") as file:
    lines = file.readlines()
    array = [list(line.strip()) for line in lines]

richtungen = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

startkoord = None
for row in range(len(array)):
    for col in range(len(array[0])):
        if array[row][col] == "^":
            startkoord = (row, col)
            break
    if startkoord:
        break

plt.ion()
plt.figure(figsize=(8, 8))

dist_koord = simulate_guard_fast(array, startkoord, richtungen)

plt.ioff()
plt.show()
