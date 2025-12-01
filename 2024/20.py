from collections import deque, defaultdict
from tqdm import tqdm

def bfs_naturpfad(grid, start, end):
    queue = deque([(start, 0, [])])
    visited = set()

    while queue:
        current, steps, path = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        path.append(current)

        if current == end:
            return path

        x, y = current
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (x + dx, y + dy)
            if neighbor in grid and grid[neighbor] != "#" and neighbor not in visited:
                queue.append((neighbor, steps + 1, path.copy()))
    return []

def noclip_simulation(grid, dauer, savinggrenze):
    start = end = None
    for coord, value in grid.items():
        if value == "S":
            start = coord
        elif value == "E":
            end = coord

    naturpfad = bfs_naturpfad(grid, start, end)
    cheat_savings = defaultdict(int)

    path_to_end_cache = {point: len(naturpfad) - i - 1 for i, point in enumerate(naturpfad)}

    progress_bar = tqdm(naturpfad, desc="Processing noclip starts")

    for i, noclip_start in enumerate(progress_bar):
        for j, noclip_end in enumerate(naturpfad[i + 1:], start=i + 1):
            distance = abs(noclip_start[0] - noclip_end[0]) + abs(noclip_start[1] - noclip_end[1])
            if distance > dauer:
                continue

            noclip_steps = distance
            steps_after_reentry = path_to_end_cache[noclip_end]
            total_noclip_steps = i + noclip_steps + steps_after_reentry
            normal_steps = len(naturpfad)

            if total_noclip_steps < normal_steps:
                savings = normal_steps - total_noclip_steps
                cheat_savings[savings] += 1

    progress_bar.close()

    counter = 0
    for savings, count in sorted(cheat_savings.items()):
        if savings > savinggrenze:
            counter += count            
    return counter


with open("2024/input/20.txt", "r") as file:
    lines = file.readlines()
    grid = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            grid[(x, y)] = char

# Aufgabe 1
noclip_dauer = 2
savinggrenze = 100
print("Aufgabe 1:",noclip_simulation(grid, noclip_dauer, savinggrenze))

# Aufgabe 2
noclip_dauer = 20
savinggrenze = 100
print("Aufgabe 2:",noclip_simulation(grid, noclip_dauer, savinggrenze))