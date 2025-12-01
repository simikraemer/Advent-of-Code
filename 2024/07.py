from itertools import product

def prüfe_berechnung(wunschergebnis, zahlenmaterial, operatoren):
    operationskombi = product(operatoren, repeat=len(zahlenmaterial) - 1)
    for operationskombo in operationskombi:
        ergebnis = zahlenmaterial[0]
        for i, operation in enumerate(operationskombo):
            if operation == "+":
                ergebnis += zahlenmaterial[i + 1]
            elif operation == "*":
                ergebnis *= zahlenmaterial[i + 1]
            elif operation == "||":
                ergebnis = int(str(ergebnis) + str(zahlenmaterial[i + 1]))
        if ergebnis == wunschergebnis:
            return True
    return False

with open("2024/input/07.txt", "r") as file:
    lines = file.readlines()

counter1 = 0
counter2 = 0

for idx, line in enumerate(lines, start=1):
    print(str(idx) + "/" + str(len(lines)))
    parts = line.strip().split(":")
    wunschergebnis = int(parts[0])
    zahlenmaterial = list(map(int, parts[1].split()))

    if prüfe_berechnung(wunschergebnis, zahlenmaterial, ["+", "*"]):
        counter1 += wunschergebnis
        counter2 += wunschergebnis
    elif prüfe_berechnung(wunschergebnis, zahlenmaterial, ["+", "*", "||"]):
        counter2 += wunschergebnis

print(f"Aufgabe 1: {counter1}")
print(f"Aufgabe 2: {counter2}")