number_of_snowball = int(input())
max_snowball_weight = 0
max_snowball_time = 0
max_snowball_value = 0
max_snowball_quality = 0

for snowball in range(number_of_snowball):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if value > max_snowball_value:
        max_snowball_weight = weight
        max_snowball_time = time
        max_snowball_value = value
        max_snowball_quality = quality
print(f"{max_snowball_weight} : {max_snowball_time} = {int(max_snowball_value)} ({max_snowball_quality})")