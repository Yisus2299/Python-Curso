# GUI
# Graphical
# User
# Interface
from tkinter import *


window = Tk()
window.title("My First GUI Program") # sets the window title
window.minsize(width=500, height=300)

# Label

my_label = Label(window, text="New Text", font=("Arial", 24, "italic"))
my_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# new button

new_button = Button(window, text="New Button")
new_button.grid(row=0, column=2, padx=10, pady=10)

# Button

def button_clicked():
     print("Button clicked")
     new_text = entry.get()
     print(new_text)
     my_label.config(text=new_text) # text= updates the label with the new text


# Click Me button:

button = Button(window, text="Click Me", command=button_clicked)
button.grid(row=1, column=1, padx=10, pady=10) # grid positions the widget


# Entry

entry = Entry(window, width=20) # creates a text input box
entry.grid(row=2, column=3, padx=10, pady=10)
# print(entry.get()) # prints the input text when clicked






window.mainloop()