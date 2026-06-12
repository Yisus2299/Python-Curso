size = input("What pizza size do you want? S, M, or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
pepperoni_price = 2
extra_cheese_price = 3

small_pizza = 15
medium_pizza = 20
large_pizza = 25

if size == "S":
    bill += small_pizza
elif size == "M":
    bill += medium_pizza
elif size == "L":
    bill += large_pizza

if pepperoni == "Y":
    bill += pepperoni_price
elif pepperoni == "N":
    bill += 0

if extra_cheese == "Y":
    bill += extra_cheese_price
elif extra_cheese == "N":
    bill += 0

print(f"The total pizza bill is {bill}")
