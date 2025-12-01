import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap, to_hex

def parse_input(lines):
    grid = {}
    boxes = []  # Liste der Boxen als Tupel
    commands = []
    parsing_grid = True

    for y, line in enumerate(lines):
        line = line.strip()
        if line == "":
            parsing_grid = False
            continue
        if parsing_grid:
            new_x = 0
            for x, char in enumerate(line):
                if char == "#":
                    grid[(new_x, y)] = "#"
                    grid[(new_x + 1, y)] = "#"
                elif char == ".":
                    grid[(new_x, y)] = "."
                    grid[(new_x + 1, y)] = "."
                elif char == "@":
                    grid[(new_x, y)] = "@"
                    grid[(new_x + 1, y)] = "."
                elif char == "O":
                    grid[(new_x, y)] = "["
                    grid[(new_x + 1, y)] = "]"
                    boxes.append(((new_x, y), (new_x + 1, y)))
                new_x += 2
        else:
            commands.extend(list(line))

    return grid, boxes, commands


def find_connected_boxes(initial_box, boxes, direction):
    dx, dy = direction
    connected_boxes = {initial_box}
    to_check = [initial_box]

    while to_check:
        current_box = to_check.pop()
        left, right = current_box

        for box in boxes:
            if box in connected_boxes:
                continue  # Bereits geprüft

            box_left, box_right = box

            # Prüfe Verbindung basierend auf der Bewegungsrichtung
            if dx != 0:  # Horizontalbewegung
                if box_left[1] == left[1] and box_left[0] == right[0] + 1:  # Rechts angrenzend
                    connected_boxes.add(box)
                    to_check.append(box)
                elif box_right[1] == right[1] and box_right[0] == left[0] - 1:  # Links angrenzend
                    connected_boxes.add(box)
                    to_check.append(box)

            elif dy != 0:  # Vertikalbewegung
                # Ganz aufliegend
                if (box_left[0] == left[0] and box_left[1] == left[1] + dy) and \
                (box_right[0] == right[0] and box_right[1] == right[1] + dy):  # Unten angrenzend
                    connected_boxes.add(box)
                    to_check.append(box)
                elif (box_left[0] == left[0] and box_left[1] == left[1] - dy) and \
                    (box_right[0] == right[0] and box_right[1] == right[1] - dy):  # Oben angrenzend
                    connected_boxes.add(box)
                    to_check.append(box)
                    
                # Halb aufliegend
                elif dy == -1 and (box_left[0] == left[0] - 1 or box_left[0] == left[0] + 1) and \
                     box_right[1] == left[1] - 1:
                    connected_boxes.add(box)
                    to_check.append(box)
                elif dy == 1 and (box_left[0] == left[0] - 1 or box_left[0] == left[0] + 1) and \
                     box_left[1] == right[1] + 1:
                    connected_boxes.add(box)
                    to_check.append(box)

    return connected_boxes


def can_move_boxes(grid, boxes, direction):
    dx, dy = direction
    box_positions = {pos for box in boxes for pos in box}  # Alle aktuellen Positionen der Boxen

    for box in boxes:
        left, right = box

        # Zielpositionen für die aktuelle Box berechnen
        next_left = (left[0] + dx, left[1] + dy)
        next_right = (right[0] + dx, right[1] + dy)

        # Prüfe, ob Zielpositionen blockiert sind
        if (grid.get(next_left) in ["#", "["] and next_left not in box_positions) or \
           (grid.get(next_right) in ["#", "]"] and next_right not in box_positions):
            return False

    return True


def move_boxes(grid, all_boxes, moving_boxes, direction):
    dx, dy = direction
    updated_boxes = []  # Liste für alle Kisten (verschoben und nicht verschoben)

    for box in all_boxes:
        if box in moving_boxes:  # Verschieben, wenn die Box in der Liste der bewegten Boxen ist
            left, right = box
            next_left = (left[0] + dx, left[1] + dy)
            next_right = (right[0] + dx, right[1] + dy)

            # Aktualisiere das Grid
            grid[next_left] = "["
            grid[next_right] = "]"
            grid[left] = "."
            grid[right] = "."

            # Füge die neue Position der verschobenen Box hinzu
            updated_boxes.append((next_left, next_right))
        else:
            # Unveränderte Box bleibt erhalten
            updated_boxes.append(box)

    return updated_boxes


