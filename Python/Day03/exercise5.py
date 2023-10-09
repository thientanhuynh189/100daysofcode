print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_name = name1 + name2
name_lower = combine_name.lower()

count_true = name_lower.count('t') + name_lower.count('r') + name_lower.count('u') + name_lower.count('e')

count_love = name_lower.count('l') + name_lower.count('o') + name_lower.count('v') + name_lower.count('e')

TrueLove = str(count_true) + str(count_love)

if int(TrueLove) < 10 or int(TrueLove) > 90:
  print(f"Your score is {TrueLove}, you go together like coke and mentos")
elif int(TrueLove) >= 40 and int(TrueLove) <= 50:
  print(f"Your score is {TrueLove}, you are alright together.")
else:
  print(f"Your score is {TrueLove}")