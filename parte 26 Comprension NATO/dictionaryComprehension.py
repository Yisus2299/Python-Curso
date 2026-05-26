#partiendo de lo visto anteriormente que mas o menos era asi:

#nombres_cortos = [name for name in nombres if len(name) < 5]

#la formula para los diccionarios es la siguiente:

# new_dict = {new_key:new_value for (key,value) in dict.items()}
import random
names = ['Alekk', 'Ryo', 'Zyran', 'Nana']

students_scores = {student:random.randint(1,100) for student in names} #me muestra los diferentes nombres y cada uno tiene un valor random


passed_students = {student:score for (student, score) in students_scores.items()} #Recorre cada par (clave, valor) de students_scores con .items().
# Para cada par, crea una entrada student: score en un nuevo diccionario.
# print(passed_students)


# ejercicio 1:

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
result =  {word: len(word) for word in words}
# print(result)

# ejercicio 2:

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: (temp_c * 9/5) + 32 for day, temp_c in weather_c.items()} #items es cuando ya hay un valor en el direccion, es decir, Monday: 12 <-- 12 es el valor que regresara

# print(weather_f)

semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
dias = [dia for dia in semana]
# print(dias)

#=======================================================================================================================================================================================#

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}


for (key, value) in student_dict.items():
    print(value)




