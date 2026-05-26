# lista = []

# while True:
#     palabras = input("Escribe algo (Enter vacío para terminar):\n")
#     if palabras == "":
#         break
#     lista.append()

# print(lista)

# texto = ""
# texto += input("Primera parte: ") + " "
# texto += input("Segunda parte: ")

# print(f"{texto}")

# lista = ['a','b','c','d','e']

# practica = ""

# for letra in lista:
#     practica += letra

# print(practica)

#ejercicios con diccionarios

#1- mostrar por pantalla todo el diccinario, cambiar la edad, la profesion y solo mostrar la ciudad.

'''my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}

my_dict['profession'] = 'Doctor'

my_dict['age'] = 40

print(my_dict)
print(my_dict['city'])'''

#2- ejercicio de las notas y mostrar que hacer dependiendo del caso

'''student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name, grade in student_scores.items():
    if grade >= 91:
        student_grades[name] = "Sobresaliente"
    elif grade >= 81:
        student_grades[name] = "Nada mal"
    elif grade >= 71:
        student_scores[name] = "puede mejorar"
    else:
        student_grades[name] = "reprobado"
print(student_grades)'''

# Crea un diccionario de productos y sus precios, y luego imprime cada producto y su precio usando .items().

# productos = {"Manzana": 10, "Pera": 15, "Melon": 20}

# for fruta, cantidad in productos.items():
#     print(f"Fruta: {fruta}, cantidad: {cantidad}.")


# notas = {'Ana': 8, 'Pedro': 4, 'Luis': 6}

# aprobados = {nota: nombre for nombre, nota in notas.items() if nota >= 5}

# print(aprobados)

''''usuarios = {'id1': 'admin', 'id2': 'user', 'id3': 'guest', 'id5': 'No lo se'}


usuarios['id4'] = "lector" #agregar cosas a un diccionario
usuarios.update({'id3': "solo ver"}) #actualizar algo en un diccionario
del usuarios['id5'] #eliminar cosas de un diccionario, otra opcion para borrar: #usuarios.pop('id3')

#print(usuarios)'''

#====================================================================================================================#

import random


data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Facebook',
        'follower_count': 350,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Two Door Cinema Club',
        'follower_count': 150,
        'description': 'Music Band',
        'country': 'United Kingdom'
    }
] #primero tenemos el diccionario con toda la informacion que usaremos en el ejercicio

account_a = random.choice(data) #creamos una variable para la opcion A que eliga informacion aleatoria
account_b = random.choice(data) #creamos una variable para la opcion B que eliga informacion aleatoria


def choice(account): #creamos una funcion para almacenar en variables el nombre, la descripcion y el pais
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return (f"{account_name}, {account_description} From {account_country}") #retornamos el nombre, la descripcion y el pais



def revisar(user_guess, a_follower, b_follower): #creamos una funcion que almacene una condicional para comprobar los seguidores
    if a_follower > b_follower: #si A tiene mas seguidores que B, de manera corta, regresamos la salida de la letra A
        return user_guess == "a"
    else:
        return user_guess == "b" #lo mismo para la B



should_continue = True #creamos una variable para el bucle While y que el juego continue
score = 0 #creamos una variable iniciada en 0 que almacene el puntaje si acertamos o fallamos


while should_continue: #iniciamos el bucle while en donde vamos a almacenar las variables de los seguidores, de lo contrario no funcionara
 #aqui es donde guardamos las dos variables que tienen que ver con los seguidores, para poder llamar a la funcion del condicional 
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]

#mostramos por pantalla la funcion en que a la vez llama a las opciones random y que muestren alguna opcion
    # print(f"Compara a: {choice(account_a)}")
    # print("vs")
    # print(f"Compara b: {choice(account_b)}")
    #preguntamos por pantalla cual opcion puede ser mayor
    # guess = input("Quien tiene mas seguidores? Escribe 'A' o 'B':  ").lower()
    
    #creamos una variable que de una realice la condicional
    # answer = revisar(guess, a_follower, b_follower )

    # if answer:
    #     score+=1 #si acertamos el puntaje se incrementa
    #     print(f"Acertaste, tienes razon. Puntaje actual {score}")
    #     account_a = account_b
    #     #En “Higher or Lower”, la regla habitual es: el que era la opción B pasa 
    #     # a ser la nueva A en la siguiente pregunta (el “ancla” que ya conoces). Por eso copias la referencia de B en A.
    #     account_b = random.choice(data) #La nueva opción a comparar es otra cuenta aleatoria del listado. Es la nueva “B” que el jugador debe comparar con la que ahora es A.
    #     while account_a == account_b:
    #         account_b = random.choice(data)
    #     #Si el azar repite la misma cuenta que ya es A, tendrías otra vez dos veces lo mismo en pantalla y el juego no tendría sentido. Este bucle vuelve a elegir B hasta que sea distinta de A.
    # else:
    #     print(f"Fallaste, lo siento. Puntaje actual {score}")
    #     should_continue = False #apenas fallas, se acaba el bucle y se termina el juego
    #     break

#==========================================================================================================================================================================================================#











