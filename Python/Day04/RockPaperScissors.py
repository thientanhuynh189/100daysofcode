import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

associated = [rock, paper, scissors]

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choose_parameter = associated[choose]
print(choose_parameter)

print("Computer chose:")
random_number = random.randint(0,2)
random_choose = associated[random_number]
print(random_choose)

if choose == 0 and random_choose == 2:
  print("You win")
elif choose > random_number:
  print("You win")
elif choose == random_number:
  print("Draw.")
elif choose >= 3 or choose < 0:
  print("You typed an invalid number. Try again!")
else:
  print("You lose")