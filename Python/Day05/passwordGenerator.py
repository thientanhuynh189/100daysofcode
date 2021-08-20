#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# position = 0
letter = ""
# for choice_letter in letters:
#   if position < nr_letters:
#     position += 1
#     choice_letter = letters[random.randint(0, len(letters) - 1)]
#     letter += choice_letter
# for nr in range(1, nr_letters + 1):
#   letter += random.choice(letters)

# position = 0
symbol = ""
# for choice_symbol in symbols:
#   if position < nr_symbols:
#     position += 1
#     choice_symbol = symbols[random.randint(0, len(symbols) - 1)]
#     symbol += choice_symbol
# for nr in range(1, nr_symbols + 1):
#   symbol += random.choice(symbols)

# position = 0
number = ""
# for choice_number in numbers:
#   if position < nr_numbers:
#     position += 1
#     choice_number = numbers[random.randint(0, len(numbers) - 1)]
#     number += choice_number
# for nr in range(1, nr_numbers + 1):
#   number += random.choice(numbers)

# print(letter + symbol + number)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = []
for nr in range(1, nr_letters + 1):
  password += random.choice(letters)
for nr in range(1, nr_symbols + 1):
  password += random.choice(symbols)
for nr in range(1, nr_numbers + 1):
  password += random.choice(numbers)
random.shuffle(password)
final_password = ""
for pw in password:
  final_password += pw
print(final_password)