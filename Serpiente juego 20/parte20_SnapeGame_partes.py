from turtle import  Screen
from food import Food
from serpiente import Snake
from puntaje import scoreboard
import time

screen = Screen()
screen.setup(width= 600, height=600)
screen.bgcolor("black") #cambia todo el color de la ventana que aparece
screen.title("Juego de la serpiente") #coloca un mensaje al inicio de la pantallita con el mensaje que queremos
screen.tracer(0)

#aqui para mas facilidad, llamamos a las clases creadas en sus archivos correspodientes poniendolas en variables
#mi yo del futuro se confundio llamando scoreboard.incrementar puntaje en el if de las colisiones xdd
#asi que, si hacen algo con POO, revisen como llamaron a las clases en las variables paara que no les pase lo mismo 
snake = Snake()
food = Food()
puntaje = scoreboard() 

screen.listen()#es para agregar letras y acciones
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detectar las colisiones con la comida
    if snake.head.distance(food) < 15: #si la cabeza de la serpiente esta a menos de 15 pixeles
        food.refresh()
        snake.extender()
        puntaje.incrementar_puntaje()

    #detectar colision con la pared
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        puntaje.reset()
        snake.reinicio_serpiente()
        
        
    
    #detectar colision con la cola
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) < 10:
            puntaje.reset()
            snake.reinicio_serpiente()
            break
            
            


    

screen.exitonclick()