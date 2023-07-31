import re

regex = r"(U\$)([A-Z]{1}[a-z]{2,})(U\$)(P\@\$)([A-Za-z]{5,}[0-9]{1,})(P\@\$)"
count = int(input())
counter = 0

for _ in range(count):
	text = input()
	if re.match(regex, text):
		group = re.findall(regex, text)
		if group:
			for i in group:
				print("Registration was successful")
				print(f"Username: {i[1]}, Password: {i[4]}")
				counter += 1
	else:
		print("Invalid username or password")

print(f"Successful registrations: {counter}")