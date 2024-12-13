def parse_claw_machines(lines):
    claw_machines = []
    current_claw_machine = {}

    for line in lines:
        line = line.strip()
        if not line:
            if current_claw_machine:
                claw_machines.append(current_claw_machine)
                current_claw_machine = {}
            continue

        # Parse die Zeile
        if line.startswith("Button A:"):
            x_a, y_a = map(int, [s.split("+")[1] for s in line.split(", ")])
            current_claw_machine["Button A"] = {"X": x_a, "Y": y_a}
        elif line.startswith("Button B:"):
            x_b, y_b = map(int, [s.split("+")[1] for s in line.split(", ")])
            current_claw_machine["Button B"] = {"X": x_b, "Y": y_b}
        elif line.startswith("Prize:"):
            x_prize, y_prize = map(int, [s.split("=")[1] for s in line.split(", ")])
            current_claw_machine["Prize"] = {"X": x_prize, "Y": y_prize}

    if current_claw_machine:
        claw_machines.append(current_claw_machine)

    return claw_machines


def find_cheapest_path(claw_machine):
    from math import inf

    # Extrahiere die notwendigen Daten
    button_a = claw_machine["Button A"]
    button_b = claw_machine["Button B"]
    prize = claw_machine["Prize"]

    target_x, target_y = prize["X"], prize["Y"]
    cost_a, cost_b = 3, 1

    min_cost = inf
    best_path = {"A": 0, "B": 0}

    max_steps = 100
    for a_steps in range(max_steps):
        for b_steps in range(max_steps):
            x = a_steps * button_a["X"] + b_steps * button_b["X"]
            y = a_steps * button_a["Y"] + b_steps * button_b["Y"]

            if x == target_x and y == target_y:
                cost = a_steps * cost_a + b_steps * cost_b
                if cost < min_cost:
                    min_cost = cost
                    best_path = {"A": a_steps, "B": b_steps}

    return {"Steps": best_path, "Cost": min_cost}


with open("AdventofCode2024/input/13.txt", "r") as file:
    lines = file.readlines()

claw_machines = parse_claw_machines(lines)

counter1 = 0
for i, claw_machine in enumerate(claw_machines):
    result = find_cheapest_path(claw_machine)
    print(i+1,"/",len(claw_machines))
    if result["Cost"] != float('inf'):
        counter1 += result["Cost"]
print("Aufgabe 1:", counter1)