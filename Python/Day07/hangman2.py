import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"Psst, the solution is {chosen_word}")

display = []
for letter in chosen_word:
  display.append("_")
  
guess = input("Guess a letter: ").lower()

for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = guess
  else:
    display[position] = "_"

print(display)