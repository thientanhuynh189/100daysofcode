#Step 1

word_list = ["ardwark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word
import random

chosen_word = word_list[random.randint(0, len(word_list) - 1)] #random.choice(word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user_guess = input("Give me 1 letter, please: ").lower()
# user_guess.lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters is the chosen_word
for letter in chosen_word:
  if user_guess == letter:
    print("Right")
  else:
    print("Wrong")