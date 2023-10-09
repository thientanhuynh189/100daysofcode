from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)


bids = {}
condition = True
while condition:
  name = str(input("What is your name? "))
  price = int(input("What's your bid? $"))
  bids[name] = price

  guess = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if guess == "yes":
    clear()
    condition = True
  elif guess == "no":
    clear()
    condition = False
    highest_name = ""
    highest_bid = 0
    for bidder in bids:
      if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        highest_name = bidder
    print(f"The winner is {highest_name} with a bit of ${highest_bid}")
    # import operator
    # highest_name = max(bids.items(), key=operator.itemgetter(1))[0]
    # highest_bid = max(bids.items(), key=operator.itemgetter(1))[1]
    # print(f"The winner is {highest_name} with a bit of ${highest_bid}")
  else:
    condition = True
    print("Sorry, can't identify")