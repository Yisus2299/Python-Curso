#Funciones con salidas : return/continue/break

# def format_name(f_name, l_name, M_name ):
#     print(f_name.title())
#     print(l_name.title())
#     print(M_name.title())

# format_name(f_name = "angela", l_name = "aNGelA", M_name ="ANGELA")

def format_name(f_name, l_name ):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    
#formated_string = format_name("AnGeLa","YU") - esta es una manera de hacerlo
#print(format_name("AnGeLa","YU")) #esta es otra manera de hacerlo
#------------------------------------------------------------------------------#
def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("Hello"))
#print(output)
#------------------------------------------------------------------------------#

def format_name(f_name, l_name):
    if f_name == "" or l_name =="":
        return "No pusiste nada"
    else:
        formatted_f_name = f_name.title()
        formatted_l_name = l_name.title()
        return f"Resultado: {formatted_f_name} {formatted_l_name}"

# print(format_name(input("Cual es tu primer nombre?: "), input("Cual es tu apellido?: ")))

#--------------------------------------------------------------------------------------------------------#

#----------------------------------------Docstrings:

def format_name(f_name, l_name):
    '''Toma el primer nombre y el apellido para formar un Return el Title case de la version del nombre'''
    if f_name == "" or l_name =="":
        return "No pusiste nada"
    else:
        formatted_f_name = f_name.title()
        formatted_l_name = l_name.title()
        return f"Resultado: {formatted_f_name} {formatted_l_name}"

formated_name = format_name("AnGeLa","yU")

length = len(formated_name)

# print(length)

