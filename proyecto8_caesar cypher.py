alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(texto_original, shift_cambio):
    cipher_text = ""

    for letra in texto_original:
       shifted_position = alfabeto.index(letra) + shift_cambio # 7 -> 9


       shifted_position %= len(alfabeto) #0-25
       cipher_text += alfabeto[shifted_position] # j

    print(f"Aquí está el resultado encodeado: {cipher_text}")

#parte 2 creamos la funcion de caesar


def caesar(texto_original, shift_cambio, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_cambio *= -1

    for letra in texto_original:

            if letra not in alfabeto:
                output_text += letra
            else:

                shifted_position = alfabeto.index(letra) + shift_cambio 
                shifted_position %= len(alfabeto) 
                output_text += alfabeto[shifted_position]  
    print(f"Aquí está el {encode_or_decode}d result: {output_text}")


deberias_continuar = True

while deberias_continuar:

    direccion = input("Escribe 'encode' para encriptar, escribe 'decode' para desencriptar:\n").lower()
    texto = input("Escribe tu mensaje:\n").lower()
    cambio = int(input("Escribe el cambio del número:\n"))

    restart= input("Escribe 'Si' quieres hacerlo otra vez. De otra forma, escribe 'No',\n ").lower()
    if restart == "no":
        deberias_continuar = False
        print("Adios.")
    
    caesar(texto_original = texto, shift_cambio = cambio, encode_or_decode = direccion)













