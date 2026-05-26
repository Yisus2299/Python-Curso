from turtle import Turtle
import random


COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.autos = [] #si no creamos una lista en donde guardar los autos con los colores que tenemos, deberiamos de crear una gran cantidad de cosas xd
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        random_chance = random.randint(1, 6) #hacemos esta condicional para evitar que aparezcan millones de autos
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250) #con esto orientamos los autos desde el minimo y maximo de la pantalla
            new_car.goto(300, random_y)
            self.autos.append(new_car) #con esto agregamos los autos creados con todo a la lista que creamos arriba
    
    def move_cars(self):
        for car in self.autos: #creamos un For para mostrar todos los autos creados
            car.backward(self.car_speed) #usamos una funcion de turtle para moverlos hacia atras

    def level_up(self): #funcion para cuando ganemos, se aumente la velocidad del auto
        self.car_speed += MOVE_INCREMENT
        #Esto es lo mismo que decir: STARTING_MOVE_DISTANCE += MOVE_INCREMENT

