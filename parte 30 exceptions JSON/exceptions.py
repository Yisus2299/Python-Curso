'''
try: algo que puede causar una exception

except: haz esto si habia una exception

else: haz esto si no hay exceptiones

finally: haz esto sin importar que suceda
'''

# hagamos nuestras propias excepciones

# try:
    # file = open("a_file.txt") # sin la variable, el archivo no existe asi que, habra un error
    # a_dictionary = {"Key":"value"}
    # print(a_dictionary["sdsfs"])
# except FileNotFoundError:
    # print("Habia un error") #hay un error ya que el archivo de arriba no existe
    # file = open("a_file.txt", "w")
    # file.write("Something")
#else:
 # si todo sale bien entonces colocamos esto aqui ya que no hay ninguna excepcion
# finally:
  # se ejecutara sin importar que
  # raise TypeError, ValueError, etc, etc, etc

#=====================================================================================================#

altura = float(input("altura: "))
peso = int(input("Peso: "))

if altura >= 3:
    raise ValueError("Los humanos no deberian de medir 3 metros") # Raise hace que te aparezca un mensaje con lo que pongamos en parentesis

# bmi = peso / altura ** 2
# print(bmi)













