with open('2023/input/1.txt', 'r') as datei:
    source_liste = datei.readlines()
    
gefilterte_liste = []
akzeptierte_strings = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

for eintrag in source_liste:
    fijiZiffer1 = ''
    
    for zeichen in eintrag:
        if zeichen.isdigit():
            if not fijiZiffer1:
                fijiZiffer1 = zeichen
            fijiZiffer2 = zeichen
    gefilterte_liste.append(fijiZiffer1 + fijiZiffer2)

fiji1 = sum(map(int, gefilterte_liste))


with open('2023/input/1.txt', 'r') as datei:
    source_liste = datei.readlines()
    
gefilterte_liste = []

for eintrag in source_liste:
    fijiZiffer1 = ""
    ziffern_array = []
    index = 0

    for zeichen in eintrag:
        if zeichen.isdigit():
            ziffern_array.append([zeichen, index])
        index += 1

    for zahlenstring in akzeptierte_strings:
        position_im_string = 0
        while True:
            index = eintrag.find(zahlenstring, position_im_string)
            if index == -1: # Wenn zahlenstring nicht (mehr) in eintrag gefunden werden kann
                break
            ziffern_array.append([akzeptierte_strings[zahlenstring], index])
            position_im_string = index + 1 # An der Stelle nach dem ersten Buchstaben des gefundenen Strings weitersuchen
    
    ziffern_array.sort(key=lambda x: x[1]) # Sortieren nach Position
    fijiZiffer1 = ziffern_array[0][0]
    fijiZiffer2 = ziffern_array[-1][0]
    
    gefilterte_liste.append(fijiZiffer1 + fijiZiffer2)

fiji2 = sum(map(int, gefilterte_liste))

print("Lösung Aufgabe 1.1: ", str(fiji1))
print("Lösung Aufgabe 1.2: ", str(fiji2))
print("Grüße von Fiji :^)")