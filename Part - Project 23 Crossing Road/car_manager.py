from turtle import Turtle
import random


COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []  # store active car turtles
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)  # reduce spawn rate so not every loop creates a car
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)  # random Y position within screen bounds
            new_car.goto(300, random_y)
            self.cars.append(new_car)  # add the new car to the list

    def move_cars(self):
        for car in self.cars:  # move every created car
            car.backward(self.car_speed)

    def level_up(self):
        # increase car speed on level up
        self.car_speed += MOVE_INCREMENT

