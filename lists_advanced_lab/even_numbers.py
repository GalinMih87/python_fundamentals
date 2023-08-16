number = list(map(int, input().split(",")))
index = [i for i in range(len(number)) if number[i] % 2 == 0]
print(index)