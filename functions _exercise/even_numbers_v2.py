numbers_as_digits = [int(s) for s in input().split()]
even_numbers = lambda x: x % 2 == 0
result = list(filter(even_numbers, numbers_as_digits))
print(result)
