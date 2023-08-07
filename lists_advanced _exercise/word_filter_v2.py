words = input().split()
filter_words = [word for word in words if len(word) % 2 == 0]
print(*filter_words, sep="\n")
