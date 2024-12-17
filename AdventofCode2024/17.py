def parse_input(lines):
    registers = {}
    program = []
    
    for line in lines:
        if line.startswith("Register"):
            parts = line.split(":")
            register_name = parts[0].split()[1]
            register_value = int(parts[1].strip())
            registers[register_name] = register_value
        
        elif line.startswith("Program"):
            program_line = line.split(":")[1].strip()
            program = list(map(int, program_line.split(",")))

    A = registers.get('A', 0)
    B = registers.get('B', 0)
    C = registers.get('C', 0)

    return A, B, C, program

def berechne_den_quatsch(a, b, c, program):
    def combo(operand):
        if operand <= 3:
            return operand
        if operand == 4:
            return a
        if operand == 5:
            return b
        if operand == 6:
            return c
        return 7

    i = 0
    output = []
    while i < len(program):
        op = program[i]
        operand = program[i + 1]

        if op == 0:  # adv
            a //= 2 ** combo(operand)
        elif op == 1:  # bxl
            b ^= operand
        elif op == 2:  # bst
            b = combo(operand) % 8
        elif op == 3:  # jnz
            if a != 0:
                i = operand
                continue
        elif op == 4:  # bxc
            b ^= c
        elif op == 5:  # out
            output.append(combo(operand) % 8)
        elif op == 6:  # bdv
            b = a // 2 ** combo(operand)
        elif op == 7:  # cdv
            c = a // 2 ** combo(operand)

        i += 2
    return output

def find_minimal_A(a, n, program):
    if n > len(program):
        return a

    for i in range(8):  # 3 Bits durchlaufen (0 bis 7)
        new_a = (a << 3) | i  # Nächste 3 Bits an A hängen
        output = berechne_den_quatsch(new_a, 0, 0, program)

        # Prüfen, ob der Output mit dem Ende des Programms übereinstimmt
        if output == program[-n:]:
            result = find_minimal_A(new_a, n + 1, program)
            if result is not False:
                return result
    return False

with open("AdventofCode2024/input/17.txt", "r") as file:
    lines = file.readlines()

A, B, C, program = parse_input(lines)

print("Aufgabe 1:", ','.join(map(str, berechne_den_quatsch(A, B, C, program))))
print("Aufgabe 2:", find_minimal_A(0, 1, program))