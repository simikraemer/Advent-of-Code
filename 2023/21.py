from functools import cache

fiji1 = 0
fiji2 = 0

data = []

with open("2023/input/21.txt", "r") as file:
    for zeile in file:
        data.append(zeile.strip())

def findstartpos():
    for y, zeile in enumerate(data):
        for x, char in enumerate(zeile):
            if char == "S":
                pos = [(y,x)]
                return pos

def main(schrittziel):
    pos = findstartpos()
    schritte = 0
    while schritte < schrittziel:
        npos = set()
        schritte += 1
        for p in pos:
            np = findnewpos(p)
            #print("NP",np)
            npos.update(np)
        pos = list(npos)
        #print("position am mainende",pos)
    #print(pos)
    return len(pos)
          
@cache
def findnewpos(p):
    np = []
    #print("Position in findnewpos:",p)
    richtungen = [(0,1), (0,-1), (1,0), (-1,0)]
    for r in richtungen:
        #print("npx Rechnung:",r[0] , p[0], r[1] , p[1])
        npx = (r[0] + p[0], r[1] + p[1])
        if 0 <= npx[0] < len(data) and 0 <= npx[1] < len(data[0]):
            if data[npx[0]][npx[1]] != "#":
                np.append(npx)
    return np

startposition = []
schrittziel = 64
fiji1 = main(schrittziel)

#---------------------------------
# Aufgabe 2
#---------------------------------

# 26501365 = 65 + (202300 * 131)

def kantenfinder(type):
    schrittziel = 200
    schrittmin = 65
    pos = findstartpos()
    schritte = 0
    positions_and_steps = {}
    while schritte < schrittziel:
        npos = set()
        schritte += 1
        for p in pos:
            np = findnewpos(p)
            #print("NP",np)
            npos.update(np)
            for new_p in np:
                if new_p not in positions_and_steps:
                    positions_and_steps[new_p] = schritte

        pos = list(npos)
    
    if type == "gerade":
        count = sum(1 for pos, steps in positions_and_steps.items() if steps % 2 == 0 and steps > schrittmin)
    elif type == "ungerade":
        count = sum(1 for pos, steps in positions_and_steps.items() if steps % 2 != 0 and steps > schrittmin)

    return count

n = 202300
gerader_block = main(200)
ungerader_block = main(201)
gerade_kante = kantenfinder("gerade")
ungerade_kante = kantenfinder("ungerade")

alle_geraden_blöcke = (n ** 2) * gerader_block
alle_ungeraden_blöcke = ((n + 1) ** 2) * ungerader_block
alle_geraden_kanten = n * gerade_kante
alle_ungeraden_kanten = (n+1) * ungerade_kante

fiji2 = alle_geraden_blöcke + alle_ungeraden_blöcke + alle_geraden_kanten - alle_ungeraden_kanten

print("Lösung Aufgabe 21.1: " + str(fiji1))
print("Lösung Aufgabe 21.2: " + str(fiji2))
print("Grüße von Fiji :^)")