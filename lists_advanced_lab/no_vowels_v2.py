text = input()
vowels = ["a", "u", "e", "i", "o"]
no_vowels = "".join([x for x in text if x.lower() not in vowels])
print(no_vowels)