
import random

usuario = int(input("Elige: 0 Piedra, 1 Papel, 2 Tijeras "))
opciones = ["Piedra", "Papel", "Tijeras"]
pc = random.randint(0,2)
eleccion_usuario = opciones[usuario]
computadora_eleccion = opciones[pc]
print(f"elegiste {eleccion_usuario}")
print(f"la maquina eligio {computadora_eleccion}")
if usuario == pc:
    print("Empate!")
elif (eleccion_usuario == "Piedra" and computadora_eleccion == "Tijeras") or \
     (eleccion_usuario == "Papel" and computadora_eleccion == "Piedra") or \
     (eleccion_usuario == "Tijeras" and computadora_eleccion == "Papel"):
    print("Ganaste!")
else:
    print("Perdiste!")

