from flask import Flask
import random

app = Flask(__name__)

# 3) Genera un número aleatorio (0 a 9) una sola vez al arrancar el servidor
SECRET_NUMBER = random.randint(0, 9)


@app.route("/")
def home():
    return (
        '<h1 style="color: black; text-align:center;">Guess a number between 0 and 9</h1>'
        '<p style="text-align:center;">Escribe un número en la URL, por ejemplo: /3</p>'
        # Pon aquí tu imagen luego (puede ser URL o un archivo estático)
        '<div style="text-align:center;"><img src="https://via.placeholder.com/300" width="300"></div>'
    )


# 4) Ruta que detecta el número en la URL y lo compara con el secreto
@app.route("/<int:guess>")
def check_guess(guess: int):
    if guess < SECRET_NUMBER:
        return (
            '<h1 style="color: purple; text-align:center;">Too low, try again!</h1>'
            '<div style="text-align:center;"><img src="https://i.pinimg.com/736x/20/00/1e/20001eaddc88c53cc0f5f2d149c39375.jpg" width="300"></div>'
        )
    elif guess > SECRET_NUMBER:
        return (
            '<h1 style="color: red; text-align:center;">Too high, try again!</h1>'
            '<div style="text-align:center;"><img src="https://i.pinimg.com/736x/ef/3c/67/ef3c67f967e2db531984640a0c3161b5.jpg" width="300"></div>'
        )
    else:
        return (
            '<h1 style="color: green; text-align:center;">You found me!</h1>'
            '<div style="text-align:center;"><img src="https://i.pinimg.com/736x/f4/c6/27/f4c627261335050f44778ef550cc9553.jpg" width="300"></div>'
        )


if __name__ == "__main__": #esto lo ejecuta
    app.run(debug=True)
