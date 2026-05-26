# reto 1: hacer que con la w te muevas hacia adelante, s atrras, a te gires y d dibujes
from turtle import Turtle, Screen, color, shape, textinput
import random
import turtle

'''tim = Turtle()
# tim.speed("fast")
screen = Screen()


def mover_adelante():
    tim.forward(10)

def move_atras():
    tim.backward(10)

def girar_izquierda():
    new_heading = tim.heading() + 10 #consultar el ángulo actual
    tim.setheading(new_heading) # fijar el ángulo a un valor concreto.

def girar_derecha():
    new_heading = tim.heading() - 10 #consultar el ángulo actual
    tim.setheading(new_heading)# fijar el ángulo a un valor concreto.

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen() #Hace que la ventana escuche eventos del teclado. Sin esto, las teclas suelen no responder.
screen.onkey( fun=mover_adelante, key= "w" )
screen.onkey( fun=move_atras, key = "s" )
screen.onkey( fun=girar_izquierda, key = "a" )
screen.onkey( fun=girar_derecha, key = "d" ) #asocia la tecla que ponemos como Key para que haga una accion, en este caso moverse hacia adelante
screen.onkey( fun=clear, key = "c" )
#si ponemos fun=mover_adelante(), no se movera. Ya que, con parentesis la funcion ejecuta el programa de una vez y luego el Onkey, los parentesis tienen mas prioridad
screen.exitonclick()'''
#============================================================================================================================================================================#

# reto 2 - agregar mas tortugas. Podemos usar las clases o blueprints

is_race_on = True
screen = Screen()
screen.setup(width=500,height=450) #configura el tamano del recuadro o la ventana que se abre
user_bet = screen.textinput(title="Haz tu apuesta", prompt="Cual tortuga ganara la carrera? pon el color: ") #hace aparecer un mensaje con input por pantalla
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
                print(f"El ganador fue la tortuga {winning_color}. ")
            else:
                print(f"perdiste. Gano la tortuga {winning_color}. ")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

















screen.exitonclick()







