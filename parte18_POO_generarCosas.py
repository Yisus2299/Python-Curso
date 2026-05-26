#turtle y interfaz grafica (GUI) video 130

from turtle import Turtle, Screen, colormode, pen, speed, circle
import random

import heroes

tortuga = Turtle()
tortuga.shape("turtle")
tortuga.color("black", "orange")

#========================================================================================================================================#

''' 1 - #si queremos dibujar figuras que vayan en diferentes angulos debemos de crear variables

#podemos colocar el numero de angulos a recorrer estaticamente como: num_sides = 5
# pero si realmente queremos que el numero no sea estatico y quee el numero cambie, es con una funcion

colors = ['Green','Red','Orange','Yellow','Purple','IndianRed','wheat','SeaGreen'] #creamos una variable para almacenar los colores

def forma(num_sides):
    angle = 360 / num_sides #sacamos esta variable afuera para tener diferentes formas
    for i in range(num_sides):
        tortuga.forward(100)
        tortuga.right(angle)

for shape_side in range(3,11):
    tortuga.color(random.choice(colors)) #importamos random para que eliga los colores aleatoriamente
    forma(shape_side) #hacemos otro bucle For y le metemos adentro la funcion para hacer otra figura'''

#==========================================================================================================================================#

#2- Random walk

'''colormode(255) #en lugar de nosotros poner los colores como en la pasada. Existe este atributo que nos permite asignarlo de manera aleatoria

def random_color(): #creamos una funcion para evitar repetir el codigo mil veces xd
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color= (r,g,b) # y almacenamos todo en una variable con una tupla y lo regresamos
    return random_color


direccion = [0, 90, 180, 270] #cremos unas direcciones aleartorias
tortuga.pensize(10) #esto aumenta el tamano de las lineas que la tortuga dibuja
tortuga.speed(10) #aumenta la velocidad dela tortuga coloreando

for _ in range(200):
    tortuga.color(random_color())
    tortuga.forward(30)
    tortuga.setheading(random.choice(direccion))'''

#===========================================================================================================================================#

# 3 - dibujar un Spirografo

colormode(255)
tortuga.speed("fastest") #mantenemos que el sistema eliga los colores aleatoriamente y la velocidad con la que los pinta

def random_color(): #mantenemos la funcion de los colores
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colores = (r,g,b)
    return colores

def spirograph(gap): #creamos una funcion en donde el espaciado sea minimo o mas grande, depende de nosotros
    for _ in range(int(360 / gap)): #usamos un bucle For para que lo haga automaticamente sin necesidad de que nosotros pongamos linea tras linea
        tortuga.color(random_color()) #color aleatorio
        tortuga.circle(100) #generamos un circulo una y otra, y otra, y otra
        tortuga.setheading(tortuga.heading() + gap)
# tortuga.setheading(...) fija la nueva dirección con ese resultado
#tortuga.heading() obtiene el ángulo actual (por ejemplo 0, 90, 180...).
#+ gap le suma un incremento (por ejemplo 10 grados).
spirograph(5)






















pantalla = Screen()
pantalla.exitonclick()







# https://pypi.org/project : para importar cosas y leer documentacion tenemos la pagina de piyi
# import heroes
# print (heroes.genarr(10))