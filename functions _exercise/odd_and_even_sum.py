number = input()
new_nember = list(map(int, number))


def symbol(n):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for i in new_nember:
        if i % 2 == 0:
            sum_of_even_digits += i
        if i % 2 != 0:
            sum_of_odd_digits += i

    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


print(symbol(number))