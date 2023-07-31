password = input()
new_password = ""
while True:
    command = input()

    if command == "Done":
        break

    command = command.split()

    action = command[0]

    if action == "TakeOdd":
        for i in range(len(password)):
            if i % 2 != 0:
                new_password += password[i]
        password = new_password
        print(password)
    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        password = password[:index] + password[index + length:]
        print(password)
    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")