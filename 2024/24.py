def parse_input(lines):
    initial_values = {}
    gates = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if ":" in line:
            wire, value = line.split(":")
            initial_values[wire.strip()] = int(value.strip())
        elif "->" in line: 
            gates.append(line)
    
    return {"initial_values": initial_values, "gates": gates}

def aufgabe1(input_data):
    initial_values = input_data["initial_values"]
    gates = input_data["gates"]
    wire_values = initial_values.copy()
    
    def process_gate(gate):
        parts = gate.split(" ")
        if "AND" in gate:
            input1, input2, output = parts[0], parts[2], parts[4]
            wire_values[output] = wire_values[input1] & wire_values[input2]
        elif "XOR" in gate:
            input1, input2, output = parts[0], parts[2], parts[4]
            wire_values[output] = wire_values[input1] ^ wire_values[input2]
        elif "OR" in gate:
            input1, input2, output = parts[0], parts[2], parts[4]
            wire_values[output] = wire_values[input1] | wire_values[input2]
    
    remaining_gates = gates.copy()
    while remaining_gates:
        processed_gates = []
        
        for gate in remaining_gates:
            parts = gate.split(" ")
            input1, input2 = parts[0], parts[2]
            
            if input1 in wire_values and input2 in wire_values:
                process_gate(gate)
                processed_gates.append(gate)
        
        remaining_gates = [gate for gate in remaining_gates if gate not in processed_gates]
    
    output_value = 0
    z_wires = sorted([wire for wire in wire_values if wire.startswith("z")])
    for i, wire in enumerate(z_wires):
        output_value += wire_values[wire] * (2 ** i)
    return output_value


with open("2024/input/24.txt", "r") as file:
    lines = file.readlines()

input = parse_input(lines)

print("Aufgabe 1:", aufgabe1(input))