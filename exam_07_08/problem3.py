animals = {}

while True:
    command = input()

    if command == "EndDay":
        break

    command = command.split(": ")
    act = command[0]

    if act == "Add":
        name_food_area = command[1].split("-")
        name = name_food_area[0]
        food = int(name_food_area[1])
        area = name_food_area[2]
        if area in animals:
            animals[area] = [name, animals[area][1] + food]
        else:
            animals[area] = [name, food]

    elif act == "Feed":
        name_food_area = command[1].split("-")
        name = name_food_area[0]
        food = int(name_food_area[1])

print(animals)