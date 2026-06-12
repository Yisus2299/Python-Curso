# how to use OOP in Python

# we create a class specifying everything that thing can do (for example a car, the color, the doors, the windows, the kilometers, etc)
# then we create an object, which is basically a different version of the class (it is a blue car, with the same doors, windows, kilometers, etc)

# object =  # class
'''car = carBlueprint()'''

#===================================================================================================================================================#

# from turtle import Screen, Turtle
# import turtle # we do this instead of writing: turtle.Turtle()

# timmy = Turtle()

#====================================================================================================================================================#
# object attributes

# a car has attributes like:
# speed = 0
# fuel = 32

# the syntax would be: object -> car.speed <- attribute

# from turtle import Screen, Turtle

# timmy = Turtle()

# my_screen = Screen()


#====================================================================================================================================================#
# object methods

# methods refer to the functions that the object can perform

''''from turtle import Screen, Turtle, forward, left, circle

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("black", "green")
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()'''

#====================================================================================================================================================#
# python packages - pypi

from prettytable import PrettyTable
# we can change the appearance of our table with attributes

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l" # align the table information to the left
print(table)


