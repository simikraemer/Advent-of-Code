with open("AdventofCode2024/input/05.txt", "r") as file:
    lines = file.readlines()

rules = []
updates = []
abschnittswechsel = False

for line in lines:
    line = line.strip()
    if line == "":
        abschnittswechsel = True
        continue

    if abschnittswechsel:
        updates.append(list(map(int, line.split(','))))
    else:
        rules.append(tuple(map(int, line.split('|'))))
        
counter1 = 0
counter2 = 0

for update in updates:
    aufgabe2 = False

    while True: # Bis alle Regeln eingehalten wurden
        valid = True
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    update.remove(rule[0])
                    update.insert(update.index(rule[1]), rule[0])
                    valid = False
                    aufgabe2 = True
        if valid:
            break

    mittelindex = len(update) // 2

    if aufgabe2:
        counter2 += update[mittelindex]
    else:
        counter1 += update[mittelindex]
                
print("Aufgabe 1: " + str(counter1))
print("Aufgabe 2: " + str(counter2))