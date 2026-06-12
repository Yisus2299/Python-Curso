from turtle import Turtle


class Paddle(Turtle):  # paddle class for player controls

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x, y)


    def paddle_up(self):  # move paddle up
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_down(self):  # move paddle down
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
