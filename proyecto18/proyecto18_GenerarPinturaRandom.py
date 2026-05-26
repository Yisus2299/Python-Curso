# aqui aprendimos a como generar la lista de colores basado en la imagen que tenemos en la carpeta
# es una practica porque el codigo tuve que arreglarlo con IA. Pero en escencia, solo creamos una lista vacia y basado en la imagen metimos todo en esa 
'''import os
import colorgram
# Extract 6 colors from an image.
rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
colors = colorgram.extract(os.path.join(os.path.dirname(__file__), 'image.jpg'), 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    nuevo_color = (r,g,b)
    rgb_colors.append(nuevo_color)'''

# print(rgb_colors)

#========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
from turtle import Turtle, colormode, Screen
import random



tortuga = Turtle()
tortuga.speed("fastest")
colormode(255)
tortuga.penup() #oculta la linea
tortuga.hideturtle() #oculta al personaje
lista_color = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tortuga.setheading(225) #cambia la direccion dependiendo del numero (90 - arriba por ejemplo)
tortuga.setheading(300)
tortuga.setheading(0)
numero_puntos = 100

for dot_count in range(1, numero_puntos + 1):   
    tortuga.dot(20, random.choice(lista_color))
    tortuga.forward(50)

    if dot_count % 10 == 0:
        tortuga.setheading(90)
        tortuga.forward(50)
        tortuga.setheading(180)
        tortuga.forward(500)
        tortuga.setheading(0)


pantalla = Screen()
pantalla.exitonclick()
