with open("2024/input/08.txt", "r") as file:
    lines = file.readlines()
    array = [list(line.strip()) for line in lines]

schwingungsbäuche1 = set()
schwingungsbäuche2 = set()

for zeichen in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
    positionen = [(x, y) for x in range(len(array)) for y in range(len(array[0])) if array[x][y] == zeichen]

    for i in range(len(positionen)):
        for j in range(i + 1, len(positionen)):
            x1, y1 = positionen[i]
            x2, y2 = positionen[j]

            dx = x2 - x1
            dy = y2 - y1
            
            ### Aufgabe 1 ###
            for nx, ny in [(x1 - dx, y1 - dy), (x2 + dx, y2 + dy)]: # Jeweils von Koordinate i und j eine Abstandslänge nach außen
                if 0 <= nx < len(array) and 0 <= ny < len(array[0]): # Innerhalb
                    schwingungsbäuche1.add((nx, ny))
            
            ### Aufgabe 2 ###            
            for richtung in (-1,1): # Von einer Koordinate i aus erst in negative, dann positive Richtung über alle ganzzahligen Faktoren
                faktor = 0
                while True:
                    nx = x1 + (faktor * richtung * dx)
                    ny = y1 + (faktor * richtung * dy)
                    if 0 <= nx < len(array) and 0 <= ny < len(array[0]): # Innerhalb
                        schwingungsbäuche2.add((nx, ny))
                    else:
                        break
                    faktor += 1

print(f"Aufgabe 1: {len(schwingungsbäuche1)}")
print(f"Aufgabe 2: {len(schwingungsbäuche2)}")