number = input().split(" ")
new_nember = list(map(int, number))


def min_num(a):
    minimum = min(new_nember)
    return minimum


def max_num(a):
    maximum = max(new_nember)
    return maximum


def sum_numbs(a):
    sum_of_numbers = sum(new_nember)
    return sum_of_numbers


print(f"The minimum number is {min_num(new_nember)}")
print(f"The maximum number is {max_num(new_nember)}")
print(f"The sum number is: {sum_numbs(new_nember)}")

