alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(direct, message, shift_amount):
  end_text = ""
  default_shift = shift_amount
  for letter in message:
    position = alphabet.index(letter)
    if direct == "decode":
      shift_amount *= -1
    new_position = position + shift_amount
    if new_position > len(alphabet):
      new_position -= len(alphabet)
    elif new_position < 0:
      new_position += len(alphabet)
    end_text += alphabet[new_position]
    shift_amount = default_shift
  print(f"The {direct}d text is {end_text}")
  
ceasar(direct=direction,message=text,shift_amount=shift)