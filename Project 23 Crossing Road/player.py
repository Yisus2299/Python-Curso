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
        self.go_to_start()

    def go_up(self):
        # move the player forward
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        # return player to starting position
        self.goto(STARTING_POSITION)


    def reached_goal(self):
        # return True if player has crossed the finish line
        return self.ycor() > FINISH_LINE_Y
    
