from tkinter import *
from pathlib import Path
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
BASE_DIR = Path(__file__).parent

WORDS_TO_LEARN_PATH = BASE_DIR / "data" / "words_to_learn.csv"
ORIGINAL_WORDS_PATH = BASE_DIR / "data" / "french_words.csv"

# Cargar progreso
try:
    data = pandas.read_csv(WORDS_TO_LEARN_PATH)
except FileNotFoundError:
    data = pandas.read_csv(ORIGINAL_WORDS_PATH)
except pandas.errors.EmptyDataError:
    data = pandas.read_csv(ORIGINAL_WORDS_PATH)
else:
    # Validar que tenga las columnas esperadas; si no, usar original
    expected_columns = {"French", "English"}
    if not expected_columns.issubset(set(data.columns)):
        data = pandas.read_csv(ORIGINAL_WORDS_PATH)

to_learn = data.to_dict(orient="records")

current_card = {}
flip_timer = None


def next_card():
    global current_card, flip_timer

    # Cancelar timer anterior para evitar flips acumulados
    if flip_timer is not None:
        window.after_cancel(flip_timer)

    # Si no hay más palabras, mostrar mensaje final
    if not to_learn:
        canvas.itemconfig(card_background, image=card_front_img)
        canvas.itemconfig(card_title, text="Completado", fill="black")
        canvas.itemconfig(card_word, text="¡Ya aprendiste todas!", fill="black")
        return

    current_card = random.choice(to_learn)

    # Mostrar frente de la tarjeta (francés)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    # Programar volteo
    flip_timer = window.after(2000, flip_card)


def flip_card():
    # Mostrar reverso (inglés)
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    # Si la conoces, se elimina de la lista, se guarda progreso y pasa a la siguiente
    if current_card in to_learn:
        to_learn.remove(current_card)
        pandas.DataFrame(to_learn).to_csv(WORDS_TO_LEARN_PATH, index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=str(BASE_DIR / "images" / "card_front.png"))
card_back_img = PhotoImage(file=str(BASE_DIR / "images" / "card_back.png"))

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file=str(BASE_DIR / "images" / "wrong.png"))
unknown_button = Button(image=cross_image, highlightthickness=0, bd=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file=str(BASE_DIR / "images" / "right.png"))
known_button = Button(image=check_image, highlightthickness=0, bd=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()