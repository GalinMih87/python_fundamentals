number = input().split(" ")
new_nember = list(map(int, number))


def even(a):
    new_list = []
    for i in new_nember:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


print(even(new_nember))