from src.functions_and_karel.caesar import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(art.logo)


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        current_index = alphabet.index(letter)
        new_position = current_index + shift_amount
        if new_position >= len(alphabet):
            cipher_text += alphabet[new_position - current_index - 1]
        else:
            cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")


def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        current_index = alphabet.index(letter)
        new_position = current_index - shift_amount
        if new_position < 0:
            cipher_text += alphabet[new_position + current_index]
        else:
            cipher_text += alphabet[new_position]
    print(f"The decoded text is {cipher_text}")

run = True

while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction.lower() == "encode":
        encrypt(text, shift)
    elif direction.lower() == "decode":
        decrypt(text, shift)

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if not again == "yes":
        run = False
        print("Thank you for using encryptor! Bye!!")
