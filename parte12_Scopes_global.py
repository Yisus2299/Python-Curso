#scope y el proyecto llamado: Adivinar el numero

enemies = 1

def incrementar():
    enemies = 2
    #print(f"los enemigos adentro son: {enemies}")

#incrementar()
#print(f"Los enemigos afuera de la funcion: {enemies}")

#local scope: existe dentro de la función.

def drink_potion():
    pocion_fuerza = 2 #pocion_fuerza está definido dentro de drink_potion.
    # Esa variable solo “vive” dentro de esa función; fuera de ella no la deberías usar (saldría NameError si intentas acceder). 
    print(pocion_fuerza)

#drink_potion()

#global scope: existe a nivel del archivo (fuera de funciones).

salud_jugador = 10 #salud_jugador = 10 está en el “scope global”
# así que se puede usar desde cualquier parte del archivo (incluidas funciones), siempre que no haya una variable local con el mismo nombre que la “tape”

def game():
    def drink_potion():
        pocion_fuerza = 2
        print(salud_jugador)

    drink_potion()
#game() #en este caso metimos a drink_potion dentro de otra funcion asi que, debemos de llamar a game() para ejecutarlo

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#No hay Block Scope en Python

nivel = 3
enemies = ['aliens', 'zombies','vampiros']

def crear_enemigo():
    nuevo_enemigo = ""
    if nivel < 5:
        nuevo_enemigo+= enemies[0]
    return print(f"el enemigo es: {nuevo_enemigo}")
#crear_enemigo()

#===================================================================================================================================================================#

#escribir una funcion que diga si un numero es primo o no:

def is_prime(num): # crea una función que recibe un número num y decide si es primo.
    #Caso rápido: números menores que 2
    if num < 2: #si el numero es menor a 2 no cuenta como primo
        return False
    for i in range(2, num): #Buscas divisores: Genera valores i = 2, 3, 4, ... hasta llegar al numero colocado
        #empezamos en 2 ya que 1 no cuenta, y avanza 2,3,4,5,6,7... hasta llegar al numero que asignamos
        if num % i == 0: #si el numero que se divide da 0 o parecido entonces:
            return False  # Si encuentras un divisor, NO es primo
    return True #  # Si encuentras un divisor, NO es primo

#print(is_prime(2)) #ponemos el numero 2 como ejemplo ya que es primo y funciona

#====================================================================================================================================================================#
#Me quede en How to modify a global variable - video 89 (cambiar contrasena del banco isis :u)
# Modificando el Global Scope
enemigos = 1

def incrementar_enemigos(enemy):
    print(f"los enemigos adentro de la funcion: {enemigos}")
    return enemy + 1

enemigos = incrementar_enemigos(enemigos)
#print(f"enemigos afuera de la funcion: {enemigos}")

#=====================================================================================================================================================================#

#global constants 
# se trata de que las URLs como: GOOGLE, FACEBOOK, INSTAGRAM y formulas matematicas como PI van casi siempre en mayusculas y las podemos llamar 
# despues si estan antes de la funcion que queramos crear


