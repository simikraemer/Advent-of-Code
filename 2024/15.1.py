def parse_input(lines):
    grid = {}
    commands = []
    parsing_grid = True

    for y, line in enumerate(lines):
        line = line.strip()
        if line == "":
            parsing_grid = False
            continue
        if parsing_grid:
            for x, char in enumerate(line):
                grid[(x, y)] = char 
        else:
            commands.extend(list(line))

    return grid, commands
    

def simulate_robot(grid, commands):
    directions = {
        '<': (-1, 0),  # Links
        '>': (1, 0),   # Rechts
        '^': (0, -1),  # Oben
        'v': (0, 1),   # Unten
    }

    robot_position = next((pos for pos, char in grid.items() if char == '@'), None)
    
    for i, command in enumerate(commands, 1):        
        if command not in directions:
            continue
        
        dx, dy = directions[command]
        new_pos = (robot_position[0] + dx, robot_position[1] + dy)
        
        if grid.get(new_pos) == '.':
            grid[robot_position] = '.'
            grid[new_pos] = '@'
            robot_position = new_pos
        
        elif grid.get(new_pos) == 'O':
            current_pos = new_pos
            to_move = []
            
            while grid.get(current_pos) == 'O':
                to_move.append(current_pos)
                current_pos = (current_pos[0] + dx, current_pos[1] + dy)
            
            if grid.get(current_pos) == '.':
                for pos in reversed(to_move):
                    next_pos = (pos[0] + dx, pos[1] + dy)
                    grid[next_pos] = 'O'
                grid[robot_position] = '.'
                grid[new_pos] = '@'
                robot_position = new_pos

    return grid


def calculate_gps_sum(grid):
    """
    Berechnet die GPS_SUM basierend auf den Box-Koordinaten im Grid.
    Die Formel lautet: (y * 100 + x) für jede Box 'O'.
    """
    gps_sum = 0

    for (x, y), value in grid.items():
        if value == 'O':
            gps_sum += y * 100 + x

    return gps_sum


with open("2024/input/15.txt", "r") as file:
    lines = file.readlines()

grid, commands = parse_input(lines)

updated_grid = simulate_robot(grid, commands)

gps_sum = calculate_gps_sum(grid)
print("GPS_SUM:", gps_sum)