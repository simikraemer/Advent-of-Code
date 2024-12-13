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
    from sympy import Matrix, solve_linear_system, symbols

    button_a = claw_machine["Button A"]
    button_b = claw_machine["Button B"]
    prize = claw_machine["Prize"]

    target_x, target_y = prize["X"], prize["Y"]
    cost_a, cost_b = 3, 1

    A, B = symbols('A B')

    matrix = Matrix([
        [button_a["X"], button_b["X"], target_x],
        [button_a["Y"], button_b["Y"], target_y]
    ])

    solution = solve_linear_system(matrix, A, B)

    if solution is not None:
        A = solution[A]
        B = solution[B]

        if A.is_integer and B.is_integer and A >= 0 and B >= 0:
            A, B = int(A), int(B)
            cost = A * cost_a + B * cost_b
            return {"Steps": {"A": A, "B": B}, "Cost": cost}
    else:
        return None


from tqdm import tqdm

with open("AdventofCode2024/input/13.txt", "r") as file:
    lines = file.readlines()

claw_machines = parse_claw_machines(lines)

# Aufgabe 1
counter1 = 0
for i, claw_machine in enumerate(tqdm(claw_machines, desc="Aufgabe 1")):
    result = find_cheapest_path(claw_machine)
    if result is not None and result["Cost"] != float('inf'):
        counter1 += result["Cost"]
print("Aufgabe 1:", counter1)

# Aufgabe 2
offset = 10000000000000
counter2 = 0
for i, claw_machine in enumerate(tqdm(claw_machines, desc="Aufgabe 2")):
    claw_machine["Prize"]["X"] += offset
    claw_machine["Prize"]["Y"] += offset
    result = find_cheapest_path(claw_machine)
    if result is not None and result["Cost"] != float('inf'):
        counter2 += result["Cost"]
print("Aufgabe 2:", counter2)