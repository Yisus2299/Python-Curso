import random

lista = ["isis", "ryo", "selene", "nana"]

palabra_elegida = random.choice(lista)

vidas = 6
letras_correctas = []

print("Bienvenido al juego del ahorcado.")

placeholder = ""
for _ in range(len(palabra_elegida)):
    placeholder += "_"
print("Palabra:", placeholder)

game_over = False

while not game_over:
    print(f"Te quedan {vidas} vidas.")

    adivinar = input("Adivina una letra: ").lower()

    if adivinar in letras_correctas:
        print("Ya adivinaste esa letra. Intenta otra.")
    else:
        if adivinar in palabra_elegida:
            letras_correctas.append(adivinar)
        else:
            vidas -= 1
            print("No está esa letra.")

    display = ""
    for letra in palabra_elegida:
        if letra in letras_correctas:
            display += letra
        else:
            display += "_"

    print("Palabra:", display)

    if vidas == 0:
        game_over = True
        print(f"Has perdido. La palabra era: {palabra_elegida}")

    if "_" not in display:
        game_over = True
        print("Tú ganas.")