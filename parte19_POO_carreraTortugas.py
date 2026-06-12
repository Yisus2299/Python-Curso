# challenge 1: make it so w moves forward, s moves back, a turns and d draws
from turtle import Turtle, Screen, color, shape, textinput
import random
import turtle

'''tim = Turtle()
# tim.speed("fast")
screen = Screen()


def move_forward():
    tim.forward(10)

def move_back():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10 # get the current angle
    tim.setheading(new_heading) # set the heading to a specific value.

def turn_right():
    new_heading = tim.heading() - 10 # get the current angle
    tim.setheading(new_heading)# set the heading to a specific value.

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen() # makes the window listen for keyboard events. Without this, keys usually don't respond.
screen.onkey( fun=move_forward, key= "w" )
screen.onkey( fun=move_back, key = "s" )
screen.onkey( fun=turn_left, key = "a" )
screen.onkey( fun=turn_right, key = "d" ) # associates the key we set with an action, in this case moving forward
screen.onkey( fun=clear, key = "c" )
# if we use fun=move_forward(), it will not move. Because with parentheses the function runs immediately and then Onkey, parentheses have higher precedence
screen.exitonclick()'''
#============================================================================================================================================================================#

# challenge 2 - add more turtles. We can use classes or blueprints

is_race_on = True
screen = Screen()
screen.setup(width=500,height=450) # configure the size of the window that opens
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? enter the color: ") # shows a message with an input on screen
colors = ['red','orange','green','blue','purple','black']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for index in range(len(colors)):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x= -230, y= y_positions[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"The winner was turtle {winning_color}.")
            else:
                print(f"You lost. Turtle {winning_color} won.")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

















screen.exitonclick()







