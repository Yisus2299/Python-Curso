from turtle import Turtle
import random

class Ball(Turtle): #TODA FUNCION CREADA SE INICIALIZA, SEA HEREDADA O NO
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.velocidad = 0.1
    
    def move(self):
        new_x = self.xcor() + self.x_move #es mejor colocarlo asi xd
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1 #ni yo entendi esta verga pero bueno xd
        # esa funcion hace que si esta negativo pase a positivo, lo que quiere decir que, si pasa al lado de la raqueta de manera positiva, se regresara al lado negativo
        self.velocidad *= 0.9
    def bounce_x(self):
        self.x_move *= -1
    
    def reset_position(self):
        self.goto(0,0) #esto hace qie la pelota vuelva al inicio
        self.velocidad = 0.1
        self.bounce_x() #si revisamos la funcion, vemos que dependiendo de para donde se vaya, va al lado contrario