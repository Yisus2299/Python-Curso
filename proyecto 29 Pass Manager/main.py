from email import message
from pathlib import Path #importamos pathlib para poder luego usar la imagen que queremos 
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

BASE_DIR = Path(__file__).resolve().parent #creamos una constante para luego usar la imagen

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','*','+','-','?','@']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symnols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list =  password_letters + password_numbers  + password_symnols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
#===================================Find Password ======================================#
def find_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please enter a website")
        return

    data_file_path = BASE_DIR / "data.json"

    try:
        with open(data_file_path, "r", encoding="utf-8") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops", message="No details for the website exists")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(): #creamos una funcion de guardar para asi poder usarla luego y ahorrar codigo
    # Tenemos el termino Append que agrega las cosas al final de una lista o archivo
    # Y tenemos el metodo Write que sobreescribira el contenido existente
    

    website = website_entry.get() #los gets traen las cosas que hay en los entrys que previamente creamos
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="No dejes campos vacíos")
        return

    data_file_path = BASE_DIR / "data.json"
    # cargar otra vez la vieja informacion
    try:
        with open(data_file_path, "r", encoding="utf-8") as data_file:
            data = json.load(data_file) #lee el archivo existente. Y lo ponemos en una variable para no escribir eso a cada rato
    except FileNotFoundError:
        data = {}
        
# actualizar la informacion
    data.update(new_data) # agrega/actualiza el sitio nuevo.
    #guardar la informacion
    with open(data_file_path, "w", encoding="utf-8") as data_file:
        json.dump(data, data_file, indent=4) # vuelve a escribir todo en formato JSON.
    
    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk() #primero asignamos Tk() a una variable
window.title("Password Manager") #esto nos dice como se va a llamar lo que hacemos
window.config( padx=70, pady=70) #esto nos agranda o achica mas o menos los bordes


logo_path = BASE_DIR / "logo.png" #asignamos la constante a una variable


canvas = Canvas(window, height=200, width=200) #Crea un widget
logo_img = PhotoImage(file=str(logo_path)) #Carga el archivo PNG (o GIF) indicado por logo_path
canvas.create_image(100, 100, image=logo_img) #Dibuja la imagen dentro del canvas
canvas.logo_img = logo_img
canvas.grid(row=0, column=0, columnspan=3) # row: es el orden en que van. 0 es el primero

#Nota importante: Sin pack() (o grid() / place()), el widget existe pero no se muestra en la ventana.

# Labels: etiquetas
website_label = Label(text="Website:")
website_label.grid(row=1, column=0) #el 0 los pone a la izquierda / 1 centro / 2 derecha
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


#Entries: Entradas en donde van la informacion
website_entry = Entry(window, width=21)
website_entry.grid(row=1, column=1)
email_entry = Entry(window, width=41)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "JesusZ@gmail.com") #auto genera lo que hay en ese campo
password_entry = Entry(window, width=21)
password_entry.grid(row=3, column=1)

#Buttons: Botones
generate_password_button = Button(window, text="Generate Password", command=generate_password) 
generate_password_button.grid(row=3, column=2)
add_button = Button(window, text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(window, text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)













window.mainloop()