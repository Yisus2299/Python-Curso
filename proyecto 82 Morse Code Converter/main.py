# Hoy crearemos un codigo Morse y, principalmente debido a que se trata de un codigo Morse necesitamos los caracteres principales. 
# todas las reglas y en que se basa me guie de este link: https://en.wikipedia.org/wiki/Morse_code

# 1- primero creamos una variable global que podamos usar en todas las funciones y en cualquier ocasion.

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

# 2- creamos la funcion que convierte un caracter a morse

def text_to_morse(text: str) -> str:
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

# 3- creamos la funcion que convierte un texto completo a morse

def main():
    print("=== Conversor a código Morse ===")
    user_text = input("Escribe el texto: ")
    if not user_text.strip():
        print("No ingresaste texto.")
        return
    print("\nMorse:")
    print(text_to_morse(user_text))

# 4- creamos la interfaz por consola:

if __name__ == "__main__":
    texto = input("Escribe el texto a convertir: ")
    resultado = text_to_morse(texto)
    print(resultado)

# si ejecutamos y probamos colocando por ejemplo "Hello World" la respuesta esperada deberia de ser algo como: .... . .-.. .-.. --- / .-- --- .-. .-.. -.. 