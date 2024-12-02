with open('input/6.txt', 'r') as datei:
    source_liste = datei.readlines()
    
time_array1 = []
time_array2 = []
distanz_array1 = []   
distanz_array2 = []     
fiji1 = 1
fiji2 = 1

for eintrag in source_liste:
    eintrag_geteilt = eintrag.split(": ")
    category, values = eintrag_geteilt[0], eintrag_geteilt[1].split()
    if category.strip() == 'Time':
        time_array1.extend([int(val) for val in values])
        time_array2.extend([int(''.join(values))])
    elif category.strip() == 'Distance':
        distanz_array1.extend([int(val) for val in values])
        distanz_array2.extend([int(''.join(values))])
    
for index, zeit in enumerate(time_array1):
    max_zeit = zeit
    erfolg_counter = 0
    for i in range(0, max_zeit):
        haltezeit = i
        distanz = i * (max_zeit - i)
        if distanz > distanz_array1[index]:
            erfolg_counter += 1
    fiji1 *= erfolg_counter
    
for index, zeit in enumerate(time_array2):
    max_zeit = zeit
    erfolg_counter = 0
    for i in range(0, max_zeit):
        haltezeit = i
        distanz = i * (max_zeit - i)
        if distanz > distanz_array2[index]:
            erfolg_counter += 1
    fiji2 *= erfolg_counter

print("Lösung Aufgabe 6.1: ", str(fiji1))
print("Lösung Aufgabe 6.2: ", str(fiji2))
print("Grüße von Fiji :^)")