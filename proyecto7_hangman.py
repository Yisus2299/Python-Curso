import random

list = ["isis", "ryo", "selene", "nana"]

choosen_word = random.choice(list)

lives = 6
letras_correctas = []

print("Welcome to the hangman game.")

placeholder = ""
for _ in range(len(choosen_word)):
    placeholder += "_"
print("Word:", placeholder)

game_over = False

while not game_over:
    print(f"You have {lives} lives left.")

    adivinar = input("Guess a letter: ").lower()

    if adivinar in letras_correctas:
        print("You already guessed that letter. Try another one.")
    else:
        if adivinar in choosen_word:
            letras_correctas.append(adivinar)
        else:
            lives -= 1
            print("That letter is not in the word.")

    display = ""
    for letter in choosen_word:
        if letter in letras_correctas:
            display += letter
        else:
            display += "_"

    print("Word:", display)

    if lives == 0:
        game_over = True
        print(f"You lost. The word was: {choosen_word}")

    if "_" not in display:
        game_over = True
        print("You win.")