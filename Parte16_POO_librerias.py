#como usar POO en python

#creamos una clase especificando todo lo que puede hacer dicha cosa (ejemplo un auto, el color, las puertas, las ventanas, los kilometros, etc)
#luego creamos un objeto, que es basicamente una version diferente de la clase (es un auto azul, con las mismas puertas, ventanas, kilometros, etc)

#objeto =  #class
'''car = carBlueprint()'''

#===================================================================================================================================================#

# from turtle import Screen, Turtle
# import turtle #hacemos esto en lugar de colocar: turtle.Turtle()

# timmy = Turtle()

#====================================================================================================================================================#
#object attributes

#un auto tiene atributos como: 
# speed = 0
# fuel = 32

#la sintaxis seria: objeto-> car.speed <-attribute

# from turtle import Screen, Turtle

# timmy = Turtle()

# my_screen = Screen()


#====================================================================================================================================================#
#object methods

#los metodos se reieren a las funciones que puede cumplir ese objeto

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
#python packages - piyi

from prettytable import PrettyTable
#podemos cambiar la apariencia de nuestra tabla con atributos

tabla = PrettyTable()

tabla.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
tabla.add_column("Type", ["Electric", "Water", "Fire"])
tabla.align = "l" #ponemos la informacion de la tabla a la izquierda
print(tabla)


