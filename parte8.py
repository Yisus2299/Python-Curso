# funciones con inputs / argumentos y parametros

'''def greet():

    print("Hey isis")
    print("te quiero con todo mi corazon")
    print("jamas cambies<33")'''

# greet()

#funciones que te permiten usar inputs

'''def greet_with_name(name, name2, name3, name4):
    print(F"hola {name} te quiero con todo mi corazon, siempre estare contigo<3")
    print(F"hola {name2} eres mi mejor amigo aunque te molesto jsjs")
    print(F"hola {name3} gracias por existir y me encanta lo espontanea que eres")
    print(F"hola {name4} siempre seras la mejor pintora de todas<3")

greet_with_name(name = "isis", name2= "Ryo", name3= "Nana", name4= "Selene")'''

#------------------------------------------------------------------------------------------------#
#ejercicio de dias de la semana: 2 versiones de hacerlo:

'''def life_in_weeks():
    edad = int(input("¿Cuál es tu edad? "))

    años_restantes = 90 - edad
    semanas_restantes = años_restantes * 52

    print(f"Te quedan {semanas_restantes} semanas (aprox).")'''

# life_in_weeks() #segunda forma con sin inputs

'''def life_in_weeks(edad):
    años_restantes = 90 - edad
    semanas_restantes = años_restantes * 52
    print(f"Te quedan {semanas_restantes} semanas (aprox).")

life_in_weeks(22)'''

#-------------------------------------------------------------------------------------------#
#ejercicio 2 -- love calculator

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
