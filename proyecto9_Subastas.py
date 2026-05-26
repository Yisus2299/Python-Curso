#1- preguntale al usuario por el input
#2- guarda la informacion dentro de un diccionario {nombre: price}
#3- ya sea si son nuevas apuestas a ser agregadas
#4- compara las apuestas en un diccionario

def buscar_apuesta_ganadora(diccionario_apuestas):
    ganador = ""
    apuesta_ganadora = 0
    for apostador in diccionario_apuestas:
        cantidad_apuesta = diccionario_apuestas[apostador]
        if cantidad_apuesta > apuesta_ganadora:
            apuesta_ganadora = cantidad_apuesta
            ganador = apostador

    print(f"El ganador es: {ganador} con una apuesta de ${apuesta_ganadora}")

apuestas = {}

continuar_apuesta = True

while continuar_apuesta:
    nombre = input("Como te llamas?\n")
    precio = int(input("Cual es tu apuesta?: $"))
    apuestas[nombre] = precio
    continuar = input("Hay alguna otra apuesta? Escribe 'Si' o 'No'.  \n").lower()
    if continuar == "no":
        continuar_apuesta = False
        buscar_apuesta_ganadora(apuestas)
    elif continuar_apuesta == "Si":
        print("\n" * 20)