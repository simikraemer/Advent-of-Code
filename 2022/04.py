x1 = 0
x2 = 0

with open("AdventofCode2022/input/04.txt", "r") as file:
    inhalt = file.read().strip()
    zeilen = inhalt.split("\n")

    for zeile in zeilen:
        links, rechts = zeile.split(",")
        start1, ende1 = map(int, links.split("-"))
        start2, ende2 = map(int, rechts.split("-"))

        if (start1 <= start2 and ende1 >= ende2) or (start2 <= start1 and ende2 >= ende1):
            x1 += 1

        if not (ende1 < start2 or ende2 < start1):
            x2 += 1

print(x1)
print(x2)
