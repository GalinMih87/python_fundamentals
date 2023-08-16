txt = input().split()
searching_palidrom = input()
palindromes = []

for word in txt:
    if word == word[::-1]:
        palindromes.append(word)
print(f"{palindromes}")
print(f"Found palindrome {palindromes.count(searching_palidrom)} times")
