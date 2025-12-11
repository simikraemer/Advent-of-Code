lights = []
buttons = []
joltages = []
from pathlib import Path
with open(Path(__file__).resolve().parent / "input" / "10.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        lights.append(list(line[line.index("[")+1:line.index("]")]))
        joltages.append(list(map(int, line[line.index("{")+1:line.index("}")].split(","))))
        
        line_buttons = []
        pos = 0
        while pos < line.index("{")-1:
            try:
                start = line.index("(", pos)
                end   = line.index(")", start)
            except ValueError:
                break
            button_str = line[start + 1 : end]
            line_buttons.append(button_str.split(","))
            pos = end + 1
        buttons.append(line_buttons)
        
#for light in lights:
#    print(light)
#for button in buttons:
#    print(button)

def push_the_button(button, light):
    for i in button:
        if light[int(i)] == "#":
            light[int(i)] = "."
        else:
            light[int(i)] = "#"
    return light

def resetlight(length):
    light = []
    for _ in range(length):
        light.append(".")
    return light

aufgabe1 = 0
from itertools import combinations
for m, maschine in enumerate(buttons):
        
    anzahl_buttons = len(buttons[m])

    button_optionen = []
    for r in range(1, anzahl_buttons + 1):
        for combo in combinations(range(anzahl_buttons), r):
            button_optionen.append(list(combo))
    #print(button_optionen)
    
    #light_dict = {lights[m], 0}
    
    for option in button_optionen:
        light = resetlight(len(lights[m]))
        for o in option:
            light = push_the_button(buttons[m][o],light)
        #print("--")
        if light == lights[m]:
            #print(light)
            #print(lights[m])
            aufgabe1 += len(option)
            #print(len(option), option)
            found = True
            break

# Aufgabe 2 mit KI, die michauf den ILP-Solver verwiesen hat, alle meine Ansätze wären BruteForce gewesen

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

aufgabe2 = 0

def berechne_minbuttonpresses(buttons_m, joltages_m):
    anzahl_counters = len(joltages_m)
    anzahl_buttons = len(buttons_m)
    A_eq = np.zeros((anzahl_counters, anzahl_buttons), dtype=float) # Solver nutzt floats...

    for j, button in enumerate(buttons_m):
        for idx_str in button:
            if idx_str.strip() == "":
                continue
            idx = int(idx_str)
            if 0 <= idx < anzahl_counters:
                A_eq[idx][j] = 1.0

    b_eq = np.array(joltages_m, dtype=float)
    c = np.ones(anzahl_buttons, dtype=float)
    integrality = np.ones(anzahl_buttons, dtype=int)
    bounds = Bounds(0, np.inf)
    constraint_eq = LinearConstraint(A_eq, b_eq, b_eq)
    constraints = (constraint_eq,)
    res = milp(
        c=c,
        integrality=integrality,
        bounds=bounds,
        constraints=constraints,
    )
    x = res.x

    minbuttonpresses = 0
    for value in x:
        minbuttonpresses += int(round(value))

    return minbuttonpresses

for m, maschine in enumerate(buttons):
    minbuttonpresses = berechne_minbuttonpresses(buttons[m], joltages[m])
    aufgabe2 += minbuttonpresses


print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")