# Diccionarios y Nesting

#para usar los diccionarios creados tenemos que llamarlos y usar los [] para indicar cual es
programing_dictionary = {
 "Function": " 1 - A piece of code that you can easily call over and over again.",
 "Loop": "2- The action of doing something over and over again.",
}

#asi podemos agregar cosas de manera externa a los diccionarios
programing_dictionary["Bug"] = "3- An error in a program that prevents the program from running as expected."
programing_dictionary["Practica"] = "4- Una practica a ver en donde se agrega esto al diccionario."

# print(programing_dictionary)

empty_dictionary = {}
empty_dictionary["existing"] = "algo para saber que la lista no esta vacia"
# print(empty_dictionary["existing"])

#2- editar un item en un diccionario

programing_dictionary["Bug"] = "se cambio el contenido del Bug"
#print(programing_dictionary)

#3- Bucle a traves de un diccionario: el for muestra todo lo que hay en el diccionario
# for _ in programing_dictionary:
    # print(_)

#4- ejercicio
# de los nombres de los estudiantes con los puntajes que tenemos
# necesitamos saber quien tiene mejor nota, para eso usamos condicionales para comparar los puntajes


student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

#creamos un bucle for con las variables de nombres y puntajes
# el cual recorrera todo el diccionario de puntajes
for nombre, puntaje in student_scores.items():
    if puntaje >= 91:
        student_grades[nombre] = "Sobresaliente"
    elif puntaje >= 81:
        student_grades[nombre] = "Puedes mejorar"
    elif puntaje >= 71:
        student_grades[nombre] = "Nada mal"
    else:
        student_grades[nombre] = "Fallaste"

#print(student_grades)

#Nesting
#es la combinacion de una lista con un diccionario

viajes = {
    "Francia": {
        "ciudades visitadas": ["Paris","Lille","Dijon"],
        "total": 12
    },
    "Germany": {
        "ciudades visitadas": ["Berlin", "Stuttgart"],
        "total": 5
    },
}

'''print(viajes["Germany"]["ciudades visitadas"][1])''' #si queremos mostrar algo de una sola cosa, seleccionamos la rama principal y luego lo que queremos mostrar

