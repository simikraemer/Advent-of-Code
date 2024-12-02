def übersetzen(von_werte, mappings):
    translated_seeds = []
    for von_wert in von_werte:
        wert_im_mapping = False
        for row in mappings:
            if von_wert in range(row[1],row[1]+row[2]):
                zu_wert = von_wert - row[1] + row[0]
                translated_seeds.append(zu_wert)
                wert_im_mapping = True
                break
        
        if not wert_im_mapping:
            zu_wert = von_wert
            translated_seeds.append(zu_wert)
    
    return translated_seeds    

maps = {}
aktuelle_map = None

with open('input/5.txt', 'r') as datei:
    zeilen = datei.readlines()
    for zeile in zeilen:
        zeile = zeile.strip()
        if zeile.startswith("seeds:"):
            maps['seeds'] = list(map(int, zeile.split(':')[1].split()))
        elif zeile.endswith("map:"):
            aktuelle_map = zeile.replace(" map:", "")
            maps[aktuelle_map] = []
        elif zeile:
            maps[aktuelle_map].append(list(map(int, zeile.split())))
    
map_liste = ['seeds', 'seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

translated_seeds = maps['seeds']  # Die ursprünglichen Seeds
for map_name in map_liste[1:]:
    translated_seeds = übersetzen(translated_seeds, maps[map_name])

fiji1 = min(translated_seeds)
fiji2 = """Haven't solved task 5.2:
I got the star with a code from the Internet, because I was trying to reverse engineer the code with my result, but I wasn't able to solve the task by myself (yet). 
In the time stress of the pre-Christmas period, I have to admit defeat for the time being :("""

print("Lösung Aufgabe 5.1: ", str(fiji1))
print("Lösung Aufgabe 5.2: ", str(fiji2))
print("Grüße von Fiji :^)")