def simulate_robot(grid, boxes, commands):
    """
    Führt die Bewegung des Roboters anhand der Kommandos aus.
    Wenn der Roboter eine Kiste schiebt, bewegt er sich mit.
    Visualisiert die Bewegungen mit einer Animation.
    """
    directions = {
        '<': (-1, 0),  # Links
        '>': (1, 0),   # Rechts
        '^': (0, -1),  # Oben
        'v': (0, 1),   # Unten
    }

    # Log-Datei öffnen
    log_file = open("AdventofCode2024/output/15_log.txt", "w")

    def log(message):
        """Schreibt eine Nachricht in die Log-Datei."""
        log_file.write(message + "\n")

    # Roboterposition finden
    robot_position = next((pos for pos, char in grid.items() if char == '@'), None)
    if not robot_position:
        raise ValueError("Robot position '@' not found in the grid.")

    frames = [(grid.copy(), boxes.copy())]

    for i, command in enumerate(commands, start=1):
        log(f"\nStep {i}: Executing command '{command}'")
        dx, dy = directions[command]
        new_pos = (robot_position[0] + dx, robot_position[1] + dy)
        log(f"DEBUG: Robot attempting to move to {new_pos} (dx={dx}, dy={dy})")

        # Wand-Kollision
        if grid.get(new_pos) == "#":
            log(f"DEBUG: Robot hit a wall at {new_pos}. Skipping.")
            frames.append((grid.copy(), boxes.copy()))
            continue

        # Prüfen, ob der Roboter eine Box schiebt
        adjacent_box = next((box for box in boxes if new_pos in box), None)

        # Wenn keine Box gefunden wird
        if not adjacent_box:
            if grid.get(new_pos) == ".":  # Freies Feld
                grid[robot_position] = "."
                grid[new_pos] = "@"
                robot_position = new_pos
            frames.append((grid.copy(), boxes.copy()))
            continue

        # Wenn eine Box gefunden wird
        log(f"DEBUG: Robot is attempting to push a box at {adjacent_box}.")
        connected_boxes = find_connected_boxes(adjacent_box, boxes, (dx, dy))
        log(f"DEBUG: Connected boxes to move: {connected_boxes}")
        if can_move_boxes(grid, connected_boxes, (dx, dy)):
            log("DEBUG: Boxes can be moved. Proceeding with movement.")
            boxes = move_boxes(grid, boxes, connected_boxes, (dx, dy))  # Verbundene Boxen bewegen
            log("DEBUG: Boxes moved successfully.")
            # Roboter bewegt sich mit der Kiste
            grid[robot_position] = "."
            robot_position = new_pos
            grid[robot_position] = "@"
        else:
            log("DEBUG: Boxes cannot be moved. Movement blocked.")
        frames.append((grid.copy(), boxes.copy()))

    animate_grid(frames, commands)

    log_file.close()
    
    print("Aufgabe 2:", gps_sum(boxes))

    return grid, boxes


def animate_grid(frames, commands):
    fig, ax = plt.subplots()
    ax.axis('off')

    max_x = max(coord[0] for frame in frames for coord in frame[0].keys())
    max_y = max(coord[1] for frame in frames for coord in frame[0].keys())

    temp_grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    colors = [
        "white",  # 0 Frei
        "black",  # 1 Wand
        "white",# 2 Robby Roboter
    ]

    cmap = plt.cm.prism
    num_boxes = len(frames[0][1])
    box_colors = [to_hex(cmap(i / max(1, num_boxes - 1))) for i in range(num_boxes)]
    colors.extend(box_colors)

    custom_cmap = ListedColormap(colors)

    max_value = len(colors) - 1

    grid_image = ax.imshow(temp_grid, cmap=custom_cmap, interpolation="nearest", vmin=0, vmax=max_value)

    command_text = ax.text(
        0, 0, "", ha="center", va="center", fontsize=12, color="black", weight="bold"
    )

    def update(frame_index):
        grid, boxes = frames[frame_index]
        command = commands[frame_index] if frame_index < len(commands) else "None"

        temp_grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

        for (x, y), char in grid.items():
            if char == "#":
                temp_grid[y][x] = 1  # Wand
            elif char == ".":
                temp_grid[y][x] = 0  # Frei
            elif char == "@":
                temp_grid[y][x] = 2  # Robby Roboter

                command_text.set_position((x, y))
                command_text.set_text(command)

        for i, box in enumerate(boxes, start=3):
            left, right = box
            temp_grid[left[1]][left[0]] = i
            temp_grid[right[1]][right[0]] = i

        grid_image.set_data(temp_grid)
        return [grid_image, command_text]

    ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=1, blit=True)
    figManager = plt.get_current_fig_manager()
    figManager.full_screen_toggle()
    plt.show()


def gps_sum(boxes):
    total_sum = 0

    for box in boxes:
        left, _ = box

        # Entfernung der Box von der oberen und linken Kante
        distance_from_top = left[1]
        distance_from_left = left[0]

        # GPS-Koordinate für diese Box berechnen
        gps = 100 * distance_from_top + distance_from_left
        total_sum += gps

    return total_sum


with open("AdventofCode2024/input/15.txt", "r") as file:
    lines = file.readlines()

grid, boxes, commands = parse_input(lines)

simulate_robot(grid, boxes, commands)