user_funds = 10.31
item_price = float(input("Burger price: "))

if item_price < user_funds:
    print("You have enough money!")
elif item_price == user_funds:
    print("You have the precise amount of money")
elif item_price > user_funds:
    print("Sorry you don't have enough money")