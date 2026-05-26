from turtle import  Screen
from paddles import Raquetas
import time
from ball import Ball
from puntaje import Puntaje

screen = Screen()
screen.bgcolor("black") #color de fondo de la pantalla
screen.setup(800, 600) #tamano de la pantalla
screen.title("PONG GAME") #titulo del juego en el recuadro de la pantallita
screen.tracer(0)# si queremos eliminar las animaciones usamos tracer(0)

paddle_der = Raquetas(350, 0) #llamamos la funcion de generar_raquetas y, las asignamos con X/Y
paddle_izq = Raquetas(-350, 0)
ball = Ball()
scoreboard = Puntaje()


screen.listen() #si o si, si ocupamos Tracer, debemos de colocar el Listen() antes

screen.onkeypress(paddle_izq.paddle_up, "Up")
screen.onkeypress(paddle_izq.paddle_down, "Down")
screen.onkeypress(paddle_der.paddle_up, "w")
screen.onkeypress(paddle_der.paddle_down, "s")

game_is_on = True
scoreboard.update_scoreboard() #llamamos a la funcion de actualizar el marcador antes del while para que se ejecute. Sino, no se mostraran los marcadores
while game_is_on:
    time.sleep(ball.velocidad)
    screen.update() # y si ocupamos tracer, debemos de crear un bucle While, y adentro colocar la funcion update()
    ball.move()
    
# detectar la colision con las paredes de arriba y abajo
    if ball.ycor() > 280 or ball.ycor() < -280:
        #necesita rebotar
        ball.bounce_y()
        #detectar colisiones con las raquetas
    if ball.distance(paddle_der) < 50 and ball.xcor() > 320 or ball.distance(paddle_izq) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        #detectar si la raqueta derecha falla
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        #detectar si la raqueta izquierda falla
    if ball.xcor() < -380:
        ball.reset_position()  
        scoreboard.r_point()




















screen.exitonclick()
