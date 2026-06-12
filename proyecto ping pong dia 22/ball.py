from turtle import Turtle
import random

class Ball(Turtle):  # All created functions initialize, whether inherited or not
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.1
    
    def move(self):
        new_x = self.xcor() + self.x_move  # calculate new x position
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1  # reverse the y direction when bouncing vertically
        # reduce speed slightly on bounce
        self.speed *= 0.9
    def bounce_x(self):
        self.x_move *= -1
    
    def reset_position(self):
        self.goto(0, 0)  # send the ball back to the center
        self.speed = 0.1
        self.bounce_x() #si revisamos la funcion, vemos que dependiendo de para donde se vaya, va al lado contrario