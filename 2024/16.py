import heapq
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def parse_input(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            grid[(x, y)] = char
    return grid


def cheapest_path(grid):
    directions = [
    (1, 0),   # Rechts
    (0, 1),   # Unten
    (-1, 0),  # Links
    (0, -1)  # Oben
    ]
    start = next(pos for pos, val in grid.items() if val == 'S')
    end = next(pos for pos, val in grid.items() if val == 'E')

    queue = [(0, start, 0, [])]  # (Kosten, Position des Rentiers, Richtungsindex, Pfad)
    visited = {}
    lowest_score = float('inf')
    visited_coordinates = set()
    all_paths = []

    while queue:
        cost, (x, y), direction, path = heapq.heappop(queue)

        # Valid oder neuer Pfad
        if (x, y, direction) in visited and visited[(x, y, direction)] < cost:
            continue
        visited[(x, y, direction)] = cost

        path = path + [((x, y), direction, cost)]

        # Alle billigsten Pfade abhandeln
        if (x, y) == end:
            if cost < lowest_score:
                lowest_score = cost
                visited_coordinates.clear()
                all_paths.clear()
            if cost == lowest_score:
                visited_coordinates.update((pos[0], pos[1]) for pos, _, _ in path)
                all_paths.append(path)
            continue  # Nach dem Endfeld gehts nicht weiter

        # Schritt vor
        dx, dy = directions[direction]
        forward_pos = (x + dx, y + dy)
        if grid.get(forward_pos) in {'.', 'E'}:
            heapq.heappush(queue, (cost + 1, forward_pos, direction, path))

        # Drehen links
        left_direction = (direction - 1) % 4
        heapq.heappush(queue, (cost + 1000, (x, y), left_direction, path))

        # Drehen rechts
        right_direction = (direction + 1) % 4
        heapq.heappush(queue, (cost + 1000, (x, y), right_direction, path))

    return lowest_score, visited_coordinates, all_paths


def animate_paths(grid, paths):
    max_x = max(x for x, y in grid.keys()) + 1
    max_y = max(y for x, y in grid.keys()) + 1

    grid_array = np.zeros((max_y, max_x))
    for (x, y), val in grid.items():
        if val == '.':
            grid_array[y, x] = 0  # Frei
        elif val == '#':
            grid_array[y, x] = 1  # Wand
        elif val == 'S':
            grid_array[y, x] = 2  # Start
        elif val == 'E':
            grid_array[y, x] = 3  # Ende

    cmap = {
        0: (1.0, 1.0, 1.0),  # Weiß - Frei
        1: (0.0, 0.0, 0.0),  # Schwarz - Wand
        2: (0.0, 0.0, 1.0),  # Blau - Start
        3: (0.0, 1.0, 0.0),  # Grün - Ende
        4: (1.0, 0.0, 0.0),  # Rot - Rentier Rudolf mit der roten Nase
        5: (0.8, 0.8, 0.0),  # Gelb - Besucht
    }

    fig, ax = plt.subplots()
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')  # Fenster maximieren
    img = ax.imshow(
        np.zeros((*grid_array.shape, 3)),
        interpolation='nearest'
    )

    visited_cells = set()

    def update(frame):
        grid_copy = grid_array.copy()
        active_positions = set()

        for path in paths:
            if frame < len(path):
                x, y = path[frame][0]
                active_positions.add((x, y))

        visited_cells.update(active_positions)
        for x, y in visited_cells:
            grid_copy[y, x] = 5  # Grey - Besucht
        for x, y in active_positions:
            grid_copy[y, x] = 4  # Blue - Rentier

        color_mapped_grid = np.zeros((*grid_copy.shape, 3))
        for value, color in cmap.items():
            color_mapped_grid[grid_copy == value] = color

        img.set_data(color_mapped_grid)
        return img,

    max_frames = max(len(path) for path in paths)

    ani = animation.FuncAnimation(fig, update, frames=max_frames, interval=3, blit=True)

    plt.axis('off')
    plt.show()


with open("2024/input/16.txt", "r") as file:
    lines = file.readlines()

grid = parse_input(lines)
score, visited, paths = cheapest_path(grid)

print("Aufgabe 1:", score)
print("Aufgabe 2:", len(visited))

animate_paths(grid, paths)