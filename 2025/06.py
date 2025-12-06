matrix = []
from pathlib import Path
with open(Path(__file__).resolve().parent / "input" / "06.txt", "r") as file:
    lines = file.readlines()
    for line in lines:   
        line = line.strip()
        line = " ".join(line.split())
        for i, eintrag in enumerate(line.split(" ")):
            if eintrag == "":
                continue
            matrix.append((i, eintrag))
    
maxi = 0
matrix = sorted(matrix)
for thomastupel in matrix:
    if thomastupel[0] > maxi:
        maxi = thomastupel[0]
      
i = 0  
aufgabe1 = 0
while i <= maxi:
    erstereintrag = True
    for thomastupel in matrix:
        si, eintrag = thomastupel
        if i != si:
            continue
        if erstereintrag:
            operator = eintrag
            if operator == "+":
                senkrechte = 0
            else:
                senkrechte = 1
            erstereintrag = False
            continue
        if operator == "+":
            senkrechte += int(eintrag)
        elif operator == "*":
            senkrechte *= int(eintrag)
    aufgabe1 += senkrechte
    i += 1
            
aufgabe2 = 0
    
matrix = []
for line in lines:
    senkrechte = []
    for eintrag in line:
        senkrechte.append(eintrag)
    matrix.append(senkrechte)
    
ops = []
for operatortuple in enumerate(matrix[-1]):
    if operatortuple[1] == "+" or operatortuple[1] == "*":
        ops.append((operatortuple))

for i, operatortuple in enumerate(ops):
    bereichstart = operatortuple[0]
    if operatortuple[1] == "+":
        zwischen = 0
    elif operatortuple[1] == "*":
        zwischen = 1
    if i < len(ops) - 1:
        bereichende = ops[i+1][0] - 2
    else:
        bereichende = len(matrix[0])-2
    for x in range(bereichstart, bereichende + 1):
        verenazahlsen = []
        for y in range(0,len(lines)-1):
            verenazahlsen.append(matrix[y][x])
        if operatortuple[1] == "+":
            zwischen += int(''.join(verenazahlsen))
        elif operatortuple[1] == "*":
            zwischen *= int(''.join(verenazahlsen))
        
    aufgabe2 += zwischen
    
print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")