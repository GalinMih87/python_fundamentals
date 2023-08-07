numbers_as_string = input().split(", ")


def positive_number(num):
    return [number for number in numbers_as_string if int(number) >= 0]


def negative_number(num):
    return [number for number in numbers_as_string if int(number) < 0]


def even_number(num):
    return [number for number in numbers_as_string if int(number) % 2 == 0]


def odd_number(num):
    return [number for number in numbers_as_string if int(number) % 2 != 0]


print(f"Positive: {', '.join(positive_number(numbers_as_string))}")
print(f"Negative: {', '.join(negative_number(numbers_as_string))}")
print(f"Even: {', '.join(even_number(numbers_as_string))}")
print(f"Odd: {', '.join(odd_number(numbers_as_string))}")
