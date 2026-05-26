from turtle import Turtle

STARTING_POSITIONS  = [(0,0), (-20,0), (-40,0)] #creamos una tupla con las posiciones que querran recorrer
# y creamos un ciclo For para que las recorra. Esto en lugar de crear segmentos uno por uno
# y les asignamos los datos como los colores, la forma y las posiciones gracias al For y las coordenadas
MOVE_DISTANT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = [] #todo lo hecho en el bucle For lo guardamos aqui
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS: #crea la serpiente
            self.agregar_segmento(position)

    def agregar_segmento(self, position): #agregamos la posicion para agregar adentro el segmento
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def reinicio_serpiente(self): #esto lo colocamos para cuando perdamos, la serpiente vuelva a aparecer en el inicio en lugar de acabar el juego
        for seg in self.segments:
            seg.goto(1000, 1000) #creamos un For ya que, cada que morimos, la serpiente se queda en el lugar en donde morimos
            #asi que, esto reunira todos los segmentos que conforman a la serpiente y los mandaran lejos
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    
    def extender(self):
        self.agregar_segmento(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1,  0, -1): #para que la serpiente se mueve
            nex_x = self.segments[seg_num - 1].xcor()
            nex_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(nex_x, nex_y)
        self.head.forward(MOVE_DISTANT)

    def up(self):
        if self.head.heading() != DOWN:
         self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)



    def right(self):
        if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)

    
        
