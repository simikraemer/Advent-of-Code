from collections import defaultdict, deque

fiji1 = 0
fiji2 = 0

with open("2023/input/17.txt", "r") as file:
    zeilen = file.read().strip().split("\n")
    plattform = [[int(digit) for digit in row] for row in zeilen]

def ergebnis(minmap):
    results = []
    for y, x, ausrichtung in minmap:
        if y == anzahl_zeilen - 1 and x == anzahl_spalten - 1:
            results.append(minmap[y, x, ausrichtung])
    return min(results)

def minmap(schrittrange):
    for min_schritte, max_schritte in schrittrange:
        minmap = defaultdict(lambda:1000)
        queue = deque()
        start_summe = 0
        start_y = 0
        start_x = 0
        queue.appendleft((start_y, start_x, "O", start_summe))
        queue.appendleft((start_y, start_x, "S", start_summe))

        while queue:
            y, x, richtung, summen = queue.pop()
            ausrichtung = gleiche_ausrichtung[richtung]
            
            vorherigerminwert = minmap[y, x, ausrichtung]
            if vorherigerminwert <= summen:
                continue

            minmap[(y, x, ausrichtung)] = summen
            for new_richtung in orthogonale_ausrichtung[richtung]:
                summe = 0
                dy, dx = richtungen[new_richtung]
                new_y, new_x = y, x

                for schritte in range(1, max_schritte + 1):
                    new_y += dy
                    new_x += dx
                    if 0 <= new_y < anzahl_zeilen and 0 <= new_x < anzahl_spalten:
                        summe += plattform[new_y][new_x]
                        if schritte >= min_schritte:
                            queue.appendleft((new_y, new_x, new_richtung, summen + summe))
        return minmap
    
orthogonale_ausrichtung = {"N":"WO", "S":"WO", "W":"NS", "O": "NS"}
gleiche_ausrichtung = {"N":"NS", "S":"NS", "W":"WO", "O":"WO"}
richtungen = {"N":(-1, 0), "S":(1, 0), "W":(0, -1), "O":(0, 1)}

anzahl_zeilen = len(zeilen)
anzahl_spalten = len(zeilen[0])

minmap1 = minmap([(1, 3)])
fiji1 += ergebnis(minmap1)
minmap2 = minmap([(4, 10)])
fiji2 += ergebnis(minmap2)

print("Lösung Aufgabe 17.1: " + str(fiji1))
print("Lösung Aufgabe 17.2: " + str(fiji2))
print("Grüße von Fiji :^)")