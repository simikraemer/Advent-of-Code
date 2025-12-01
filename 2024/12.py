def finde_areas(array):
    zeilen = len(array)
    spalten = len(array[0])
    besucht = [[False for _ in range(spalten)] for _ in range(zeilen)]
    areas = []
    richtungen = [
        (-1, 0),  # Oben
        (0, 1),   # Rechts
        (1, 0),   # Unten
        (0, -1),  # Links
    ]

    def dfs(x, y, aktuelle_area, zeichen):
        if x < 0 or x >= zeilen or y < 0 or y >= spalten or besucht[x][y] or array[x][y] != zeichen: # Innerhalb
            return
        
        besucht[x][y] = True
        aktuelle_area.append((x, y))
        
        for dx, dy in richtungen:
            dfs(x + dx, y + dy, aktuelle_area, zeichen)

    for x in range(zeilen):
        for y in range(spalten):
            if not besucht[x][y] and array[x][y] != ".":
                aktuelle_area = []
                dfs(x, y, aktuelle_area, array[x][y])
                if aktuelle_area:
                    areas.append({
                        "zeichen": array[x][y],
                        "koordinaten": aktuelle_area
                    })

    return areas


def berechne_areas(areas, array):
    zeilen = len(array)
    spalten = len(array[0])
    richtungen = [
        (-1, 0),  # Oben
        (0, 1),   # Rechts
        (1, 0),   # Unten
        (0, -1),  # Links
    ]
    ergebnisse = []
    
    def finde_seiten(umfangs_set):
        def sind_horizontale_nachbarn(grenze1, grenze2):
            """Prüft, ob zwei Grenzen horizontal nebeneinander liegen und die Richtungen gleich sind."""
            x1, y1, dx1, dy1 = grenze1
            x2, y2, dx2, dy2 = grenze2
            return (y1 == y2) and (abs(x1 - x2) == 1) and (dx1 == dx2 and dy1 == dy2)

        def sind_vertikale_nachbarn(grenze1, grenze2):
            """Prüft, ob zwei Grenzen vertikal nebeneinander liegen und die Richtungen gleich sind."""
            x1, y1, dx1, dy1 = grenze1
            x2, y2, dx2, dy2 = grenze2
            return (x1 == x2) and (abs(y1 - y2) == 1) and (dx1 == dx2 and dy1 == dy2)

        sortiertes_set = sorted(umfangs_set, key=lambda grenze: (grenze[0], grenze[1], grenze[2], grenze[3]))

        bereits_gezählt = []
        counter = 0

        for grenze in sortiertes_set:
            fortführung_einer_seite = False

            for gezahlte_grenze in bereits_gezählt:
                if sind_horizontale_nachbarn(grenze, gezahlte_grenze) or sind_vertikale_nachbarn(grenze, gezahlte_grenze):
                    fortführung_einer_seite = True
                    break

            if not fortführung_einer_seite:
                counter += 1

            bereits_gezählt.append(grenze)

        return counter

    for area in areas:
        fläche = len(area['koordinaten'])
        umfangs_set = set()
        umfang = 0

        for x, y in area['koordinaten']:
            for dx, dy in richtungen:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= zeilen or ny < 0 or ny >= spalten:
                    umfangs_set.add((x, y, dx, dy))
                    umfang += 1
                elif array[nx][ny] != area['zeichen']:
                    umfangs_set.add((x, y, dx, dy))
                    umfang += 1

        seiten = finde_seiten(umfangs_set)

        ergebnisse.append({
            "zeichen": area['zeichen'],
            "fläche": fläche,
            "umfang": umfang,
            "seiten": seiten,
            "koordinaten": area['koordinaten']
        })

    return ergebnisse


with open("2024/input/12.txt", "r") as file:
    lines = file.readlines()
    array = [list(line.strip()) for line in lines]

areas = finde_areas(array)
ergebnisse = berechne_areas(areas, array)

counter1 = 0
for area in ergebnisse:
    counter1 += area['fläche'] * area['umfang']
print("Aufgabe 1:", counter1)
    
counter2 = 0
for area in ergebnisse:
    counter2 += area['fläche'] * area['seiten']
print("Aufgabe 2:", counter2)