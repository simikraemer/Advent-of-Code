with open("input/10.txt", 'r') as file:
    einträge = file.read().strip().split()
besucht = set()
aktuelle_position = {(lambda einträge: next(((x, y) for y, row in enumerate(einträge) for x, char in enumerate(row) if char == 'S'), None))(einträge)}
fiji1 = 0
fiji2 = 0

# Nur wenn aktuelles und nächstes Position ein sinnvolles Zeichen haben, wird die neue Position angenommen -> Verhindert Sackgassen
# Durch "besucht" wird verhindert, dass man einen Schritt zurückgeht und while stoppt, sobald der Loop sich "trifft", da keine nächste Position möglich
while aktuelle_position:
    richtungen = [(1, 0, "SLF-", "J7-"), (-1, 0, "SJ7-", "LF-"), (0, 1, "SF7|", "LJ|"), (0, -1, "SLJ|", "F7|")]
    nächste_position = set()
    for x, y in aktuelle_position:
        for dx, dy, valides_aktuelles_zeichen, valides_nächstes_zeichen in richtungen:
            neues_x, neues_y = x + dx, y + dy
            if 0 <= neues_x < len(einträge[0]) and 0 <= neues_y < len(einträge) and einträge[y][x] in valides_aktuelles_zeichen and einträge[neues_y][neues_x] in valides_nächstes_zeichen and (neues_x, neues_y) not in besucht:
                nächste_position.add((neues_x, neues_y))
    besucht |= aktuelle_position
    aktuelle_position = nächste_position
    fiji1 += 1 if nächste_position else 0

# Alle Punkte, die nicht besucht wurden, werden in Punkte verwandelt
for y, zeile in enumerate(einträge):
    for x, zeichen in enumerate(zeile):
        if (x, y) not in besucht:
            einträge[y] = einträge[y][:x] + "." + einträge[y][x + 1:]

# Wenn sich die Einträge links von jedem beliebigen Punkt außerhalb der besuchten Punkte auf eine ungerade Anzahl von |, L oder J summieren, dann wird der Punkt vom Loop eingekreist.
# Den Tipp hab ich aus dem Internet :^)
for y, zeile in enumerate(einträge):
    for x, zeichen in enumerate(zeile):
        if (x, y) not in besucht:
            summezeichenlinks = sum(1 for zeichen in zeile[:x] if zeichen in "|LJ")
            if summezeichenlinks % 2 != 0:
                fiji2 += 1
        besucht.add((x, y))

print("Lösung Aufgabe 10.1: " + str(fiji1))
print("Lösung Aufgabe 10.2: " + str(fiji2))
print("Grüße von Fiji :^)")
