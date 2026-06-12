# Functions with outputs: return/continue/break

# def format_name(f_name, l_name, M_name ):
#     print(f_name.title())
#     print(l_name.title())
#     print(M_name.title())

# format_name(f_name = "angela", l_name = "aNGelA", M_name ="ANGELA")

def format_name(f_name, l_name ):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    
#formated_string = format_name("AnGeLa","YU") - this is one way to do it
#print(format_name("AnGeLa","YU")) #this is another way to do it
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
        return "You didn't enter anything"
    else:
        formatted_f_name = f_name.title()
        formatted_l_name = l_name.title()
        return f"Result: {formatted_f_name} {formatted_l_name}"

# print(format_name(input("What is your first name?: "), input("What is your last name?: ")))

#--------------------------------------------------------------------------------------------------------#

#----------------------------------------Docstrings:

def format_name(f_name, l_name):
    '''Takes the first name and last name to return the Title case version of the name.'''
    if f_name == "" or l_name =="":
        return "You didn't enter anything"
    else:
        formatted_f_name = f_name.title()
        formatted_l_name = l_name.title()
        return f"Result: {formatted_f_name} {formatted_l_name}"

formated_name = format_name("AnGeLa","yU")

length = len(formated_name)

# print(length)

