from art import logo, vs
import random
from game_data import data
from replit import clear


def random_chosen():
    random_chose = random.randint(0, len(data) - 1)
    return data[random_chose]


def begin_game(dictionary1, dictionary2):
    print(
        f"Compare A: {dictionary1['name']}, a/an {dictionary1['description']}, from {dictionary1['country']}"
    )
    print(vs)
    print(
        f"Against B: {dictionary2['name']}, a/an {dictionary2['description']}, from {dictionary2['country']}"
    )


def check_game(dictionary1, dictionary2):
    if dictionary1['follower_count'] > dictionary2['follower_count']:
        return True
    elif dictionary2['follower_count'] > dictionary2['follower_count']:
        return True
    else:
        return False


def result_game(condition, score):
    if condition:
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")


condition = True
score = 0
check = 0
while condition:
    if check == 0:
        first_person = random_chosen()
        second_person = random_chosen()
    elif check > 0:
        first_person = second_person
        second_person = random_chosen()
    if first_person != second_person:
      clear()
      print(logo)
      if condition == True and score > 0:
          result_game(condition, score)

      begin_game(dictionary1=first_person, dictionary2=second_person)

      question = input("Who has more followers? Type 'A' or 'B': ")
      if question == 'A' or question == 'a':
          check_answer = check_game(dictionary1=first_person,
                                    dictionary2=second_person)
          if check_answer:
              score += 1
              condition = True
              check = 1
          else:
              condition = False
              clear()
              print(logo)
              result_game(condition, score)

      elif question == 'B' or question == 'b':
          check_answer = check_game(dictionary1=first_person,
                                    dictionary2=second_person)
          if check_answer:
              score += 1
              condition = True
              check = 2
          else:
              condition = False
              clear()
              print(logo)
              result_game(condition, score)
    else:
      second_person = random_chosen()
    
