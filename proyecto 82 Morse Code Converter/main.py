# This script implements a Morse code converter. The MORSE_CODE mapping
# follows the standard defined on Wikipedia: https://en.wikipedia.org/wiki/Morse_code

# 1- define a global mapping so it can be used by all functions.

MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
    "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.",
    "$": "...-..-", "@": ".--.-.",
}

# 2- function that converts text to Morse code.
def text_to_morse(text: str) -> str:
    """Convert a text string to Morse code.

    Words are separated by a slash (/) and letters by spaces.
    Unknown characters are ignored.
    """
    words = []
    current_word = []
    for char in text:
        if char.isspace():
            if current_word:
                words.append(" ".join(current_word))
                current_word = []
            continue
        code = MORSE_CODE.get(char.upper())
        if code:
            current_word.append(code)
    if current_word:
        words.append(" ".join(current_word))
    return " / ".join(words)


def main():
    print("=== Morse Code Converter ===")
    user_text = input("Enter text: ")
    if not user_text.strip():
        print("No text entered.")
        return
    print("\nMorse:")
    print(text_to_morse(user_text))

# 4- creamos la interfaz por consola:

if __name__ == "__main__":
    main()

# si ejecutamos y probamos colocando por ejemplo "Hello World" la respuesta esperada deberia de ser algo como: .... . .-.. .-.. --- / .-- --- .-. .-.. -.. 