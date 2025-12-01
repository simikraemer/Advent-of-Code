import re

with open("AdventofCode2024/input/03.txt", "r") as file:
    input = file.read()

pattern = r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))"
funktionen = re.findall(pattern, input)
aufgabe1 = 0
aufgabe2 = 0
enabled = True

for funktion, x, y in funktionen:
    if funktion == "do()":
        enabled = True
    elif funktion == "don't()":
        enabled = False
    elif funktion.startswith("mul"):
        aufgabe1 += int(x) * int(y)
        if enabled:
            aufgabe2 += int(x) * int(y)


print("Aufgabe 1: " + str(aufgabe1))
print("Aufgabe 2: " + str(aufgabe2))