with open('2023/input/4.txt', 'r') as datei:
    source_liste = datei.readlines()
    
fiji1 = 0

for eintrag in source_liste:
    eintrag_geteilt = eintrag.split(": ")
    karteID = eintrag_geteilt[0].split()[1]
    nummern_geteilt = eintrag_geteilt[1].split(" | ")
    siegnum_string = nummern_geteilt[0]
    losnum_string = nummern_geteilt[1]
    siegnum = [int(num) for num in nummern_geteilt[0].split()]
    losnum = [int(num) for num in nummern_geteilt[1].split()]
    
    punkte = 0
    for num in losnum:
        if num in siegnum:
            if punkte >= 1:
                punkte *= 2
            else:
                punkte = 1
    fiji1 += punkte

alle_karten = {}

for eintrag in source_liste:
    eintrag_geteilt = eintrag.split(": ")
    karteID = eintrag_geteilt[0].split()[1]
    alle_karten[karteID] = 1

for eintrag in source_liste:
    eintrag_geteilt = eintrag.split(": ")
    karteID = eintrag_geteilt[0].split()[1]
    nummern_geteilt = eintrag_geteilt[1].split(" | ")
    siegnum_string = nummern_geteilt[0]
    losnum_string = nummern_geteilt[1]
    siegnum = [int(num) for num in nummern_geteilt[0].split()]
    losnum = [int(num) for num in nummern_geteilt[1].split()]
    
    treffer = 0
    for num in losnum:
        if num in siegnum:
            treffer += 1
            
    for betroffene_karten in range(int(karteID) + 1, int(karteID) + treffer + 1):
        alle_karten[f"{betroffene_karten}"] += 1 * alle_karten[karteID]
    
fiji2 = 0
for kartenID in alle_karten:
    fiji2 += alle_karten[kartenID]

print("Lösung Aufgabe 4.1: ", str(fiji1))
print("Lösung Aufgabe 4.2: ", str(fiji2))
print("Grüße von Fiji :^)")