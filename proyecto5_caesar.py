# password generator
import random

letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numeros = ['0','1','2','3','4','5','6','7','8','9']
simbolos = ['!','#','$','%','&','*','+','-','?','@']

cantidad_letras = int(input("enter the number of letters you want to add: "))
cantidad_numeros = int(input("enter the number of numbers you want to add: "))
cantidad_simbolos = int(input("enter the number of symbols you want to add: "))

# create a variable to store the password we will build
contrasena = ""

# create a for loop with the range for the letters the user wants
    # the for-loop variable name does not matter
for contrasenas in range(cantidad_letras):
    # add a randomly chosen letter to the password string
    contrasena += random.choice(letras)

for contrasenas in range(cantidad_numeros):
    contrasena += random.choice(numeros)

for contrasenas in range(cantidad_simbolos):
    contrasena += random.choice(simbolos)

print(f"perfect, your password is {contrasena}")


