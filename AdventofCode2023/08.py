import math
with open("AdventofCode2023/input/8.txt", "r") as datei:
    source_liste = datei.readlines()

gesamtarray = []
firstline = True
for eintrag in source_liste:
    if firstline:
        anweisungen = eintrag.rstrip()
        firstline = False

for eintrag in source_liste[2:]:
    eintrag_geteilt = eintrag.rstrip().split("=")
    zer0 = eintrag_geteilt[0][:3]
    un0 = eintrag_geteilt[1][2:5]
    tw0 = eintrag_geteilt[1][7:10]
    eintragarray = [zer0, un0, tw0]
    gesamtarray.append(eintragarray)


aktuelle_position = "AAA"
fiji1 = 0
while not aktuelle_position.endswith("Z"):
    for ziffer in anweisungen:
        fiji1 += 1
        if ziffer == "L":
            for eintrag in gesamtarray:
                if eintrag[0] == aktuelle_position:
                    aktuelle_position = eintrag[1]
                    break
        elif ziffer == "R":
            for eintrag in gesamtarray:
                if eintrag[0] == aktuelle_position:
                    aktuelle_position = eintrag[2]
                    break
                
start_positionen = [eintrag[0] for eintrag in gesamtarray if eintrag[0].endswith("A")]
benötigte_schritte = []
for aktuelle_position in start_positionen:
    fiji2 = 0
    while not aktuelle_position.endswith("Z"):
        for ziffer in anweisungen:
            fiji2 += 1
            if ziffer == "L":
                for eintrag in gesamtarray:
                    if eintrag[0] == aktuelle_position:
                        aktuelle_position = eintrag[1]
                        break
            elif ziffer == "R":
                for eintrag in gesamtarray:
                    if eintrag[0] == aktuelle_position:
                        aktuelle_position = eintrag[2]
                        break
    benötigte_schritte.append(fiji2)
fiji2 = math.lcm(*benötigte_schritte)

print("Lösung Aufgabe 8.1: " + str(fiji1))
print("Lösung Aufgabe 8.2: " + str(fiji2))
print("Grüße von Fiji :^)")