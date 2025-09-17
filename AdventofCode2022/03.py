def buchstabe2wert(buchstabe):
    if buchstabe.islower():
        return ord(buchstabe) - ord("a") + 1
    else:
        return ord(buchstabe) - ord("A") + 27

x1_items = []
x2_items = []

with open("AdventofCode2022/input/03.txt", "r") as file:
    inhalt = file.read().strip()
    rucksäcke = inhalt.split("\n")

    for rucksack in rucksäcke:
        mitte = len(rucksack) // 2
        fach1 = set(rucksack[:mitte])
        fach2 = set(rucksack[mitte:])
        x1_items.extend(fach1 & fach2)

    for i in range(0, len(rucksäcke), 3):
        elfentruppe = rucksäcke[i:i+3]
        schnittmenge = set(elfentruppe[0]) & set(elfentruppe[1]) & set(elfentruppe[2])
        x2_items.extend(schnittmenge)

x1 = sum(buchstabe2wert(buchstabe) for buchstabe in x1_items)
x2 = sum(buchstabe2wert(buchstabe) for buchstabe in x2_items)

print(x1)
print(x2)