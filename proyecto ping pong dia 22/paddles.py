from turtle import Turtle


class Raquetas(Turtle): #creamos la primera clase y le asignamos la variable
    
    def __init__(self, x,y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x,y)
    

    def paddle_up(self): #esta logica es para poder mover la raqueta de arriba a abajo y ademas con los limites de X/Y
        nuevo_y = self.ycor() + 20
        self.goto(self.xcor(), nuevo_y)

    def paddle_down(self):
        nuevo_y = self.ycor() - 20
        self.goto(self.xcor(), nuevo_y)
