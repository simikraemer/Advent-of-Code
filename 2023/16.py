import sys

fiji1 = 0
fiji2 = 0

with open("2023/input/16.txt", "r") as fl:
    lines = fl.readlines()
    plattform = tuple(tuple(line.strip()) for line in lines)

besucht = []    
richtungen = [(-1, 0), (0, -1), (1, 0), (0, 1)]
#                N        W        S       O

def laser(plattform, position, richtung):
    stillstand = False
    while not stillstand:
        if ((position),(richtung)) in besucht:
            break
        
        y, x = position
        dy, dx = richtung
        new_y, new_x = y + dy, x + dx
        new_position = (new_y, new_x)  
        
        if (position[0] > -1 and position[1] > -1) and\
           (position[0] < len(plattform) and position[1] < len(plattform[0])):
            besucht.append((position, richtung))     
        
        if 0 <= new_y < len(plattform) and 0 <= new_x < len(plattform[0]):     
        
            if plattform[new_y][new_x] == "|" and (richtung == (0, 1) or richtung == (0, -1)):
                new_richtung1 = (-1, 0)
                new_richtung2 = (1, 0)
                richtung = new_richtung1
                position = new_position  
                laser(plattform,new_position,new_richtung2)
                        
            elif plattform[new_y][new_x] == "-" and (richtung == (-1, 0) or richtung == (1, 0)):
                new_richtung1 = (0, -1)
                new_richtung2 = (0, 1)
                richtung = new_richtung1
                position = new_position  
                laser(plattform,new_position,new_richtung2)

            elif plattform[new_y][new_x] == "-" and (richtung == (0, 1) or richtung == (0, -1)) or\
               plattform[new_y][new_x] == "|" and (richtung == (-1, 0) or richtung == (1, 0)) or\
               plattform[new_y][new_x] == ".":
                position = new_position  

            elif plattform[new_y][new_x] == "/" and richtung == (0, 1) or\
               plattform[new_y][new_x] == "\\" and richtung == (0, -1):
                new_richtung = (-1, 0)
                richtung = new_richtung
                position = new_position 

            elif plattform[new_y][new_x] == "/" and richtung == (0, -1) or\
               plattform[new_y][new_x] == "\\" and richtung == (0, 1):
                new_richtung = (1, 0)
                richtung = new_richtung
                position = new_position  

            elif plattform[new_y][new_x] == "/" and richtung == (1, 0) or\
               plattform[new_y][new_x] == "\\" and richtung == (-1, 0):
                new_richtung = (0, -1)
                richtung = new_richtung
                position = new_position  

            elif plattform[new_y][new_x] == "/" and richtung == (-1, 0) or\
               plattform[new_y][new_x] == "\\" and richtung == (1, 0):
                new_richtung = (0, 1)
                richtung = new_richtung
                position = new_position  
            
            
        else:
            stillstand = True
                        
position = (0, -1)
richtung = (0, 1)
laser(plattform,position,richtung)
distinkt_koord = set()
for eintrag in besucht:
    distinkt_koord.add(eintrag[0])
fiji1 = len(distinkt_koord)


energieteile = []
anzahl_zeilen = len(plattform)
anzahl_spalten = len(plattform[0])

counter = 0
vor_progress = -1
for zeileidx in range(anzahl_zeilen):
    position = (zeileidx, -1)
    richtung = (0, 1)
    laser(plattform,position,richtung)
    distinkt_koord = set()
    for eintrag in besucht:
        distinkt_koord.add(eintrag[0])
    energieteile.append(len(distinkt_koord))
    besucht = []
    distinkt_koord = set()
    
    position = (zeileidx, anzahl_spalten)
    richtung = (0, -1)
    laser(plattform,position,richtung)
    for eintrag in besucht:
        distinkt_koord.add(eintrag[0])
    energieteile.append(len(distinkt_koord))
    besucht = []
    
    
    counter += 1
    progress = (counter / anzahl_zeilen) * 100
    akt_progress = int(progress)
    if akt_progress != vor_progress:
        vor_progress = akt_progress
        sys.stdout.write("\r")
        sys.stdout.write(f"Fortschritt Aufgabe 2 Waagerecht: [{'=' * akt_progress}{' ' * (100 - akt_progress)}] {akt_progress}%")
        sys.stdout.flush()
print(" - Abgeschlossen")
    
counter = 0
vor_progress = -1
for spalteidx in range(anzahl_spalten):
    position = (-1, spalteidx)
    richtung = (1, 0)
    laser(plattform,position,richtung)
    distinkt_koord = set()
    for eintrag in besucht:
        distinkt_koord.add(eintrag[0])
    energieteile.append(len(distinkt_koord))
    besucht = []
    
    position = (anzahl_zeilen, spalteidx)
    richtung = (-1, 0)
    laser(plattform,position,richtung)
    distinkt_koord = set()
    for eintrag in besucht:
        distinkt_koord.add(eintrag[0])    
    energieteile.append(len(distinkt_koord))
    besucht = []
    
    counter += 1
    progress = (counter / anzahl_spalten) * 100
    akt_progress = int(progress)
    if akt_progress != vor_progress:
        vor_progress = akt_progress
        sys.stdout.write("\r")
        sys.stdout.write(f"Fortschritt Aufgabe 2 Senkrecht: [{'=' * akt_progress}{' ' * (100 - akt_progress)}] {akt_progress}%")
        sys.stdout.flush()
print(" - Abgeschlossen")

fiji2 = max(energieteile)
    
print("Lösung Aufgabe 16.1: " + str(fiji1))
print("Lösung Aufgabe 16.2: " + str(fiji2))
print("Grüße von Fiji :^)")