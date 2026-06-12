'''
try: algo que puede causar una exception

except: haz esto si habia una exception

else: haz esto si no hay exceptiones

finally: haz esto sin importar que suceda
'''

# hagamos nuestras propias excepciones

# try:
    # file = open("a_file.txt") # without the file, this will raise an error
    # a_dictionary = {"Key":"value"}
    # print(a_dictionary["sdsfs"])
# except FileNotFoundError:
    # print("There was an error") # the above file does not exist
    # file = open("a_file.txt", "w")
    # file.write("Something")
#else:
 # if everything goes well, this block will execute when there is no exception
# finally:
  # this will run regardless of whether an exception was raised

#=====================================================================================================#

altura = float(input("altura: "))
peso = int(input("Peso: "))

if altura >= 3:
    raise ValueError("Los humanos no deberian de medir 3 metros") # Raise hace que te aparezca un mensaje con lo que pongamos en parentesis

# bmi = peso / altura ** 2
# print(bmi)













