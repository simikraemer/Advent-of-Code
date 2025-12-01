from tqdm import tqdm
from PIL import Image, ImageDraw

def parse_robos(lines):
    robos = {}
    for i, line in enumerate(lines):
        line = line.strip()

        parts = line.split()
        
        p = tuple(map(int, parts[0][2:].split(',')))
        v = tuple(map(int, parts[1][2:].split(',')))
        
        robos[f"Robo-{i+1}"] = {"p": p, "v": v}

    return robos


def anordnung_feststellen(robos, breite, höhe): # Prüft ob ein 5x5 Feld KOMPLETT mit Robos gefüllt ist
    robo_positions = set(robo["p"] for robo in robos.values()) 

    for y in range(höhe - 4):
        for x in range(breite - 4):
            if all((x + dx, y + dy) in robo_positions for dy in range(5) for dx in range(5)):
                return True

    return False


def bild_speichern(robos, sekunde, breite, höhe):
    zellengröße = 5
    image_width = breite * zellengröße
    image_height = höhe * zellengröße

    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    position_counts = {}
    for robo in robos.values():
        pos = robo["p"]
        position_counts[pos] = position_counts.get(pos, 0) + 1

    for (x, y), count in position_counts.items():
        top_left = (x * zellengröße, y * zellengröße)
        bottom_right = ((x + 1) * zellengröße - 1, (y + 1) * zellengröße - 1)
        color = (255, 0, 0) if count == 1 else (0, 0, 255)
        draw.rectangle([top_left, bottom_right], fill=color)

    output_pfad = f"AdventofCode2024/output/14 - {sekunde}s.jpg"
    image.save(output_pfad, "JPEG")


def sekunde_simulieren(robos, breite, höhe):
    for robo in robos.values():
        x, y = robo["p"]
        dx, dy = robo["v"]
        nx = (x + dx) % breite
        ny = (y + dy) % höhe
        robo["p"] = (nx, ny)


def quadranten_zählen(robos, breite, höhe):
    mid_x = breite // 2
    mid_y = höhe // 2
    
    q1, q2, q3, q4 = 0, 0, 0, 0

    for robo in robos.values():
        x, y = robo["p"]

        # Robos mittig zwischen Quadranten werden nicht gezählt
        if breite % 2 != 0 and x == mid_x:
            continue
        if höhe % 2 != 0 and y == mid_y:
            continue

        if x >= mid_x and y < mid_y:
            q1 += 1
        elif x < mid_x and y < mid_y:
            q2 += 1
        elif x < mid_x and y >= mid_y:
            q3 += 1
        elif x >= mid_x and y >= mid_y:
            q4 += 1

    result = q1 * q2 * q3 * q4

    return result


with open("AdventofCode2024/input/14.txt", "r") as file:
    lines = file.readlines()

robos = parse_robos(lines)
breite, höhe = (101,103)

print("Simuliere die sicken Robo-Moves, bis das Easter Egg gefunden wurde...")
progress_bar = tqdm(desc="Robo-Dance", unit=" Sekunden")

sekunde = 0
while True:
    # Aufgabe 1
    if sekunde == 100:
        counter1 = quadranten_zählen(robos, breite, höhe)

    # Aufgabe 2
    if anordnung_feststellen(robos, breite, höhe):
        counter2 = sekunde
        bild_speichern(robos, sekunde, breite, höhe)
        break

    sekunde_simulieren(robos, breite, höhe)

    sekunde += 1
    progress_bar.update(1)

progress_bar.close()

print("Aufgabe 1:", counter1)
print("Aufgabe 2:", counter2)