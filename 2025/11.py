routing = {}
from pathlib import Path
with open(Path(__file__).resolve().parent / "input" / "11.txt", "r") as file:
    lines = file.readlines()
    for i,line in enumerate(lines):
        line = line.strip()
        von = line[0:3]
        if von == "you":
            startidx = i
        nach = line[5:].split(" ")
        routing[i] = (von, nach)

aufgabe1 = 0

def rockyroadtodublin(von):
    global aufgabe1

    if von == "out":
        aufgabe1 += 1
        return

    print("Von",von)
    idx = next(k for k, (name, _) in routing.items() if name == von)

    nach = routing[idx][1]
    for n in nach:
        print("Nach",n)
        rockyroadtodublin(n)
    

print(routing[startidx])
for nach in routing[startidx][1]:
    rockyroadtodublin(nach)

aufgabe2 = 0


print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")