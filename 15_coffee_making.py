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
profit = 0
Money = 0


def quantity(order):
    """ check's if their are sufficient resources to make the order """
    for item in order:
        if order[item] > resources[item]:
            print(f"Sorry their is not enough {item}")
            return False
    return True


def money_given(Money):
    """Money given by the user and gives back the change left. """
    print("Please insert a coin")
    Money += int(input("How many quaters? : ")) * 0.25
    Money += int(input("How many dimes?")) * 0.1
    Money += int(input("How many Nickels")) * 0.05
    Money += int(input("How many pennies")) *0.01
    return Money


def check_money(total_money, drink_cost):
    """Checks wether the money is enough or not if not then returns the money."""
    if total_money >= drink_cost:
        change = round(total_money - drink_cost, 2)
        print(f"Here is the change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("The money you enters is not sufficient.Money Refunded")
        return False


def make_coffee(name,order):
    """ removes the amount of things needed from the stored dictionary."""
    for item in order:
        resources[item] -= order[item]
    print(f"Here is your drink {name} ☕. Enjoy")




keep_going = True
while keep_going:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        keep_going = False
    elif user_input == "report":
        print(f"Water: {resources['water']}ml ")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_input]
        if quantity(drink["ingredients"]):
            payment = money_given(Money)
            if check_money(payment,drink["cost"]):
                make_coffee(user_input,drink["ingredients"])


