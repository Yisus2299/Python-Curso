#volvemos a hacer el sistema de la cafetera pero con POO (la documentacion es la que trae todas las funciones y sus nombres por si acaso)

from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like?{options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report() #muestra el reporte de los ingredientes disponibles y si cambian
        money_machine.report() #muesta el reporte del dinero y la cantidad que se tiene
    else:
        drink = menu.find_drink(choice) #choice es order_drink
        if (coffee_maker.is_resource_sufficient(drink)):
            if (money_machine.make_payment(drink.cost)):
                coffee_maker.make_coffee(drink)