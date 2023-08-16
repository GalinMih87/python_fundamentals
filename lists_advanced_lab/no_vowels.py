text = input()
vowels = ["a", "A", "u", "U", "e", "E", "i", "I", "o", "O"]
no_vowels = "".join([x for x in text if x not in vowels])
print(no_vowels)