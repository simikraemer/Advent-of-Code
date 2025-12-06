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
    
print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")