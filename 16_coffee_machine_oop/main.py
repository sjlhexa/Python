from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
coffee_maker.report()
money_machine.report()


while is_on:
    drinks = menu.get_items()

    user_input = input(f"Choose a drink {drinks}: ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        user_drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(user_drink):
            if money_machine.make_payment(user_drink.cost):
                coffee_maker.make_coffee(us
