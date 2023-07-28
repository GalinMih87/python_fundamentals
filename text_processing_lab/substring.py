def txt(first_str, second_str):
    while first_str in second_str:
        second_str = second_str.replace(first_str, '')
    return second_str


print(txt(input(), input()))
