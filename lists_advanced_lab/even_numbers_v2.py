list_number = list(map(int, input().split(", ")))
new_list = []

for index, element in enumerate(list_number):
    if element % 2 == 0:
        new_list.append(index)

print(new_list)