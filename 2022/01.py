with open("2022/input/01.txt", "r") as file:
    inhalt = file.read().strip()
    elfen = inhalt.split("\n\n")

summen = []
for elf in elfen:
    zeilen = elf.strip().split("\n")
    kalorien = [int(zeile) for zeile in zeilen]
    summen.append(sum(kalorien))

x1 = max(summen)
top_drei = sorted(summen, reverse=True)[:3]
x2 = sum(top_drei)

print(x1)
print(x2)
