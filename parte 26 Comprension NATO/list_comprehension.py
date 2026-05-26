numeros = [1,2,3]
nuevo_numero = [items * 2 for items in numeros]
# print(nuevo_numero)

nombre = "Alekk"
nueva_lista = [letra for letra in nombre]
# print(nueva_lista)

#python sequences
#1- list
#2- range
#3- string
#4- tuple

range_list = [num * 2 for num in range(1,6)]
# print(range_list)

# Conditional list comprehension: creamos una condicional adentro de una lista

nombres = ['Alex', 'Beth', 'Calorina', "sarah", "alekk"]

nombres_cortos = [name for name in nombres if len(name) < 5]
# print(nombres_cortos)
nombres_largos = [name.upper() for name in nombres if len(name) >= 5]
# print(nombres_largos)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]
# print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(numero) for numero in list_of_strings]
result = [int(numbers) for numbers in list_of_strings if int(numbers) % 2 == 0]
# print(result)

from pathlib import Path
base = Path(__file__).parent
file1 = base / "file1.txt"
file2 = base / "file2.txt"

with open(file1) as f1:
    numeros1 = [int(linea.strip()) for linea in f1]
with open(file2) as f2:
    numeros2 = [int(linea.strip()) for linea in f2]
result = [n for n in numeros1 if n in numeros2]
# print(result)
