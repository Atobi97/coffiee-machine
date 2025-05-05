MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink):
    for item in drink["ingredients"]:
        if resources[item] < (drink["ingredients"][item]):
            print(f"Sorry there's not enough {item}")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.1
    nickles = int(input("How many nickles: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    payment = round(quarters + dimes + nickles + pennies, 2)
    return payment


def check_transaction(user_payment, drink_price,):
    global profit
    change = user_payment - drink_price
    if user_payment >= drink_price:
        profit += drink_price
        if change > 0:
            print(f"Your change is {change}")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink, name):
    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]
    print(f"Here is your {name}. Enjoy!")


profit = 0
turn_off = False
while not turn_off:
    answer = input("What would you like? (espresso/latte/cappuccino):").lower()
    if answer == "off":
        turn_off = True
    elif answer == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}$")
    elif answer in MENU:
        drink = MENU[answer]
        if check_resources(drink):
            user_pay = process_coins()
            if check_transaction(user_pay, drink["cost"]):
                make_coffee(drink, answer)
