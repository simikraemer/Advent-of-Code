from itertools import product
from collections import deque

# Helper functions
def is_valid_move(position, keypad, danger_zone):
    return position in keypad.values() and position != danger_zone


from functools import lru_cache

# Caching für find_paths
@lru_cache(maxsize=None)
def find_paths(start_pos, target_pos, keypad_items, danger_zone):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    queue = deque([(start_pos, "")])
    paths = []
    shortest_length = float('inf')

    while queue:
        current_pos, path = queue.popleft()

        # Skip if the path is already longer than the shortest found
        if len(path) > shortest_length:
            continue

        # If the target position is reached
        if current_pos == target_pos:
            if len(path) < shortest_length:
                shortest_length = len(path)
                paths = [path]
            elif len(path) == shortest_length:
                paths.append(path)
            continue

        # Explore all valid directions
        for move, (dy, dx) in directions.items():
            new_pos = (current_pos[0] + dy, current_pos[1] + dx)
            if new_pos in keypad_items and new_pos != danger_zone:
                queue.append((new_pos, path + move))

    return tuple(paths)  # Convert to tuple for caching compatibility

def find_all_sequences(start_pos, codes, numpad, digipad, danger_zones):
    sequences = [(start_pos, "")]
    cache = {}

    # Convert keypads to hashable frozenset
    numpad_items = frozenset(numpad.values())

    for char in codes:
        target_pos = numpad[char]
        new_sequences = []
        for current_pos, path_so_far in sequences:
            # Generate a cache key
            cache_key = (current_pos, target_pos, danger_zones[0])

            # Use cache if available, otherwise compute paths
            if cache_key not in cache:
                cache[cache_key] = find_paths(current_pos, target_pos, numpad_items, danger_zones[0])
            paths = cache[cache_key]

            # Extend the sequences with the cached paths
            for path in paths:
                new_sequences.append((target_pos, path_so_far + path + 'A'))
        sequences = new_sequences

    return [seq[1] for seq in sequences]



def calculate_complexity(code, path_length):
    numeric_part = int(''.join(filter(str.isdigit, code)))
    return numeric_part * path_length

def calculate_total_complexity(lines, numpad, digipad, start_positions, danger_zones):
    total_complexity = 0

    for code in lines:
        # Step 1: Robo1
        robo1_sequences = set(find_all_sequences(start_positions[0], code, numpad, digipad, danger_zones))
        min_length_robo1 = min(len(seq) for seq in robo1_sequences)
        shortest_robo1 = next(seq for seq in robo1_sequences if len(seq) == min_length_robo1)
        print(f"Shortest Robo1 Path for {code}: {shortest_robo1}")

        # Step 2: Robo2
        robo2_sequences = set()
        for robo1_path in robo1_sequences:
            robo2_sequences.update(find_all_sequences(start_positions[1], robo1_path, digipad, digipad, danger_zones))
        min_length_robo2 = min(len(seq) for seq in robo2_sequences)
        shortest_robo2 = next(seq for seq in robo2_sequences if len(seq) == min_length_robo2)
        print(f"Shortest Robo2 Path for {code}: {shortest_robo2}")

        # Step 3: Robo3
        robo3_sequences = set()
        counterrobo3 = 0
        for robo2_path in robo2_sequences:
            counterrobo3 += 1
            robo3_sequences.update(find_all_sequences(start_positions[2], robo2_path, digipad, digipad, danger_zones))
        min_length_robo3 = min(len(seq) for seq in robo3_sequences)
        shortest_robo3 = next(seq for seq in robo3_sequences if len(seq) == min_length_robo3)
        print(f"Shortest Robo3 Path for {code}: {shortest_robo3}")

        # Calculate complexity for the shortest path
        total_complexity += calculate_complexity(code, len(shortest_robo3))

    return total_complexity



# Configuration
NUMPAD = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    '0': (3, 1), 'A': (3, 2)
}

DIGIPAD = {
    '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2)
}

start_positions = [(3, 2), (0, 2), (0, 2)]
danger_zones = [(3, 0), (0, 0), (0, 0)]

with open("2024/input/21.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

result = calculate_total_complexity(lines, NUMPAD, DIGIPAD, start_positions, danger_zones)
print(result)
