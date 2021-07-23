# # import random
# from art import logo

# #Choosing a random number between 1 and 100.
# from random import randint
# number = randint(1,100)

# def play(live):
#   global number
#   print(f"You have {live} attempts remaining to guess the number.")

# def check_number(number_check):
#   global number
#   if number_check > number:
#     print("Too high")
#   elif number_check < number:
#     print("Too low")
#   else:
#     print("Bingo. That's correct number") 


# def program():
#   print("I'm thinking of a number between 1 and 100.")
#   if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy':
#     lives = 10
#     while lives != 0:
#       play(live=lives)
#       #Let the user guess a number.
#       guess = int(input("Make a guess: "))
#       check_number(number_check=guess)
#       lives -= 1
#   else:
#     lives = 5
#     while lives != 0:
#       play(live=lives)
#       #Let the user guess a number.
#       guess = int(input("Make a guess: "))
#       check_number(number_check=guess)
#       lives -= 1

# print(logo)
# program()
# print(f"The correct number is: {number}")

########################
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """Check answer against guess."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! the answer was {answer}.")

#Make function to set difficultydef set_difficulty():
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)

  turns = set_difficulty()

  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    #Let the user guess a number.
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

#Track the number of turns and reduce by 1 if they get it wrong.

game()