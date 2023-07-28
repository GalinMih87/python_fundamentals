""""
Вариант 1

words = input().split()
result = [word * len(word) for word in words]
print(''.join(result))
"""

"""
Вариант 2

words = input().split()
result = ''
for word in words:
    length = len(word)
    result += word * length
print(result)
"""

print(''.join(map(lambda word: word * len(word), input().split())))
