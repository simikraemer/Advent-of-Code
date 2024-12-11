from collections import defaultdict

def blinzeln(steine, iterationen):
    steine_dict = defaultdict(int)
    for stein in steine:
        steine_dict[stein] += 1

    for i in range(iterationen):
        neue_steine_dict = defaultdict(int)

        for stein, anzahl in steine_dict.items():
            if stein == 0:
                neue_steine = [1]
            elif len(str(stein)) % 2 == 0:
                mitte = len(str(stein)) // 2
                linke_hälfte = int(str(stein)[:mitte])
                rechte_hälfte = int(str(stein)[mitte:])
                neue_steine = [linke_hälfte, rechte_hälfte]
            else:
                neue_steine = [stein * 2024]

            for neuer_stein in neue_steine:
                neue_steine_dict[neuer_stein] += anzahl

        steine_dict = neue_steine_dict

    return steine_dict

with open("AdventofCode2024/input/11.txt", "r") as file:
    line = file.readline().strip()

# Aufgabe 1
steine = map(int, line.split())
steine_aufgabe_1 = blinzeln(steine, 25)
print("Aufgabe 1:", sum(steine_aufgabe_1.values()))

# Aufgabe 2
steine = map(int, line.split())
steine_aufgabe_2 = blinzeln(steine, 75)
print("Aufgabe 2:", sum(steine_aufgabe_2.values()))
