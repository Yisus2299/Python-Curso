alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_letter):
    cipher_text = ""

    for letter in original_text:
       shifted_position = alphabet.index(letter) + shift_letter # 7 -> 9


       shifted_position %= len(alphabet) #0-25
       cipher_text += alphabet[shifted_position] # j

    print(f"Here is the encoded result: {cipher_text}")

# part 2 we create the caesar function


def caesar(original_text, shift_letter, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_letter *= -1

    for letter in original_text:

            if letter not in alphabet:
                output_text += letter
            else:

                shifted_position = alphabet.index(letter) + shift_letter 
                shifted_position %= len(alphabet) 
                output_text += alphabet[shifted_position]  
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    restart= input("Type 'Yes' if you want to do it again. Otherwise, type 'No',\n ").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye.")
    
    caesar(original_text = text, shift_letter = shift, encode_or_decode = direction)













