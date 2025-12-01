def check_array_validity(subarray):
    is_increasing = all(subarray[i] < subarray[i + 1] for i in range(len(subarray) - 1))
    is_decreasing = all(subarray[i] > subarray[i + 1] for i in range(len(subarray) - 1))
    is_difference_valid = all(abs(subarray[i] - subarray[i + 1]) < 4 for i in range(len(subarray) - 1))

    return (is_increasing or is_decreasing) and is_difference_valid

array = []

with open("2024/input/02.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    array.append([int(value) for value in line.split()])
    
counter1 = 0
counter2 = 0

for subarray in array:
    safe = check_array_validity(subarray)
    
    if safe:
        counter1 += 1
        counter2 += 1
    else:        
        if any(check_array_validity(subarray[:i] + subarray[i+1:]) for i in range(len(subarray))):
            counter2 += 1
        
print("Aufgabe 1: " + str(counter1))
print("Aufgabe 2: " + str(counter2))