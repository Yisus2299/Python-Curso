# functions with inputs / arguments and parameters

'''def greet():

    print("Hey Isis")
    print("I love you with all my heart")
    print("never change<33")'''

# greet()

# functions that allow you to use inputs

'''def greet_with_name(name, name2, name3, name4):
    print(F"hello {name}, I love you with all my heart, I will always be with you<3")
    print(F"hello {name2}, you are my best friend even though I annoy you haha")
    print(F"hello {name3}, thank you for existing and I love how spontaneous you are")
    print(F"hello {name4}, you will always be the best painter of all<3")

greet_with_name(name = "Isis", name2= "Ryo", name3= "Nana", name4= "Selene")'''

#------------------------------------------------------------------------------------------------#
# week-lifetime exercise: 2 versions to do it:

'''def life_in_weeks():
    age = int(input("What is your age? "))

    years_left = 90 - age
    weeks_left = years_left * 52

    print(f"You have {weeks_left} weeks left (approx).")'''

# life_in_weeks() # second form without inputs

'''def life_in_weeks(age):
    years_left = 90 - age
    weeks_left = years_left * 52
    print(f"You have {weeks_left} weeks left (approx).")

life_in_weeks(22)'''

#-------------------------------------------------------------------------------------------#
# exercise 2 -- love calculator

'''def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Jesus Ziegler", "Katherina Trecanao")'''
