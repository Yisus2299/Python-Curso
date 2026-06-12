
import random

usuario = int(input("Choose: 0 Rock, 1 Paper, 2 Scissors "))
opciones = ["Rock", "Paper", "Scissors"]
pc = random.randint(0,2)
eleccion_usuario = opciones[usuario]
computadora_eleccion = opciones[pc]
print(f"you chose {eleccion_usuario}")
print(f"the machine chose {computadora_eleccion}")
if usuario == pc:
    print("Tie!")
elif (eleccion_usuario == "Rock" and computadora_eleccion == "Scissors") or \
     (eleccion_usuario == "Paper" and computadora_eleccion == "Rock") or \
     (eleccion_usuario == "Scissors" and computadora_eleccion == "Paper"):
    print("You won!")
else:
    print("You lost!")

