from email import message
from pathlib import Path  # use pathlib to build paths to assets
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

BASE_DIR = Path(__file__).resolve().parent  # base directory for assets and data


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    numbers = [str(n) for n in range(10)]
    symbols = ['!', '#', '$', '%', '&', '*', '+', '-', '?', '@']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# =========================== Find Password ======================================#
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
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops", message="No details for the website exist")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Save the website/email/password entry to a local JSON file

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave fields empty")
        return

    data_file_path = BASE_DIR / "data.json"
    # load existing data if present
    try:
        with open(data_file_path, "r", encoding="utf-8") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = {}

    # update and save the data
    data.update(new_data)
    with open(data_file_path, "w", encoding="utf-8") as data_file:
        json.dump(data, data_file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()  # create main window
window.title("Password Manager")
window.config(padx=70, pady=70)


logo_path = BASE_DIR / "logo.png"


canvas = Canvas(window, height=200, width=200)  # create a canvas widget
logo_img = PhotoImage(file=str(logo_path))  # load logo image
canvas.create_image(100, 100, image=logo_img)  # draw image on the canvas
canvas.logo_img = logo_img
canvas.grid(row=0, column=0, columnspan=3)

# Note: without pack()/grid()/place() the widget exists but will not be shown.

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


# Entries
website_entry = Entry(window, width=21)
website_entry.grid(row=1, column=1)
email_entry = Entry(window, width=41)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "JesusZ@gmail.com")  # pre-fill email field
password_entry = Entry(window, width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(window, text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(window, text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(window, text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)













window.mainloop()