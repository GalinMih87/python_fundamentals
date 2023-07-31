energy = int(input())
win_games = 0

while True:
    command = input()

    if command == "End of battle":
        print(f"Won battles: {win_games}. Energy left {energy}")
        break

    distance = int(command)

    if energy >= distance:
        energy -= distance
        win_games += 1

        if win_games % 3 == 0:
            energy += win_games

    else:
        print(f"Not enough energy! Game ends with {win_games} won battles and {energy} energy")
        break
