number_of_lines = int(input())
capacity = 255
total = 0

for i in range(number_of_lines):
    liters = int(input())
    capacity -= liters

    if capacity < 0:
        capacity += liters
        print("Insufficient capacity!")
        continue

    total += liters
print(total)
