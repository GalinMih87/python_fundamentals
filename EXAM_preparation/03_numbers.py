def sorted_func(greater_numbers):
    top_five_numbers = []
    for num in sorted(greater_numbers, reverse=True):
        if len(top_five_numbers) < 5:
            top_five_numbers.append(num)
        else:
            break
    return " ".join([str(num) for num in top_five_numbers])


def numbers_func(numbers):
    average_sum = sum(numbers) / len(numbers)
    greater_numbers = [num for num in numbers if num > average_sum]

    if greater_numbers:
        print(sorted_func(greater_numbers))
    else:
        print("No")


nums = list(map(int, input().split(" ")))
numbers_func(nums)
