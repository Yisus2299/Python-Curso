#importamos el randonm randint en lugar de random
from random import randint # podemos colocar un random pero el randint es mejor ya que nos sirve para asignar desde donde hasta donde lo queremos

# creamos una variable global constante en mayusculas al inicio para seleccionar el nivel de FACIL o DIFICIL
FACIL_NIVEL_TURNOS = 10
DIFICIL_NIVEL_TURNOS = 5

#Necesitaremos una funcion para revisar o comparar la respuesta actual contra la del usuario
def revisar_respuesta(usuario_respuesta, respuesta_actual, turnos):
    '''Revisa la respuesta con adivinar, regresa el numero de turnos restantes.'''
    if usuario_respuesta > respuesta_actual:
        print("Muy alto")
        return turnos - 1
    elif usuario_respuesta < respuesta_actual:
        print("Muy bajo")
        return turnos - 1
    else: 
        print(f"adivinaste, la respuesta era {respuesta_actual}")

#luego necesitamos poner la dificultad
def poner_dificultad():
    nivel = input("Elige una dificiltad entre 'Facil' o 'Dificil': ").lower()
    if nivel == "facil":
        return FACIL_NIVEL_TURNOS
    else:
        return DIFICIL_NIVEL_TURNOS

def game():  
    print("Bienvenido al juego de adivinar el numero\n")
    print("Estoy pensando en un numero entre: 1 y 100.\n")
    respuesta = randint(1, 100)
    print(f"la respuesta correcta es: {respuesta} xd")

    turnos = poner_dificultad()
#Repetir la funcionaldiad de adivinar si lo hacen mal o falla
    adivina = 0
    while adivina != respuesta:
        print(f"Tienes {turnos} intentos restantes para adivinar el numero")
        adivina = int(input("Trata de adivinar: "))
        turnos = revisar_respuesta(adivina, respuesta, turnos)
        if turnos == 0:
            print("Te quedaste sin turnos")
            break #de hecho como nuestra variable "adivina es 0" podemos poner "return"
        elif adivina != respuesta:
            print("Adivina otra vez")

game()



