from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.color("black", "green")
        self.ir_inicio()
    
    def go_up(self):
        self.forward(MOVE_DISTANCE) #Sin esta funcion no podremos mover a la tortuga o lo que hagamos
    
    def ir_inicio(self):
        self.goto(STARTING_POSITION) #para volver al inicio


    def goal(self): #para saber si pasamos la meta que es el tope de arriba
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    
