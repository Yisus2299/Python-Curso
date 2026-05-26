from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=680, height=600)
screen.tracer(0)

jugador = Player()
jugador.speed("fast")
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(jugador.go_up, "w")


game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #detectar si chocamos con un auto: creamos un for para todos los autos y una condicional. Si chocamos el juego se acaba
    for car in car_manager.autos:
        if car.distance(jugador) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    #si cruzamos al tope de la pantalla:
    if jugador.goal():
        jugador.ir_inicio()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()





screen.exitonclick()






