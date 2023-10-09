############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
from replit import clear
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  return sum(cards)

  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

def play_game():
  print(logo)
  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"\tYour cards: {user_cards}, current score: {user_score}")
    print(f"\tComputer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, ype 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.apeend(deal_card())
      else:
        is_game_over = True

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"\tYour final hand: {user_cards}, final score: {user_score}")
  print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjacck? Type'y' or 'n': ") == 'y':
  clear()
  play_game()

#################

from art import logo
import random
from replit import clear

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_blackjack(list_card):
  scores = 0
  result = False
  for l_card in list_card:
    scores += l_card
  if scores == 22 or scores == 21:
    result = True
  return result

def computer(list_card):
  card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  total_scores = 0
  for l_card in list_card:
    total_scores += l_card
  if len(list_card) >= 4:
    for l_card, pos in list_card:
      if l_card == 11:
        list_card[pos] = 1
  if total_scores <= 17:
    list_card.append(random.choice(card))
  return list_card

def play(list_user_card, list_dealer_card):
  clear()
  card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  if len(list_user_card) and len(list_dealer_card) == 2:
      check_blackjack(list_user_card)
      check_blackjack(list_dealer_card)
      if check_blackjack(list_user_card) and check_blackjack(list_dealer_card) == True:
          print("Draw")
      elif check_blackjack(list_user_card):
        print("You have BlackJack. You win.")
      elif check_blackjack(list_dealer_card):
        print("Dealer have BlackJack. You lose.")
  if len(list_user_card) >= 4:
    for l_card, pos in list_user_card:
      if l_card == 11:
        list_user_card[pos] = 1
      
  score_user = 0
  for lcard in list_user_card:
    score_user += lcard
  if score_user > 21 and len(list_user_card) == 3:
    for l_card, pos in list_user_card:
      if l_card == 11:
        list_user_card[pos] = 1
  
  list_d_card = computer(list_card=list_dealer_card)
  score_dealer = 0
  for lcard in list_d_card:
    score_dealer += lcard

  print(f"\tYour cards: {list_user_card}, current score: {score_user}\n\tComputer's first card: {list_dealer_card[0]}")

  if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
    list_user_card.append(random.choice(card))
    user_card = list_user_card
    dealer_card = list_d_card
    play(list_user_card=user_card, list_dealer_card=dealer_card)
  else:
    print(f"\tYour final hand: {list_user_card}, final score: {score_user}")
    print(f"\tDealer final hand: {list_d_card}, final score: {score_dealer}")
    if score_user == score_dealer:
        print("Draw")
    elif score_user > score_dealer and score_user <= 21:
        print("You win")
    elif score_user <= 21 and score_dealer > 21:
        print("You win")
    elif score_user > 21:
        print("Bust. You lose")
    else:
        print("You lose")
  welcome()

def welcome():
  card_user = []
  card_dealer = []
  for rang in range(0, 2):
    card_user.append(random.choice(card))
    card_dealer.append(random.choice(card))
  question_1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") 
  if question_1 == "y":
    clear()
    print(logo)
    play(list_user_card=card_user, list_dealer_card=card_dealer)

welcome()