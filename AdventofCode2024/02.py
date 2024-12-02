def check_array_validity(subarray):
    is_increasing = all(subarray[i] < subarray[i + 1] for i in range(len(subarray) - 1))
    is_decreasing = all(subarray[i] > subarray[i + 1] for i in range(len(subarray) - 1))
    is_difference_valid = all(abs(subarray[i] - subarray[i + 1]) < 4 for i in range(len(subarray) - 1))

    return (is_increasing or is_decreasing) and is_difference_valid

array = []

with open("AdventofCode2024/input/02.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    array.append([int(value) for value in line.split()])
    
counter_1 = 0
counter_2 = 0

for subarray in array:
    safe = check_array_validity(subarray)
    
    if safe:
        counter_1 += 1
        counter_2 += 1
    else:        
        if any(check_array_validity(subarray[:i] + subarray[i+1:]) for i in range(len(subarray))):
            counter_2 += 1
        
print("Aufgabe 1: " + str(counter_1))
print("Aufgabe 2: " + str(counter_2))