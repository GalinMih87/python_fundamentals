import re

regex = r"(U\$)([A-Z]{1}[a-z]{2,})(U\$)(P\@\$)([A-Za-z]{5,}[0-9]{1,})(P\@\$)"
username = ""
password = ""
count = 0
count_of_inputs = int(input())

for c in range(count_of_inputs):
    text = input()

    result1 = re.match(regex, text)
    result2 = re.findall(regex, text)

    if not re.match(regex, text):
        print("Invalid username or password")
    for i in result2:
        username += (i[1])
        password += (i[4])
        count += 1
        print("Registration was successful")
        print(f"Username: {username}, Password: {password}")

print(f"Successful registrations: {count}")