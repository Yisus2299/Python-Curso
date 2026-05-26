# Proyecto 84 - El dia de hoy estare haciendo el juego de Tic Tac Toe en linea de comandos asi que vamos por partes sobre como hacerlo.
# 1- Lo primero es crear una variable global con las combinaciones ganadoras y utilidades del tablero:

COMBINACIONES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


# 2- creamos la funcion que crea el tablero

def crear_tablero():
    return [" "] * 9


# 3- creamos la funcion que muestra el tablero

def mostrar_tablero(tablero):
    def celda(i):
        return tablero[i] if tablero[i] != " " else str(i + 1)

    print()
    print(f" {celda(0)} | {celda(1)} | {celda(2)} ")
    print("---+---+---")
    print(f" {celda(3)} | {celda(4)} | {celda(5)} ")
    print("---+---+---")
    print(f" {celda(6)} | {celda(7)} | {celda(8)} ")
    print()


# 4- creamos la funcion que verifica si hay un ganador

def hay_ganador(tablero, jugador):
    return any(
        tablero[a] == tablero[b] == tablero[c] == jugador
        for a, b, c in COMBINACIONES
    )


# 5- creamos la funcion que verifica si el tablero esta lleno

def tablero_lleno(tablero):
    return " " not in tablero


# 6- creamos la funcion que verifica si el movimiento es valido

def movimiento_valido(tablero, posicion):
    if posicion < 1 or posicion > 9:
        return False
    return tablero[posicion - 1] == " "


# 7- creamos la funcion que aplica la jugada

def aplicar_jugada(tablero, posicion, jugador):
    tablero[posicion - 1] = jugador


# 8- creamos la funcion que pide la jugada del jugador (nosotros):

def pedir_jugada(tablero):
    while True:
        entrada = input("Elige casilla (1-9): ").strip()
        try:
            pos = int(entrada)
        except ValueError:
            print("Escribe un número del 1 al 9.")
            continue
        if movimiento_valido(tablero, pos):
            return pos
        print("Casilla ocupada o fuera de rango. Intenta otra vez.")


# 9- creamos la funcion que implementa el algoritmo Minimax para la IA:

''' Aclaracion: Minimax es un algoritmo que se utiliza para encontrar la mejor jugada en un juego de dos jugadores.
-- La IA busca la mejor jugada para maximizar su puntuacion (maximizador)
-- El usuario busca la mejor jugada para minimizar la puntuacion de la IA (minimizador)
-- La IA busca la mejor jugada para maximizar su puntuacion
'''

def minimax(tablero, es_turno_ia, jugador_ia, jugador_humano):
    if hay_ganador(tablero, jugador_ia):
        return 10
    if hay_ganador(tablero, jugador_humano):
        return -10
    if tablero_lleno(tablero):
        return 0

    if es_turno_ia:
        mejor = -float("inf")
        for i in range(9):
            if tablero[i] == " ":
                tablero[i] = jugador_ia
                puntaje = minimax(tablero, False, jugador_ia, jugador_humano)
                tablero[i] = " "
                mejor = max(mejor, puntaje)
        return mejor

    peor = float("inf")
    for i in range(9):
        if tablero[i] == " ":
            tablero[i] = jugador_humano
            puntaje = minimax(tablero, True, jugador_ia, jugador_humano)
            tablero[i] = " "
            peor = min(peor, puntaje)
    return peor


# 10- creamos la funcion que encuentra la mejor jugada para la IA:

def mejor_jugada_ia(tablero, jugador_ia, jugador_humano):
    mejor_puntaje = -float("inf")
    mejor_pos = None
    for i in range(9):
        if tablero[i] == " ":
            tablero[i] = jugador_ia
            puntaje = minimax(tablero, False, jugador_ia, jugador_humano)
            tablero[i] = " "
            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_pos = i + 1
    return mejor_pos


# 11- creamos la funcion que implementa el modo de juego contra la IA:

def jugar_dos_jugadores():
    tablero = crear_tablero()
    turno = "X"

    while True:
        mostrar_tablero(tablero)
        print(f"Turno del jugador {turno}")
        pos = pedir_jugada(tablero)
        aplicar_jugada(tablero, pos, turno)

        if hay_ganador(tablero, turno):
            mostrar_tablero(tablero)
            print(f"¡Ganó el jugador {turno}!")
            break
        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("Empate.")
            break

        turno = "O" if turno == "X" else "X"


# 12- creamos la funcion que implementa el modo de juego contra la IA:

def jugar_contra_ia():
    tablero = crear_tablero()
    humano = "X"
    ia = "O"
    turno_humano = True

    print("\nEres X. La IA es O.")
    print("Si quieres tener opciones, intenta ganar o empatar.\n")

    while True:
        mostrar_tablero(tablero)

        if turno_humano:
            print("Tu turno (X)")
            pos = pedir_jugada(tablero)
            aplicar_jugada(tablero, pos, humano)

            if hay_ganador(tablero, humano):
                mostrar_tablero(tablero)
                print("¡Ganaste!")
                break
            if tablero_lleno(tablero):
                mostrar_tablero(tablero)
                print("Empate.")
                break

            turno_humano = False
        else:
            print("Turno de la IA...")
            pos = mejor_jugada_ia(tablero, ia, humano)
            aplicar_jugada(tablero, pos, ia)
            print(f"La IA jugó en la casilla {pos}")

            if hay_ganador(tablero, ia):
                mostrar_tablero(tablero)
                print("Ganó la IA.")
                break
            if tablero_lleno(tablero):
                mostrar_tablero(tablero)
                print("Empate.")
                break

            turno_humano = True


# 13- creamos la funcion que implementa el menu principal:

def main():
    print("=== TIC TAC TOE ===")
    print("1. Dos jugadores")
    print("2. Jugar contra la IA")
    opcion = input("Elige modo (1 o 2): ").strip()

    if opcion == "1":
        jugar_dos_jugadores()
    elif opcion == "2":
        jugar_contra_ia()
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()

# jaja cree una buena IA gracias al minimax pero es casi improbable de ganarle, seria buena idea pedir el tipo de dificultad