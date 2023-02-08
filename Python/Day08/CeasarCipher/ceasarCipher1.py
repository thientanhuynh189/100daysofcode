alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_text):
  cipher_text = ""

  for letter in plain_text:
    position = alphabet.index(letter)
    cipher_position = position + shift_text
    if cipher_position > len(alphabet):
      cipher_position -= len(alphabet)
    letter = alphabet[cipher_position]
    cipher_text += letter

  print(f"The encoded text is {cipher_text}")

encrypt(plain_text=text,shift_text=shift)