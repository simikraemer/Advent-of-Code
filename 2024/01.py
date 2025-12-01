array1 = []
array2 = []

with open("2024/input/01.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    parts = line.strip().split("   ")
    
    array1.append(int(parts[0]))
    array2.append(int(parts[1]))

array1 = sorted(array1)
array2 = sorted(array2)

total_difference = 0
for i in range(min(len(array1), len(array2))):
    total_difference += abs(array1[i] - array2[i])
    
similarity_score = 0
for value in array1:
    count = array2.count(value)
    similarity_score += count * value
    
print(f"Aufgabe 1: {total_difference}")
print(f"Aufgabe 2: {similarity_score}")

