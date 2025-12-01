from collections import deque
from tqdm import tqdm

with open("2024/input/09.txt", "r") as file:
    line = file.readline().strip()

array = []
for i, zeichen in enumerate(line):
    array.append({
        "value": int(zeichen),
        "id": i // 2 if i % 2 == 0 else "."
    })

dot_positions = deque()
digit_positions = deque()

position = 0
for entry in array:
    if entry["id"] == ".":
        dot_positions.append({"start": position, "value": entry["value"], "id": entry["id"]})
    else:
        digit_positions.append({"start": position, "value": entry["value"], "id": entry["id"]})
    position += entry["value"]

# Aufgabe 1
digit_positions_task1 = deque()
for digit_block in digit_positions:
    for i in range(digit_block["value"]):
        digit_positions_task1.append((digit_block["start"] + i, digit_block["id"]))

dot_indices_task1 = [dot["start"] + i for dot in dot_positions for i in range(dot["value"])]

for dot_index in dot_indices_task1:
    if not digit_positions_task1:
        break
    last_digit_index, last_digit_value = digit_positions_task1.pop()
    if dot_index < last_digit_index:
        digit_positions_task1.appendleft((dot_index, last_digit_value))
    else:
        digit_positions_task1.append((last_digit_index, last_digit_value))

counter1 = sum(pos * int(val) for pos, val in digit_positions_task1)
print("Aufgabe 1:", counter1)

# Aufgabe 2
progress_bar = tqdm(total=len(digit_positions), desc="Aufgabe 2", unit=" Operationen")

for digit_block in reversed(digit_positions):
    value_to_move = digit_block["value"]
    for dot_block in dot_positions:
        if value_to_move == 0:
            break
        if dot_block["value"] >= value_to_move and digit_block["start"] > dot_block["start"]:
            new_start = dot_block["start"]
            dot_block["start"] += value_to_move
            dot_block["value"] -= value_to_move
            digit_block["start"] = new_start
            value_to_move = 0
            break
    progress_bar.update(1)

progress_bar.close()

counter2 = sum(
    (block["start"] + i) * block["id"]
    for block in digit_positions
    for i in range(block["value"])
)

print("Aufgabe 2:", counter2)