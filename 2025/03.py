maxjoltages = []

from pathlib import Path
with open(Path(__file__).resolve().parent / "input" / "03.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    line = line.strip()
    stelle1 = 0
    stelle2 = 0

    for i, ziffer in enumerate(str(line)[:-1]):
        if int(ziffer) > stelle1:
            stelle1 = int(ziffer)
            position1 = i
    for i, ziffer in enumerate(str(line)[position1 + 1:]):
        if int(ziffer) > stelle2:
            stelle2 = int(ziffer)
    
    maxjoltage = int(str(stelle1) + str(stelle2))
    maxjoltages.append(maxjoltage)
        
aufgabe1 = sum(maxjoltages)


def findmaxnumber(offenestellen, line):
    stelle = 0
    if offenestellen == 1:
        bereich = str(line)
    else:
        placeholder = offenestellen - 1
        bereich = str(line)[:-placeholder]
    for i,ziffer in enumerate(bereich):
        if int(ziffer) > stelle:
            stelle = int(ziffer)
            position = i
    restline = str(line)[position + 1:]
    return stelle, restline

maxjoltages = []

for line in lines:
    line = line.strip()
    offenestellen = 12
    stellen = []

    while offenestellen > 0:
        stelle, restline = findmaxnumber(offenestellen, line)
        line = restline
        stellen.append(stelle)
        offenestellen -= 1

    maxjoltage = int("".join(str(stelle) for stelle in stellen))
    maxjoltages.append(maxjoltage)

aufgabe2 = sum(maxjoltages)

print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")