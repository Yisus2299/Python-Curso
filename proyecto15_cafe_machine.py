
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    '''Regresa True/Verdadero cuando la orden puede ser hecha, False/Falso si los ingredientes son insuficientes'''
    is_enough = True
    for item in order_ingredients:
       if order_ingredients[item] >= resources[item]:
          print(f"sorry there is not enough {item}.")
          is_enough = False
    return is_enough


def process_coins():
    '''regresa el total calculado de las monedas puestas'''
    print("Please insert coins: ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    '''Regresa True cuando el pago fue aceptado o Falso si el dinero es insuficiente'''
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    '''Deduce los ingredientes requeridos de los recursos'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name}")    


is_on = True

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ") #para evitar que el bucle sea infinito colocamos los inputs adentro de el bucle While
    if choice == "offf":
        is_on = False
    elif choice == "report":
       print(f"Water: {resources["water"]}ml")
       print(f"Milk: {resources["milk"]}")
       print(f"Coffee: {resources["coffee"]}")
       print(f"Money: ${profit}")
    else:
        drink = MENU[choice] #muestra todo el contenido de los ingredientes que el usuario coloque en el input de choice y para hacerla corta, colocamos que drink contenga todo eso
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])