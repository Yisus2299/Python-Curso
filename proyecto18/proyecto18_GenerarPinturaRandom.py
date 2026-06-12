# Here we learned how to generate a list of colors based on an image in the project folder
# This is a practice snippet; the code was adjusted with AI help. Essentially we build an empty list and fill it based on the image.
'''import os
import colorgram
# Extract colors from an image.
rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
colors = colorgram.extract(os.path.join(os.path.dirname(__file__), 'image.jpg'), 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)'''

# print(rgb_colors)

#========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
from turtle import Turtle, colormode, Screen
import random


artist = Turtle()
artist.speed("fastest")
colormode(255)
artist.penup()  # lift the pen so it doesn't draw lines
artist.hideturtle()  # hide the turtle cursor
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

artist.setheading(225)  # change direction depending on the number (90 = up)
artist.setheading(300)
artist.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    artist.dot(20, random.choice(color_list))
    artist.forward(50)

    if dot_count % 10 == 0:
        artist.setheading(90)
        artist.forward(50)
        artist.setheading(180)
        artist.forward(500)
        artist.setheading(0)


screen = Screen()
screen.exitonclick()
