# turtle and graphical interface (GUI) video 130

from turtle import Turtle, Screen, colormode, pen, speed, circle
import random

import heroes

turtle = Turtle()
turtle.shape("turtle")
turtle.color("black", "orange")

#========================================================================================================================================#

''' 1 - # if we want to draw shapes that go at different angles, we must create variables

# we can set the number of sides to traverse statically like: num_sides = 5
# but if we really want the number not to be static and for the number to change, we use a function

colors = ['Green','Red','Orange','Yellow','Purple','IndianRed','wheat','SeaGreen'] # create a variable to store the colors

def forma(num_sides):
    angle = 360 / num_sides # compute this variable to create different shapes
    for i in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)

for shape_side in range(3,11):
    turtle.color(random.choice(colors)) # import random so it chooses colors randomly
    forma(shape_side) # create another for loop and call the function to draw another shape'''

#==========================================================================================================================================#

#2- Random walk

'''colormode(255) # instead of setting the colors manually like before, this attribute allows us to assign them randomly

def random_color(): # create a function to avoid repeating the code a thousand times
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b) # store everything in a tuple and return it
    return random_color


directions = [0, 90, 180, 270] # create some random directions
turtle.pensize(10) # this increases the thickness of the lines the turtle draws
turtle.speed(10) # increases the drawing speed of the turtle

for _ in range(200):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))'''

#===========================================================================================================================================#

# 3 - draw a Spirograph

colormode(255)
turtle.speed("fastest") # keep the system choosing colors randomly and control the speed at which it paints

def random_color(): # keep the color function
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

def spirograph(gap): # create a function where the spacing can be smaller or larger, depending on us
    for _ in range(int(360 / gap)): # use a for loop so it runs automatically without writing line after line
        turtle.color(random_color()) # random color
        turtle.circle(100) # draw a circle again and again
        turtle.setheading(turtle.heading() + gap)
# turtle.setheading(...) sets the new direction using that result
# turtle.heading() gets the current angle (for example 0, 90, 180...).
# + gap adds an increment (for example 10 degrees).
spirograph(5)


























screen = Screen()
screen.exitonclick()



# https://pypi.org/project : to import packages and read documentation we use the pypi page
# import heroes
# print (heroes.genarr(10))