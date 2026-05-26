# GUI
# Graphical
# User
# Interface
from tkinter import *


window = Tk()
window.title("Mi primera Programa GUI") #pone titulo al programa
window.minsize(width=500, height=300)

# Label

my_label = Label(window, text="New Text", font=("Arial", 24, "italic"))
my_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

#nuevo boton

new_button = Button(window, text="New Button")
new_button.grid(row=0, column=2, padx=10, pady=10)

#Button

def boton_pulsado():
     print("Fui clickeado")
     new_text = entrada.get()
     print(new_text)
     my_label.config(text=new_text) #text= esto ejecuta lo que le pongas despues de text


# boton de Click Me:

# boton de Click Me:
button = Button(window, text="Click Me", command=boton_pulsado)
button.grid(row=1, column=1, padx=10, pady=10) #es un metodo usado para registrar y posicionar una ventanita con un boton


# Entry

entrada = Entry(window, width=20) #crea un recuadro de texto para escribir
entrada.grid(row=2, column=3, padx=10, pady=10)
# print(entrada.get()) #muestra por pantalla lo que escribas al darle click me






window.mainloop()