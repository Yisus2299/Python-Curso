#Keywords: actualmente si queremos leer, modificar o algo en un archivo txt o el que sea primero


import os #importamos os
#creamos una constantesiguiendo esta formula y le agregamos el archivo txt que tengamos:
#tenemos 3 formas
DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "archivo.txt") #1- ese es en caso de que lo tengas en la misma carpeta o lugar
#2- si esta afuera en el escritorio, hay dos formas:
DATA_SCREEN = os.path.join(os.path.expanduser("~"), "Desktop", "archivo.txt") #expanduser("~") apunta al perfil del usuario y evita hardcodear ImKen.
DATA_SCREEN = r"C:\Users\ImKen\Desktop\archivo.txt" #colocamos r"la ruta en la que esta". 
#3- lo mismo si esta en otra carpeta:
DATA_SCREEN = "C:/Users/ImKen/Desktop/archivo.txt" #tambien lo podemos hacer sin la r y funciona. pero en lugar de colocar \ colocamos /
    
with open(DATA_SCREEN, mode="r", encoding="utf-8") as archivo: #decimos: with open (hacemos lo que haga el mode, en este caso, r = leer) as (el nombre del archivo)
    contents = archivo.read() # lo guardamos en una variable
    print(contents) # y lo imprimimos