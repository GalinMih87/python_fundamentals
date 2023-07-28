white_gold = list(map(int, input().split()))
yellow_gold = list(map(int, input().split()))
pairs = 0
left = 0

result = [x + y for x, y in zip(white_gold, yellow_gold)]

for i in result:
    if i == 10:
        pairs += 1
    if i != 10:
        left += i

pairs += left // 10

if pairs >= 7:
    print(f"Great success, you created {pairs} earrings.")
else:
    diff = abs(pairs - 7)
    print(f"Keep trying, you need {diff} more earrings.")