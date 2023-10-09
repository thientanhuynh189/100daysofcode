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