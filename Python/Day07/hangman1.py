word_list = ["ardwark", "baboon", "camel"]

import random

chosen_word = word_list[random.randint(0, len(word_list) - 1)] #random.choice(word_list)
print(chosen_word)

user_guess = input("Give me 1 letter, please: ").lower()

for letter in chosen_word:
  if user_guess == letter:
    print("Right")
  else:
    print("Wrong")