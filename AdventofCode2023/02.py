with open('AdventofCode2023/input/2.txt', 'r') as datei:
    source_liste = datei.readlines()
    
maximale_bälle_nach_farbe = {'red': 12, 'green': 13, 'blue': 14}
fiji1 = 0
fiji2 = 0

for eintrag in source_liste:
    eintrag_geteilt = eintrag.split(": ")
    
    gameID = eintrag_geteilt[0].split()[1]
    allebälle_und_farben = eintrag_geteilt[1].split('; ')
    anzahl_nach_farben = {'red': 0, 'green': 0, 'blue': 0}

    for farbe_und_anzahl in allebälle_und_farben:
        bälle_in_einer_hand = farbe_und_anzahl.split(', ')
        for bälle_in_einer_hand_von_einer_farbe_LMAO in bälle_in_einer_hand:
            anzahl, farbe = bälle_in_einer_hand_von_einer_farbe_LMAO.split() # anzahl | farbe
            anzahl = int(anzahl)
            if anzahl > anzahl_nach_farben[farbe]:
                anzahl_nach_farben[farbe] = anzahl

    möglich = True
    for farbe in anzahl_nach_farben:
        if anzahl_nach_farben[farbe] > maximale_bälle_nach_farbe[farbe]:
            möglich = False
            break
    if möglich:
        fiji1 += int(gameID)
        
    power = 1
    for farbe in anzahl_nach_farben:
        power *= anzahl_nach_farben[farbe]
    fiji2 += power

print("Lösung Aufgabe 2.1: ", str(fiji1))
print("Lösung Aufgabe 2.2: ", str(fiji2))
print("Grüße von Fiji :^)")