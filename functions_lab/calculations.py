random_operator = input()
first_num = int(input())
second_num = int(input())


def choice(operator, f, s):
    result = None
    if operator == "multiply":
        result = f * s
    elif operator == "divide":
        result = int(f / s)
    elif operator == "add":
        result = f + s
    elif operator == "subtract":
        result = f - s
    return result

print(choice(random_operator, first_num, second_num))
