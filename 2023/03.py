with open('2023/input/3.txt', 'r') as datei:
    source_liste = datei.readlines()
    
symbol_array = []
nummer_array = []
fiji1 = 0
fiji2 = 0

for zeilenindex, zeile in enumerate(source_liste):
    spaltenindex = 0
    while spaltenindex < len(zeile) - 1:
        if zeile[spaltenindex].isdigit():
            mehrerestellen = False
            start = spaltenindex  # Startindex der Zahl
            while spaltenindex < len(zeile) and zeile[spaltenindex].isdigit(): # Die Zahl abgehen
                mehrerestellen = True
                spaltenindex += 1 # Nach WhileSchleife -> Endindex der Zahl
            nummer = int(zeile[start:spaltenindex])
            nummer_array.append((zeilenindex, start, spaltenindex - start, nummer))
            if mehrerestellen:
                spaltenindex -= 1
        elif zeile[spaltenindex] != '.':
            symbol_array.append((zeilenindex, spaltenindex))
        
        spaltenindex += 1
        
for nummer in nummer_array:
    zeile, spalte, länge, zahlenwert = nummer
    zahlgrenztansymbol = False

    for symbol in symbol_array:
        s_zeile, s_spalte = symbol

        if (
            abs(s_zeile - zeile) <= 1 and # Symbol muss gleiche oder angrenzende Zeile sein
            (
                (s_spalte - spalte) <= länge and # Nach rechts von erster Ziffer
                (spalte - s_spalte) <= 1 # Nach links von erster Ziffer
            )
        ):
            zahlgrenztansymbol = True
            break
    
    if zahlgrenztansymbol:
        fiji1 += zahlenwert
        

for symbol in symbol_array:
    s_zeile, s_spalte = symbol
    anzahl_angrenzende_zahlen = 0
    zahlenrad_produkt = 1
        
    for nummer in nummer_array:
        zeile, spalte, länge, zahlenwert = nummer
        zahlgrenztansymbol = False

        if (
            abs(s_zeile - zeile) <= 1 and # Symbol muss gleiche oder angrenzende Zeile sein
            (
                (s_spalte - spalte) <= länge and # Nach rechts von erster Ziffer
                (spalte - s_spalte) <= 1 # Nach links von erster Ziffer
            )
        ):
            anzahl_angrenzende_zahlen += 1
            zahlenrad_produkt *= zahlenwert
            
        
    if anzahl_angrenzende_zahlen == 2:
        fiji2 += zahlenrad_produkt
        print(zahlenrad_produkt)

print("Lösung Aufgabe 3.1: ", str(fiji1))
print("Lösung Aufgabe 3.2: ", str(fiji2))
print("Grüße von Fiji :^)")
