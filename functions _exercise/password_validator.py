def len_of_password(password):
    if 6 <= len(password) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def symbol_are_valid(password):
    if password.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def min_two_digits(password):
    digits_counter = 0
    for character in password:
        if character.isdigit():
            digits_counter += 1
    if digits_counter >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


some_password = input()
validated = [len_of_password(some_password), symbol_are_valid(some_password), min_two_digits(some_password)]

if all(validated):
    print("Password is valid")
