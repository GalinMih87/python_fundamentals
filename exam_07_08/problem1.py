text_str = input()
index_all = []

while True:
    command = input()

    if command == "End":
        break

    command = command.split()
    act = command[0]

    if act == "Translate":
        char = command[1]
        replacement = command[2]
        text_str = text_str.replace(char, replacement)
        print(text_str)

    elif act == "Includes":
        substring = command[1]
        if substring in text_str:
            print("True")
        else:
            print("False")

    elif act == "Start":
        substring = command[1]
        if text_str.startswith(substring):
            print("True")
        else:
            print("False")

    elif act == "Lowercase":
        text_str = text_str.lower()
        print(text_str)

    elif act == "FindIndex":
        char = command[1]
        for index, value in enumerate(text_str):
            if value == char:
                index_all.append(index)
        print(index_all[-1])

    elif act == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        text_str = text_str[:start_index] + text_str[start_index + count:]
        print(text_str)