"""Coffee machine program using simple OOP wrappers.

This script ties together `MoneyMachine`, `CoffeeMaker` and `Menu`.
"""

from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()  # show remaining ingredients
        money_machine.report()  # show current profit
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)