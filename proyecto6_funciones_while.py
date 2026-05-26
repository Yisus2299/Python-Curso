# proyecto inventado "escapa del laberinto"
#no hay escape pero realmente esto ejemplifica que sin un while, se acabaria apenas dice "hay una pared ahi" y similar
posicion = 0
salida = 6

while posicion != salida:
    print("Estás en:", posicion)
    movimiento = input("Escribe izquierda o derecha: ").lower()
    if movimiento == "izquierda":
        nueva = posicion - 1
        if nueva < 0:
            print("No puedes salir del laberinto.")
        elif nueva == 2 or nueva == 5:
            print("Hay una pared ahí.")
        else:
            posicion = nueva
    elif movimiento == "derecha":
        nueva = posicion + 1
        if nueva > 6:
            print("No puedes salir del laberinto.")
        elif nueva == 2 or nueva == 5:
            print("Hay una pared ahí.")
        else:
            posicion = nueva
    else:
        print("Escribe solo 'izquierda' o 'derecha'.")
print("¡Felicidades, escapaste!")