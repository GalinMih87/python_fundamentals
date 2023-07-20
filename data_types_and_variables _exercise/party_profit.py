companion = int(input())
days = int(input())
coins = 0
for day in range(1, days + 1):
    if day % 10 == 0:
        companion -= 2
    if day % 15 == 0:
        companion += 5
    if day % 3 == 0:
        coins -= companion * 3
    if day % 5 == 0:
        coins += companion * 20
        if day % 3 == 0:
            coins -= companion * 2
    coins += 50
    coins -= companion * 2
coins_per_companion = int(coins / companion)
print(f"{companion} companions received {coins_per_companion} coins each.")