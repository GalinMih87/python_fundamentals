journey = float(input())
months = int(input())
spend = 0

for month in range(1, months + 1):
    if month % 2 != 0:
        spend -= spend * 0.16

    if month % 4 == 0:
        spend += spend * 0.25

    spend += journey * 0.25

    if month == 1:
        continue

diff = abs(spend - journey)
if spend >= journey:
    print(f"Bravo! You can go to Disneyland and you will have {diff:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {diff:.2f}lv. more.")