import matplotlib.pyplot as plt
import numpy as np

def visualize_array(array, i_pos, j_pos, schwingungsbäuche2, zeichen):
    plt.clf()
    nrows, ncols = len(array), len(array[0])
    
    plt.imshow(np.zeros((nrows, ncols)), cmap="Greys", origin="upper")
    for x in range(nrows):
        for y in range(ncols):
            if array[x][y] != ".":
                plt.text(y, x, array[x][y], ha="center", va="center", fontsize=10, color="black")
    
    if i_pos:
        plt.scatter(i_pos[1], i_pos[0], c="green", label="i-Position", s=1000, alpha=0.3)
    if j_pos:
        plt.scatter(j_pos[1], j_pos[0], c="blue", label="j-Position", s=1000, alpha=0.3)

    if i_pos and j_pos:
        x_vals = [i_pos[1], j_pos[1]]
        y_vals = [i_pos[0], j_pos[0]]
        plt.plot(x_vals, y_vals, color="black", alpha=1, linewidth=1)

    schwingungsbäuche2_coords = np.array(list(schwingungsbäuche2))
    if len(schwingungsbäuche2_coords) > 0:
        plt.scatter(schwingungsbäuche2_coords[:, 1], schwingungsbäuche2_coords[:, 0], 
                    c="red", label="Schwingungsbäuche 2", s=50, alpha = 0.5)
    
    plt.title(f"Aktuelles Zeichen: {zeichen}", fontsize=30)
    plt.pause(0.001)


with open("2024/input/08.txt", "r") as file:
    lines = file.readlines()
    array = [list(line.strip()) for line in lines]

schwingungsbäuche2 = set()

plt.ion()
plt.figure(figsize=(8, 8))

for zeichen in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
    positionen = [(x, y) for x in range(len(array)) for y in range(len(array[0])) if array[x][y] == zeichen]

    for i in range(len(positionen)):
        for j in range(i + 1, len(positionen)):
            x1, y1 = positionen[i]
            x2, y2 = positionen[j]

            dx = x2 - x1
            dy = y2 - y1

            visualize_array(array, (x1, y1), (x2, y2), schwingungsbäuche2, zeichen)

            ### Aufgabe 2 ###
            for richtung in (-1, 1):
                faktor = 0
                while True:
                    nx = x1 + (faktor * richtung * dx)
                    ny = y1 + (faktor * richtung * dy)
                    if 0 <= nx < len(array) and 0 <= ny < len(array[0]):
                        schwingungsbäuche2.add((nx, ny))
                        visualize_array(array, (x1, y1), (x2, y2), schwingungsbäuche2, zeichen)
                    else:
                        break
                    faktor += 1

plt.ioff()
plt.show()
