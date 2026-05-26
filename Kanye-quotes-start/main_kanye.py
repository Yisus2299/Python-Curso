
from tkinter import *
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)



window = Tk()
window.title("Kanye Says...")
window.config(padx=70, pady=30)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=str(BASE_DIR / "background.png"))
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=str(BASE_DIR / "kanye.png"))
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()