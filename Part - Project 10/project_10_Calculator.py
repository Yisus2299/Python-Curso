# project number 10 - calculator that decides operations and asks if you want to continue or not

#1- create a function to add

def add(n1, n2):
    return n1 + n2

#2- write three other functions: subtract, multiply, and divide.

def substract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

#3- add these four functions to a dictionary with the values. Keys = "+", "-", "*", "/".

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

#4- use the operations dictionary to perform calculations. Multiply 4 * 8 using the dictionary to see if it works:

# print(operations["*"](n1 = 4, n2 = 8))

#5- ask the user to enter a number, then create a for loop to iterate through all the operation symbols
# This is so the user can see all available symbols. Then ask the user to enter another number

#6- we should create another while loop in case you want to continue and this loop should accumulate the total calculations and contain the for loop created earlier

#7- we should wrap everything in another function but since that would be confusing, the best thing is to create a calculation function that stores it


def calculate():
    should_accumulate = True
    num1= float(input("What is the first number?: ")) # this variable is outside because it stores the number and also starts the loop

    while should_accumulate:
        for symbol in operations: # this comes from the dictionary
            print(symbol)
        symbol_chosen = input("Choose an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[symbol_chosen](num1, num2) # operations comes from the dictionary. Symbol to choose comes from our input and to make it work we include the variables num1,num2 in parentheses
        print(f"{num1} {symbol_chosen} {num2} {answer}")

        #8 - once you have the result, we should make a conditional to know if you want to continue calculating or if you want to stop there

        option = input(f"Type 'yes' to continue calculating with {answer}, or type 'no' to start a new calculation.").lower()

        if option == "yes":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculate()# we call the function again to run the calculator again

calculate() # we call the created function instead of creating another while loop and so it is more practical to repeat the code