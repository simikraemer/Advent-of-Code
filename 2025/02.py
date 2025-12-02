invalide_ids_1 = []
invalide_ids_2 = []

with open("2025/input/02.txt", "r") as file:
    line = file.read()
    bereiche = line.split(",")

    for bereich in bereiche:
        start_str, end_str = bereich.split("-")
        start = int(start_str)
        end = int(end_str)
        wert = start

        while wert <= end:
            wertstring = str(wert)
            länge = len(str(wert))

            # Aufgabe 1
            if länge % 2 == 0:
                haelfte = len(wertstring) // 2
                teil1, teil2 = wertstring[:haelfte], wertstring[haelfte:]
                if teil1 == teil2:
                    invalide_ids_1.append(wert)


            # Aufgabe 2
            for k in range(1, länge // 2 + 1):
                if länge % k != 0:
                    continue

                teile = []
                ziffern = 0
                while ziffern < länge:
                    teile.append(wertstring[ziffern:ziffern + k])
                    ziffern += k
                    
                alle_gleich = True
                erstes = teile[0]
                for teil in teile:
                    if teil != erstes:
                        alle_gleich = False
                        break
                    
                if alle_gleich:
                    invalide_ids_2.append(wert)
                    break

            wert += 1
        
aufgabe1 = sum(invalide_ids_1)
aufgabe2 = sum(invalide_ids_2)

print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")