routing = {}
routing_int = {}
name_to_idx = {}
from pathlib import Path
with open(Path(__file__).resolve().parent / "input" / "11.txt", "r") as file:
    lines = file.readlines()
    for i,line in enumerate(lines):
        line = line.strip()
        von = line[0:3]
        if von == "you":
            startidx = i
        elif von == "svr":
            serveridx = i
        elif von == "fft":
            fftidx = i
        elif von == "dac":
            dacidx = i
        nach = line[5:].split(" ")
        routing[i] = (von, nach)

aufgabe1 = 0

def rockyroadtodublin(von):
    global aufgabe1

    if von == "out":
        aufgabe1 += 1
        return

    #print("Von",von)
    idx = next(k for k, (name, _) in routing.items() if name == von)

    nach = routing[idx][1]
    for n in nach:
        #print("Nach",n)
        rockyroadtodublin(n)
    
try:
    startidx
except NameError:
    print("Aufgabe 2 Testinput:")
else:
    for nach in routing[startidx][1]:
        rockyroadtodublin(nach)
    print(f"Aufgabe 1: {aufgabe1}")


aufgabe2 = 0

name_to_idx = {}
idx_to_name = {}

max_i = max(routing.keys())
for i, (name, targets) in routing.items():
    name_to_idx[name] = i
    idx_to_name[i] = name
#print(name_to_idx, idx_to_name)

next_idx = max_i + 1
for _, (_, targets) in routing.items():
    for t in targets:
        if t not in name_to_idx:
            name_to_idx[t] = next_idx
            idx_to_name[next_idx] = t
            next_idx += 1

routing_int = {i: [] for i in range(next_idx)}
for i, (name, targets) in routing.items():
    for t in targets:
        routing_int[i].append(name_to_idx[t])

#print(routing_int)
#print(serveridx, fftidx, dacidx)

cache = {}

def count_paths(idx, fft, dac):
    #print(idx_to_name[idx])
    if idx == dacidx:
        fft = True
    if idx == fftidx:
        dac = True

    key = (idx, fft, dac)
    if key in cache:
        #print("--KNOWN--")
        #print(key,cache[key])
        #print()
        return cache[key]

    if not routing_int[idx]:
        result = 1 if (fft and dac) else 0
        #print("--SAVED--")
        #print(key,result)
        #print()
        cache[key] = result
        return result

    total = 0
    for nxt in routing_int[idx]:
        total += count_paths(nxt, fft, dac)

    cache[key] = total
    return total

aufgabe2 = count_paths(serveridx, False, False)

print(f"Aufgabe 2: {aufgabe2}")