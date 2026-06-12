# Based on what we saw earlier, it was roughly like this:

# short_names = [name for name in names if len(name) < 5]

# The dictionary comprehension formula is:

# new_dict = {new_key:new_value for (key,value) in dict.items()}
import random
names = ['Alekk', 'Ryo', 'Zyran', 'Nana']

students_scores = {student:random.randint(1,100) for student in names} # assigns a random score to each name


passed_students = {student:score for (student, score) in students_scores.items()} # Iterates each pair (key, value) in students_scores using .items().
# For each pair, it creates an entry student: score in a new dictionary.
# print(passed_students)


# exercise 1:

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
result =  {word: len(word) for word in words}
# print(result)

# exercise 2:

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: (temp_c * 9/5) + 32 for day, temp_c in weather_c.items()} # items returns key/value pairs from the dictionary, e.g. Monday: 12

# print(weather_f)

week_days = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
days = [day for day in week_days]
# print(days)

#=======================================================================================================================================================================================#

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}


for (key, value) in student_dict.items():
    print(value)




