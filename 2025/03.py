maxjoltages = []

with open("2025/input/03.txt", "r") as file:
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
    restline = ""
    if offenestellen > 0:
        restline = str(line)[:-offenestellen]
    else:
        restline = str(line)
    for i,ziffer in enumerate(restline):
        if int(ziffer) > stelle:
            stelle = int(ziffer)
            position = i
    restline = str(line)[position + 1:]
    return stelle, restline

maxjoltages = []

for line in lines:
    line = line.strip()
    offenestellen = 11
    stellen = []

    while offenestellen > -1:
        stelle, restline = findmaxnumber(offenestellen, line)
        line = restline
        stellen.append(stelle)
        offenestellen -= 1

    maxjoltage = int("".join(str(stelle) for stelle in stellen))
    maxjoltages.append(maxjoltage)

aufgabe2 = sum(maxjoltages)

print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")