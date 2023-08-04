random_drink = input()
quantity = int(input())


def price(drink, q):
    result = None
    if drink == "coffee":
        result = q * 1.50
    elif drink == "water":
        result = q * 1.00
    elif drink == "coke":
        result = q * 1.40
    elif drink == "snacks":
        result = q * 2.00
    print(f"{result:.2f}")


(price(random_drink, quantity))

