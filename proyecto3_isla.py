#isla con if, elif y else

print("Bienvenido a la isla del tesoro")

camino = input("estas en una encrucijada con dos caminos, que eliges: L o R? ")
if camino == "L":
    print("Elegiste irte en el camino de la izquierda y abriste una puerta que te llevo a un oceado. ")
    agua = input("Puedes elegir nadar o esperar. S o W? ")
    if agua =="S":
        print("elegiste nadar y te salvaste. Mientras nadas ves a lo lejos una costa y te quedas alli. ")
        puertas = input("Una vez llegas a la costa ves que hay tres puertas, que eliges: R o Y o B? ")
        if puertas == "R":
            print("Elegiste la puerta roja y te encontraste con un leon. Game over.")
        elif puertas == "Y":
            print("Elegiste la puerta amarilla y te encontraste con un dragon. Game over.")
        elif puertas == "B":
            print("Elegiste la puerta azul y te encontraste con el camino de regreso a casa. Game over.")
    elif agua =="W":
        print("elegiste esperar y te ahogaste. Game over.")
elif camino =="R":
    print("Elegiste irte en el camino de la derecha y encontraste un arbol. Game over.")
else:
    print("Game over.")


