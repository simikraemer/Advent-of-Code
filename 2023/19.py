import time
from itertools import product

fiji1 = 0
fiji2 = 0

oberer_teil = []
unterer_teil = []
unterer_teil_values = []

upper_complete = False

with open("2023/input/19.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            upper_complete = True
            continue
        if not upper_complete:
            oberer_teil.append(line)
        else:
            unterer_teil.append(line)
            values = line.replace("{", "").replace("}", "").split(",")
            value_dict = {}
            for val in values:
                key, value = val.split("=")
                value_dict[key.strip()] = int(value)
            tuple_values = (value_dict["x"], value_dict["m"], value_dict["a"], value_dict["s"])
            unterer_teil_values.append(tuple_values)

#print("Obere Sektion:")
#print(oberer_teil)
#print("\nUntere Sektion:")
#print(unterer_teil)
#print("\nUntere Sektion als Tupel:")
#print(unterer_teil_values)

def stringinbedingung(string):
    teil = string.split("}")[0]
    bedingung = {}
    buchstabe = teil[0]
    vergleichsoperator = teil[1]
    vergleichswert, rest = teil[2:].split(":", 1)
    wenntrue, wennfalse = rest.split(",", 1)
    bedingung = {
        "titel": zeilentitel,
        "buchstabe": buchstabe,
        "operator": vergleichsoperator,
        "wert": int(vergleichswert),
        "wenntrue": wenntrue,
        "wennfalse": wennfalse
    }
    return bedingung
    
bedingungen = []
for zeile in oberer_teil:
    zeilenteile = zeile.split("{")
    zeilentitel = zeilenteile[0]
    bedingungen.append(stringinbedingung(zeilenteile[1]))

def workflow(zeile, titel):
    bedingung = next((bedingung for bedingung in bedingungen if bedingung["titel"] == titel), None)
    print("Bedingung:",bedingung)
    return check(zeile,bedingung)
            
def check(zeile, bedingung):
    if bedingung["buchstabe"] == "x":
        wert = zeile[0]
    elif bedingung["buchstabe"] == "m":
        wert = zeile[1]
    elif bedingung["buchstabe"] == "a":
        wert = zeile[2]
    elif bedingung["buchstabe"] == "s":
        wert = zeile[3]
        
    if bedingung["operator"] == ">":
        if wert > bedingung["wert"]:
            if bedingung["wenntrue"] == "A":
                return True
            elif bedingung["wenntrue"] == "R":
                return False
            else:
                return workflow(zeile, bedingung["wenntrue"])
        else:
            if ">" in bedingung["wennfalse"] or "<" in bedingung["wennfalse"]:
                bedingung = stringinbedingung(bedingung["wennfalse"])
                return check(zeile,bedingung)
            if bedingung["wennfalse"] == "A":
                return True
            elif bedingung["wennfalse"] == "R":
                return False
            else:
                return workflow(zeile, bedingung["wennfalse"])
    elif bedingung["operator"] == "<":
        if wert < bedingung["wert"]:
            if bedingung["wenntrue"] == "A":
                return True
            elif bedingung["wenntrue"] == "R":
                return False
            else:
                return workflow(zeile, bedingung["wenntrue"])
        else:
            if ">" in bedingung["wennfalse"] or "<" in bedingung["wennfalse"]:
                bedingung = stringinbedingung(bedingung["wennfalse"])
                return check(zeile,bedingung)
            if bedingung["wennfalse"] == "A":
                return True
            elif bedingung["wennfalse"] == "R":
                return False
            else:
                return workflow(zeile, bedingung["wennfalse"])
            
            
starttitel = "in"
for zeile in unterer_teil_values:
    bool = workflow(zeile, starttitel)
    if bool:
        for wert in zeile:
            fiji1 += wert
            print("Fiji1 sagt",fiji1)

accepted_ranges = []

def workflow2(ranges,titel):
    bedingung = next((bedingung for bedingung in bedingungen if bedingung["titel"] == titel), None)
    #print("Bedingung:",bedingung)
    #print("Ranges",ranges)
    print("Titel:",titel)
    return check2(ranges,bedingung)
            
def check2(ranges,bedingung):
    buchstaben_idx = {"x": 0, "m": 1, "a": 2, "s": 3}
    wertidx = buchstaben_idx.get(bedingung["buchstabe"])
    min_val, max_val = ranges[wertidx]
    print(ranges,anzahlderranges(ranges))
    print("Bedingung",bedingung)
        
    if bedingung["operator"] == ">":
        trueranges = list(ranges)
        falseranges = list(ranges)
        newtrue1 = max(bedingung["wert"] + 1, min_val)
        newtrue2 = max_val
        newfalse1 = min_val
        newfalse2 = min(bedingung["wert"] + 1, max_val)
        trueranges[wertidx] = (newtrue1, newtrue2)
        falseranges[wertidx] = (newfalse1, newfalse2)
        print(trueranges,anzahlderranges(trueranges))
        print(falseranges,anzahlderranges(falseranges))
        
        if bedingung["wenntrue"] == "A":
            print("> - Accepted true:",anzahlderranges(trueranges))
            accepted_ranges.append(trueranges)
        elif bedingung["wenntrue"] == "R":
            print("> - Rejected true:",anzahlderranges(trueranges))
        else:
            print("> - Weiter an true",bedingung["wenntrue"],":",anzahlderranges(trueranges))
            workflow2(trueranges,bedingung["wenntrue"])
            
        if ">" in bedingung["wennfalse"] or "<" in bedingung["wennfalse"]:
            print("> - Innere Schleife Titel:",bedingung["titel"]," Ranges:",anzahlderranges(falseranges))
            new_bedingung = stringinbedingung(bedingung["wennfalse"])
            print("Innere Schleife Titel:",bedingung["titel"])
            check2(falseranges,new_bedingung)
        elif bedingung["wennfalse"] == "A":
            print("> - Accepted false:",anzahlderranges(falseranges))
            accepted_ranges.append(falseranges)
        elif bedingung["wennfalse"] == "R":
            print("> - Rejected false:",anzahlderranges(falseranges))
            return None
        else:
            print("> - Weiter an false",bedingung["wennfalse"],":",anzahlderranges(falseranges))
            workflow2(falseranges,bedingung["wennfalse"])
        
        
    elif bedingung["operator"] == "<":
        trueranges = list(ranges)
        falseranges = list(ranges)
        newtrue1 = min_val
        newtrue2 = min(bedingung["wert"], max_val)
        newfalse1 = min(bedingung["wert"], max_val)
        newfalse2 = max_val
        #print(newtrue1,newtrue2)
        #print(newfalse1,newfalse2)
        trueranges[wertidx] = (newtrue1, newtrue2)
        falseranges[wertidx] = (newfalse1, newfalse2)
        print(trueranges,anzahlderranges(trueranges))
        print(falseranges,anzahlderranges(falseranges))

        if bedingung["wenntrue"] == "A":
            print("< - Accepted true:",anzahlderranges(trueranges))
            accepted_ranges.append(trueranges)
        elif bedingung["wenntrue"] == "R":
            print("< - Rejected true:",anzahlderranges(trueranges))
        else:
            print("< - Weiter an true",bedingung["wenntrue"],":",anzahlderranges(trueranges))
            workflow2(trueranges,bedingung["wenntrue"])
            
        if ">" in bedingung["wennfalse"] or "<" in bedingung["wennfalse"]:
            print("< - Innere Schleife Titel:",bedingung["titel"]," Ranges:",anzahlderranges(falseranges))
            new_bedingung = stringinbedingung(bedingung["wennfalse"])
            check2(falseranges,new_bedingung)
        elif bedingung["wennfalse"] == "A":
            print("< - Accepted false:",anzahlderranges(falseranges))
            accepted_ranges.append(falseranges)
        elif bedingung["wennfalse"] == "R":
            print("< - Rejected false:",anzahlderranges(falseranges))
            return None
        else:
            print("< - Weiter an false",bedingung["wennfalse"],":",anzahlderranges(falseranges))
            workflow2(falseranges,bedingung["wennfalse"])
        
    print()

def anzahlderranges(ranges):
    produkt = 1
    for range in ranges:
        anzahl = range[1] - range[0]
        produkt *= anzahl
    return produkt

starttitel = "in"
ranges = [(1, 4001), (1, 4001), (1, 4001), (1, 4001)]
workflow2(ranges,starttitel)


for axxranges in accepted_ranges:
    produkt = 1
    for range in axxranges:
        anzahl = range[1] - range[0]
        produkt *= anzahl
    fiji2 += produkt



print("Lösung Aufgabe 19.1: " + str(fiji1))
print("Lösung Aufgabe 19.2: " + str(fiji2))
print("Grüße von Fiji :^)")