import os
from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")

class scoreboard(Turtle):
    # realmente todo bien hasta aqui. Retiramos la funcion game over que hacia que el juego se terminara y cada que regresabamos la serpiente estaba en el inicio
    # en su lugar creamos la funcion de actualizar puntaje y la de reset
    # ademas creamos la variable high_score para llevar un conteo de cual fue nuestro puntaje mas alto y continuar jugando
    # poro que falta en nuestro codigo? que cada que terminamos el programa y lo iniciamos, todos nuestros puntajes se eliminaron asi que, debemos de crear una funcion que lleve ese rastreo
    # debido a que ha recibido diferentes cambios desde la explicacion de este ejercicio en el video 184, ahora necesitamos importar Os, crear una constante en DATA_PATH ya buscar documentacion sobre como incorpoarlo

    def __init__(self):
        super().__init__()
        self.score = 0
        if os.path.isfile(DATA_PATH):
            with open(DATA_PATH, encoding="utf-8") as data:
                contenido = data.read().strip()
                self.high_score = int(contenido) if contenido else 0
        else:
            self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle() #esconde la forma hecha
        self.actualizar_puntaje()

    def actualizar_puntaje(self):
        self.clear()
        self.write(f"Puntaje: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)  #REALMENTE xd ya con el  self.clear se actualiza pero igual la creamos

    def reset(self): #creamos esto para en lugar si perdermos, se resetee el juego pero desde 0
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA_PATH, mode="w", encoding="utf-8") as data: #as data es el nombre del archivo. en este caso, data.txt
                #"w" se refiere a, si el archivo existe, lo vacia y escribe desde cero; si no existe lo crea
                data.write(str(self.high_score))
        self.score = 0
        self.actualizar_puntaje()

    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align= ALIGMENT, font= FONT)


    def incrementar_puntaje(self):
        self.score += 1
        self.actualizar_puntaje()
        # self.write(f"Puntaje: {self.score}", align=ALIGMENT, font=FONT)

        