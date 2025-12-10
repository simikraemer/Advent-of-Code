lights = []
buttons = []
from pathlib import Path
with open(Path(__file__).resolve().parent / "input" / "10.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        lights.append(list(line[line.index("[")+1:line.index("]")]))
        
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
        
    #for j, button in enumerate(buttons[m]):
    #    
    #    light = push_the_button(button,light)
    #    print(button)
    #    print(light)
        
    #print()


aufgabe2 = 0

print(f"Aufgabe 1: {aufgabe1}")
print(f"Aufgabe 2: {aufgabe2}")