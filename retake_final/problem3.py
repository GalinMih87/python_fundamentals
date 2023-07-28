heroes = {}

while True:
    command = input()

    if command == "Results":
        break

    command = command.split(":")
    action = command[0]

    if action == "Add":
        person_name = command[1]
        health = int(command[2])
        energy = int(command[3])
        if person_name not in heroes:
            heroes[person_name] = {"health": health, "energy": energy}
        else:
            heroes[person_name]["health"] += health

    elif action == "Attack":
        attacker_name = command[1]
        defender_name = command[2]
        damage = int(command[3])
        if attacker_name in heroes and defender_name in heroes:
            heroes[defender_name]["health"] -= damage
            heroes[attacker_name]["energy"] -= 1
            if heroes[defender_name]["health"] <= 0:
                print(f"{defender_name} was disqualified!")
                del heroes[defender_name]
            if heroes[attacker_name]["energy"] <= 0:
                print(f"{attacker_name} was disqualified!")
                del heroes[attacker_name]
    elif action == "Delete":
        username = command[1]
        if username == "All":
            heroes = {}
        elif username in heroes:
            del heroes[username]

count = len(heroes)
print(f"People count: {count}")
for key, value in heroes.items():
    person = key
    health = heroes[key]["health"]
    energy = heroes[key]["energy"]
    print(f"{person} - {health} - {energy}")