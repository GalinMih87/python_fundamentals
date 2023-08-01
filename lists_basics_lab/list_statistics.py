number = int(input())
positive = []
negativ = []

for _ in range(number):
    curent_number = int(input())

    if curent_number >= 0:
        positive.append(curent_number)
    else:
        negativ.append(curent_number)

print(positive)
print(negativ)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negativ)}")
