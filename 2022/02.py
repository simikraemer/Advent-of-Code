x1_wert_zug = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

x1_wert_ergebnis = {
    ("A", "X"): 3,
    ("A", "Y"): 6,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("B", "Y"): 3,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("C", "Y"): 0,
    ("C", "Z"): 3
}

x2_wert_ergebnis = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

x2_wert_zug = {
    ("A", "X"): 3,
    ("A", "Y"): 1,
    ("A", "Z"): 2,
    ("B", "X"): 1,
    ("B", "Y"): 2,
    ("B", "Z"): 3,
    ("C", "X"): 2,
    ("C", "Y"): 3,
    ("C", "Z"): 1
}

x1 = 0
x2 = 0

with open("2022/input/02.txt", "r") as file:
    inhalt = file.read().strip()
    runden = inhalt.split("\n")
    for runde in runden:
        zug_gegner, zug_moi = runde.strip().split(" ")
        x1 += x1_wert_zug[zug_moi] + x1_wert_ergebnis[(zug_gegner, zug_moi)]
        x2 += x2_wert_ergebnis[zug_moi] + x2_wert_zug[(zug_gegner, zug_moi)]

print(x1)
print(x2)