list1 = input().split(", ")
list2 = input().split(", ")
substring = []
for word1 in list1:
    for word2 in list2:
        if word1 in word2 and not word1 in substring:
            substring.append(word1)
            break
print(substring)