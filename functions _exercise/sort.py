number = input().split(" ")
new_nember = list(map(int, number))


def even(a):
    new_list = []
    for i in new_nember:
        new_list.append(i)
        sorted_list = sorted(new_nember)

    return sorted_list


print(even(new_nember))

