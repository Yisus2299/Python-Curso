from turtle import Screen
from player import Player
from car_manager import CarManager
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=680, height=600)
screen.tracer(0)

player = Player()
player.speed("fast")
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "w")


game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with a car: if any car is close to the player, end game
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    # if player reached the top of the screen:
    if player.reached_goal():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()



screen.exitonclick()






