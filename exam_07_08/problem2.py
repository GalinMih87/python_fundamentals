import re

regex = r"(\!)([A-Z][a-z]{2,})(\!):(\[)([A-Za-z]{8,})(\])"
new_list = ""
count_of_inputs = int(input())

for c in range(count_of_inputs):
    text = input()

    result1 = re.match(regex, text)
    result2 = re.finditer(regex, text)

    if not re.match(regex, text):
        print("The message is invalid")
    for i in result2:
        new_list += (i[5])
        result = [(str(ord(i))) for i in new_list]
        print(f"{i[2]}: {' '.join(result)}")
