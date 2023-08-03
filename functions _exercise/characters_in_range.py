first_symbol = input()
second_symbol = input()


def symbol(f, s):
    collectins = []
    for ch in range(ord(first_symbol) + 1, ord(second_symbol)):
        collectins.append(chr(ch))
    return collectins


result = symbol(first_symbol, second_symbol)
print(" ".join(result))


