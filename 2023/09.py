with open("2023/input/9.txt", "r") as datei:
    source_liste = datei.readlines()
    
fiji1 = 0
fiji2 = 0

for eintrag in source_liste:
    zahlenfolge = [int(zahl) for zahl in eintrag.strip().split()]
    allesnull = False
    allezahlenfolgendeseintrag = []
    
    while not allesnull:
        allezahlenfolgendeseintrag.append(zahlenfolge)
        zahlenfolge = [zahlenfolge[i + 1] - zahlenfolge[i] for i in range(len(zahlenfolge) - 1)]
        allesnull = all(zahl == 0 for zahl in zahlenfolge)
    
    for idx in range(len(allezahlenfolgendeseintrag) - 1, 0, -1):
        aktuelle_sequenz = allezahlenfolgendeseintrag[idx]
        obere_sequenz = allezahlenfolgendeseintrag[idx - 1]
        nächste_zahl_obere_seq = obere_sequenz[-1] + aktuelle_sequenz[-1]
        obere_sequenz.append(nächste_zahl_obere_seq)
    
    fiji1 += nächste_zahl_obere_seq
    
    for idx in range(len(allezahlenfolgendeseintrag) - 1, 0, -1):
        aktuelle_sequenz = allezahlenfolgendeseintrag[idx]
        obere_sequenz = allezahlenfolgendeseintrag[idx - 1]
        vorderste_zahl_obere_seq = obere_sequenz[0] - aktuelle_sequenz[0]
        obere_sequenz.insert(0, vorderste_zahl_obere_seq)
        
    fiji2 += vorderste_zahl_obere_seq

print("Lösung Aufgabe 9.1: " + str(fiji1))
print("Lösung Aufgabe 9.2: " + str(fiji2))
print("Grüße von Fiji :^)")