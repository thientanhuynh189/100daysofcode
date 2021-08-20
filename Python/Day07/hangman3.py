#Step 3

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f"Psst, the solution is {chosen_word}")

#Create blanks
display = []
for length in range(word_length):
  display += "_"
  
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks("_"). Then you can tell the user they've won.
for pos in range(word_length):
  while display[pos] == "_":
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = guess
    print(display)
    if display[pos] != "_":
      print("You win.")