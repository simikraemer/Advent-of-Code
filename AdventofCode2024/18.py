from collections import deque

def coordinates_to_grid(coordinates, grid_size, byte_limit):
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
    for x, y in coordinates[:byte_limit]:
        grid[y][x] = "#"
    return grid

def find_shortest_path(grid):
    grid_size = len(grid)
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)

    if grid[0][0] == "#" or grid[grid_size - 1][grid_size - 1] == "#":
        print("Start oder Ziel blockiert.")
        return -1 

    directions = [
    (-1, 0),   # Oben
    (1, 0),   # Unten
    (0, -1),  # Links
    (0, 1)  # Rechts
    ]
    queue = deque([(start, 0, [start])])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), steps, path = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[ny][nx] == "." and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1, path + [(nx, ny)]))

    return -1  # Kein Pfad gefunden

def find_blocking_coordinate(coordinates, grid_size, ugrenze, ogrenze):
    def is_path_possible(byte_limit):
        grid = coordinates_to_grid(coordinates, grid_size, byte_limit)
        return find_shortest_path(grid) != -1  # Weg noch möglich

    last_valid_bytes = ugrenze
    while ugrenze < ogrenze:
        mid = (ugrenze + ogrenze + 1) // 2
        if is_path_possible(mid):
            ugrenze = mid
            last_valid_bytes = mid
        else:
            ogrenze = mid - 1

    if not is_path_possible(last_valid_bytes + 1):
        return coordinates[last_valid_bytes]
    
with open("AdventofCode2024/input/18.txt", "r") as file:
    coordinates = [tuple(map(int, line.strip().split(','))) for line in file.readlines()]

# Aufgabe 1
grid = coordinates_to_grid(coordinates, grid_size = 71, byte_limit = 1024)
schritte = find_shortest_path(grid)
print("Aufgabe 1:", schritte)

# Aufgabe 2
letzte_koords = find_blocking_coordinate(coordinates, grid_size = 71, ugrenze = 1024, ogrenze = 3450)
print(f"Aufgabe 2: {letzte_koords[0]},{letzte_koords[1]}")