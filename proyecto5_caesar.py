#generador de contrasenas 
import random

letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numeros = ['0','1','2','3','4','5','6','7','8','9']
simbolos = ['!','#','$','%','&','*','+','-','?','@']

cantidad_letras = int(input("ingresa la cantidad de letras que deseas agregar: "))
cantidad_numeros = int(input("ingresa la cantidad de numeros que deseas agregar: "))
cantidad_simbolos = int(input("ingresa la cantidad de simbolos que deseas agregar: "))

#creamos una variable que almacene la contrasena que crearemos
contrasena = ""

#creamos un for con un rango de las letras que el usuario desea
    #el nombre del for no importa
for contrasenas in range(cantidad_letras):
    #le sumamos eso a la variable vacia de la contrasena y le agregamos que se eliga aleatoriamente las letras
    contrasena+= random.choice(letras)

for contrasenas in range(cantidad_numeros):
    contrasena+= random.choice(numeros)

for contrasenas in range(cantidad_simbolos):
    contrasena+= random.choice(simbolos)

print(f"perfecto, tu contrasena es {contrasena}")


