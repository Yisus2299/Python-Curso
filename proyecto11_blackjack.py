#1- crea una funcion deal_card() que use una lista de numeros que regresen una carta aleatoria
# primero importamos la funcion random para que la carta que seleccionemos sea aleatoria

import random

def deal_card(): #cuando llamemos a esta funcion, va a generar y devolverte un número que representa el valor de una carta.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card #La función devuelve el valor elegido.

#Tenemos que crear una funcion que calcule el puntaje de todas las cartas:

def calculate_score(cards): #creamos una funcion que recibe una lista de cartas y cards representa las cartas de una mano 
    if sum(cards) == 21 and len(cards) == 2: # sum(cards) suma todos los valores y len(cards) == 2 asegura que son exactamente 2 cartas
        return 0 #todo esto representa que el usuario o la PC sacaron un puntaje especial

    if 11 in cards and sum(cards) > 21: #Si hay un 11 y al sumar la mano te pasas de 21, entonces el As debe valer 1 en vez de 11 para que no revientes el límite.
        cards.remove(11) #Quita un 11 de la lista
        cards.append(1) #Agrega el 1 para reemplazar el valor del As por el que conviene.

    return sum(cards) #Devuelve el puntaje actualizado.

# Tenemos que crear una funcion que compare las cartas y los resultados

def compare(u_score, c_score): #puedes colocar User-score / se le cambio el nombre solo por abreviacion y ver que pasa pero funciono xdd
    if u_score == c_score:
        return "Empate" 
    elif c_score == 0:
        return "Perdiste, el oponente tiene Blackjack"
    elif u_score == 0:
        return "Ganaste con un Blackjack"
    elif u_score > 21:
        return "Pasaste, perdiste"
    elif c_score > 21:
        return "El oponente paso. Tu ganas"
    elif u_score > c_score:
        return "Tu ganas"
    else:
        return "Tu pierdes"

#Aqui es donde vamos a inicializar todas las cosas en donde se guardaran nuestros datos, primero 
#creamos dos listas vacias: 1- las cartas del usuario y las cartas de la PC / 2- agregamos el puntaje a las listas
def play_game(): #Metimos todo esto en una funcion para simplificar y llamar al codigo para poder usarlo nuevamente
    user_cards = []
    computer_cards = []
    computer_score = -1
    is_game_over = False
    '''porque ese valor se usa en el while computer_score != 0 and computer_score < 17: y Python necesita que computer_score exista para evaluar la condición; además, 
    con -1 la condición es verdadera al inicio, así que la PC entra al bucle y recién entonces calcula su puntaje real con calculate_score().'''

    #para recorrer los valores (una carta seleccionada por el usuario y otra por la PC) creamos un bucle For
    #En esas líneas se está haciendo la “mano inicial” del Blackjack: repartir 2 cartas al usuario y 2 cartas a la computadora.

    for _ in range(2):
        user_cards.append(deal_card()) #Llama a deal_card() para obtener una carta aleatoria y con append() la metemos al final de la lista vacia user_cards
        computer_cards.append(deal_card()) #Llama otra vez a deal_card() para otra carta aleatoria (independiente) y La agrega al final de computer_cards.

    '''En Blackjack normalmente se reparten 2 cartas iniciales al jugador y 2 cartas iniciales a la banca/PC.
    Usar for _ in range(2) garantiza que sean 2 cartas exactamente, sin tener que escribir el mismo código dos veces manualmente.
    Separar en dos listas (user_cards y computer_cards) hace más fácil después comparar manos, sumar puntos, detectar si se pasa de 21, etc.'''

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------#


    while not is_game_over: #Sirve para que la calculadora Blackjack se repita mientras la partida siga “viva”
        #Es decir, el código dentro del while se ejecuta una y otra vez hasta que is_game_over se vuelva True.
        user_score = calculate_score(user_cards) #  llama a la función calculate_score y le pasa esa lista.
        ''' estas funciones revisan reglas como: si el blackjack natural (21 con 2 cartas) → retorna 0 / As con valor 11 que se ajusta a 1 si te pasas de 21
        y al final devuelve sum(cards) (la suma real ajustada)''' #todo este resultado se guarda en user_score.
        computer_score = calculate_score(computer_cards) # y lo mismo aplica esta otra variable creada pero para la Pc y su cartas

        print(f"tus cartas son: {user_cards} y tu punaje actual es {user_score}")
        print(f"la primera carta del PC es {computer_cards[0]}")

        # lo que veras en esta condicional es lo siguiente:
        #1- user_score == 0: significa que el usuario tiene Blackjack natural, porque en calculate_score se usó return 0 para ese caso especial.
        #2- computer_score == 0: significa que la PC tiene Blackjack natural.
        #3- user_score > 21: el usuario se pasó (se “pasó de 21”), o sea perdió/termina.
        #4- is_game_over = True: Si se cumple la condición anterior, se marca que el juego terminó. (esto normalmente luego se usaría para salir de un while o parar el flujo)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Escribe 'Si' para tener otra carta, escribe 'no' para pasar: ").lower()
            if user_should_deal == "si": #5 - Si el usuario responde que sí, entonces:
                user_cards.append(deal_card()) #6- Se reparte una carta más al usuario y se añade a su lista.
            else:
                is_game_over = True #Si el usuario no quiere otra carta ("no" u otra cosa), se termina el juego marcando is_game_over = True.
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #por eso incluimos el (  computer_score = -1 ) 
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    print(f"Tu mano final es: {user_cards}, tu puntaje final {user_score}")
    print(f"La mano final de la PC es: {computer_cards}, tu puntaje final {computer_score}")
    print(compare(user_score, computer_score))

while input("Quieres seguir jugando el juego del Blackjack? Escribe 'si' o 'no': ") == "si":
    print("\n" * 20)
    play_game()





    