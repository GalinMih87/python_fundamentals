happiness = list(map(int, input().split()))
factor = int(input())
result = []
count = 0
average = (sum(happiness) * factor) / len(happiness)

for h in happiness:
    result.append(h * factor)


for j in result:
    if j >= average:
        count += 1

if count >= (len(happiness) / 2):
    print(f"Score: {count}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {count}/{len(happiness)}. Employees are not happy!")