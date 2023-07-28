text = ''
all_index = []

while True:
    command = input()

    if command == "End":
        break

    command = command.split()
    action = command[0]

    if action == "Add":
        substring = command[1]
        text = text + substring

    elif action == "Upgrade":
        char = command[1]
        for ch in text:
            if ch == char:
                next_ch = chr(ord(ch) + 1)
                text = text.replace(ch, next_ch)

    elif action == "Print":
        print(text)

    elif action == "Index":
        char = command[1]
        if char in text:
            for index, value in enumerate(text):
                if value == char:
                    all_index.append(index)
            print(*all_index)
        else:
            print("None")

    elif action == "Remove":
        substring = command[1]
        if substring in text:
            text = text.replace(substring, "")