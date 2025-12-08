boxes = []
from pathlib import Path
with open(Path(__file__).resolve().parent / "input" / "08.txt", "r") as file:
    lines = file.readlines()
    länge = len(lines)
    for line in lines:
        line = line.strip()
        x, y, z = line.split(",")
        boxes.append((int(x),int(y),int(z)))

distanzmatrix = {}
import math
for i,von in enumerate(boxes):
    for j,bis in enumerate(boxes):
        if i > j or i == j:
            continue
        distanz = math.sqrt( (bis[0] - von[0])**2 + (bis[1] - von[1])**2 + (bis[2] - von[2])**2 )
        distanzmatrix[(i, j)] = distanz

circuits = []
for box in boxes:
    circuits.append([box])
    
def find_circuit_index(circuits, box):
    for idx, circuit in enumerate(circuits):
        if box in circuit:
            return idx
    return None

distanzmatrix = sorted(distanzmatrix.items(), key=lambda x: x[1])
counter = 0
anzahl = 1000
for (von, bis), distanz in distanzmatrix:
    box_von = boxes[von]
    box_bis = boxes[bis]

    idx_von = find_circuit_index(circuits, box_von)
    idx_bis = find_circuit_index(circuits, box_bis)
    if idx_von is not None and idx_bis is not None and idx_von != idx_bis:
        circuits[idx_von].extend(circuits[idx_bis])
        del circuits[idx_bis]

    counter += 1
    if counter == anzahl:
        break
    
sizes = sorted((len(c) for c in circuits), reverse=True)[:3]
aufgabe1 = sizes[0] * sizes[1] * sizes[2]

# Euklidische Distanz = sqrt( (x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2 )

aufgabe2 = 0

circuits = []
for box in boxes:
    circuits.append([box])

for (von, bis), distanz in distanzmatrix:
    box_von = boxes[von]
    box_bis = boxes[bis]

    idx_von = find_circuit_index(circuits, box_von)
    idx_bis = find_circuit_index(circuits, box_bis)
    if idx_von is not None and idx_bis is not None and idx_von != idx_bis:
        circuits[idx_von].extend(circuits[idx_bis])
        del circuits[idx_bis]

    if len(circuits) == 1:
        aufgabe2 = boxes[von][0] * boxes[bis][0]
        break
    
        
print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")