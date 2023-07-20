n = int(input())
sum_of_chars = 0
for i in range(1, n + 1):
    symbol = input()
    sum_of_chars += ord(symbol)
print(f"The sum equals: {sum_of_chars}")