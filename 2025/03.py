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
    print(maxjoltage)
    maxjoltages.append(maxjoltage)
        
aufgabe1 = sum(maxjoltages)
aufgabe2 = 0

print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")