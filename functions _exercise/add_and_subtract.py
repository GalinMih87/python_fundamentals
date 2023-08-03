firs_number = int(input())
second_number = int(input())
three_number = int(input())


def sum_numbers(f, s):
    result = firs_number + second_number
    return result


def subtract(f, s, t):
    result = sum_numbers(f, s) - three_number
    return result


def add_and_subtract(f, s, t):
    sum_numbers(f, s)
    subtract(f, s)


print(subtract(firs_number, second_number, three_number))

