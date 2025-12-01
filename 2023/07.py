with open("2023/input/7.txt", "r") as datei:
    source_liste = datei.readlines()
    
hände = []

for eintrag in source_liste:
    eintrag_geteilt = eintrag.rstrip().split(" ")
    werte = ([zeichen for zeichen in eintrag_geteilt[0]])
    werte = (werte, eintrag_geteilt[1])
    hände.append(werte)
    


kartenwerte = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

vergleichshände = []

for hand in hände:
    werte, bid = hand
    wert_anzahl = {}
    hand_info = {"prio": 0, "kartenwerte": [], "bid": bid}
    for wert in werte:
        if wert in wert_anzahl:
            wert_anzahl[wert] += 1
        else:
            wert_anzahl[wert] = 1
    
    sortierte_anzahlen = sorted(wert_anzahl.values(), reverse=True)
    höchste_anzahl = max(wert_anzahl.values())
    zweithöchste_anzahl = sortierte_anzahlen[1] if len(sortierte_anzahlen) > 1 else sortierte_anzahlen[0]
    
    if höchste_anzahl == 5:
        hand_info["prio"] = 6
    elif höchste_anzahl == 4:
        hand_info["prio"] = 5
    elif höchste_anzahl == 3 and zweithöchste_anzahl == 2:
        hand_info["prio"] = 4
    elif höchste_anzahl == 3:
        hand_info["prio"] = 3
    elif höchste_anzahl == 2 and zweithöchste_anzahl == 2:
        hand_info["prio"] = 2
    elif höchste_anzahl == 2:
        hand_info["prio"] = 1

    if "kartenwerte" not in hand_info:
        hand_info["kartenwerte"] = []
    
    for karte in werte:
        hand_info["kartenwerte"].append(kartenwerte[karte])
    
    vergleichshände.append(hand_info)
    

vergleichshände.sort(key=lambda hand: (hand["prio"], hand["kartenwerte"]))

ränge = {}
current_rank = len(vergleichshände)
fiji1 = 0
for index, hand in enumerate(vergleichshände[::-1]):
    ränge[len(vergleichshände) - index - 1] = current_rank
    if index < len(vergleichshände) - 1:
        fiji1 += int(hand["bid"]) * int(current_rank)
        if hand["prio"] != vergleichshände[len(vergleichshände) - index - 2]["prio"] or hand["kartenwerte"] != vergleichshände[len(vergleichshände) - index - 2]["kartenwerte"]:
            current_rank -= 1
fiji1 += int(hand["bid"]) * int(current_rank)

kartenwerte = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1
}

vergleichshände = []

for hand in hände:
    werte, bid = hand
    wert_anzahl = {}
    anzahl_joker = 0
    for wert in werte:
        if wert != "J":
            if wert in wert_anzahl:
                wert_anzahl[wert] += 1
            else:
                wert_anzahl[wert] = 1
        else:
            anzahl_joker += 1
    
    nicht_joker_anzahlen = [anzahl for wert, anzahl in wert_anzahl.items() if wert != "J"]
    sortierte_anzahlen = sorted(nicht_joker_anzahlen, reverse=True)
    höchste_anzahl = 0
    zweithöchste_anzahl = 0

    if sortierte_anzahlen:
        höchste_anzahl = sortierte_anzahlen[0]
        if len(sortierte_anzahlen) > 1:
            zweithöchste_anzahl = sortierte_anzahlen[1]
    
    hand_info = {"prio": 0, "kartenwerte": [], "bid": bid, "joker": anzahl_joker}
    
    if höchste_anzahl + anzahl_joker == 5:
        hand_info["prio"] = 6
    elif höchste_anzahl + anzahl_joker == 4:
        hand_info["prio"] = 5
    elif (höchste_anzahl == 3 and zweithöchste_anzahl == 2) or \
         (höchste_anzahl == 2 and zweithöchste_anzahl == 2 and anzahl_joker == 1):
        hand_info["prio"] = 4
    elif höchste_anzahl + anzahl_joker == 3:
        hand_info["prio"] = 3
    elif (höchste_anzahl == 2 and zweithöchste_anzahl == 2) or \
        (höchste_anzahl == 2 and zweithöchste_anzahl + anzahl_joker == 2):
        hand_info["prio"] = 2
    elif höchste_anzahl + anzahl_joker == 2:
        hand_info["prio"] = 1

    if "kartenwerte" not in hand_info:
        hand_info["kartenwerte"] = []
    
    for karte in werte:
        hand_info["kartenwerte"].append(kartenwerte[karte])
    
    vergleichshände.append(hand_info)

vergleichshände.sort(key=lambda hand: (hand["prio"], hand["kartenwerte"]))

ränge = {}
current_rank = len(vergleichshände)
endhände = []
for index, hand in enumerate(vergleichshände[::-1]):
    hand_info = {"prio": hand["prio"], "kartenwerte": hand["kartenwerte"], "bid": hand["bid"], "joker": hand["joker"], "rang": 0}
    ränge[len(vergleichshände) - index - 1] = current_rank
    hand_info["rang"] = current_rank
    if index < len(vergleichshände) - 1:
        if hand["prio"] != vergleichshände[len(vergleichshände) - index - 2]["prio"] or hand["kartenwerte"] != vergleichshände[len(vergleichshände) - index - 2]["kartenwerte"]:
            current_rank -= 1
    endhände.append(hand_info)
    
fiji2 = 0
for hand in endhände:
    fiji2 += int(hand["bid"]) * int(hand["rang"])


print("Lösung Aufgabe 7.1: ", str(fiji1))
print("Lösung Aufgabe 7.2: ", str(fiji2))
print("Grüße von Fiji :^)")
