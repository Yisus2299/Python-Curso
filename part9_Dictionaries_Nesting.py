# Dictionaries and Nesting

# to use the created dictionaries we have to call them and use [] to indicate which one it is
programing_dictionary = {
 "Function": "1 - A piece of code that you can easily call over and over again.",
 "Loop": "2 - The action of doing something over and over again.",
}

# this is how we can add items externally to dictionaries
programing_dictionary["Bug"] = "3 - An error in a program that prevents the program from running as expected."
programing_dictionary["Practice"] = "4 - A practice entry to see where this is added to the dictionary."

# print(programing_dictionary)

empty_dictionary = {}
empty_dictionary["existing"] = "something to know that the list is not empty"
# print(empty_dictionary["existing"])

#2- edit an item in a dictionary

programing_dictionary["Bug"] = "the content of Bug was changed"
#print(programing_dictionary)

#3- Loop through a dictionary: the for shows everything in the dictionary
# for _ in programing_dictionary:
    # print(_)

#4- exercise
# from the student names with the scores we have
# we need to know who has the better grade, so we use conditionals to compare the scores

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

# create a for loop with the name and score variables
# which will traverse the entire scores dictionary
for nombre, puntaje in student_scores.items():
    if puntaje >= 91:
        student_grades[nombre] = "Outstanding"
    elif puntaje >= 81:
        student_grades[nombre] = "You can improve"
    elif puntaje >= 71:
        student_grades[nombre] = "Not bad"
    else:
        student_grades[nombre] = "Failed"

#print(student_grades)

# Nesting
# it is the combination of a list with a dictionary

viajes = {
    "France": {
        "visited cities": ["Paris","Lille","Dijon"],
        "total": 12
    },
    "Germany": {
        "visited cities": ["Berlin", "Stuttgart"],
        "total": 5
    },
}

'''print(viajes["Germany"]["visited cities"][1])''' # if we want to show a single item, we select the main branch and then what we want to display

