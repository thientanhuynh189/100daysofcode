print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age >= 45 and age <= 55:
    bill = 0
  elif age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")

  wants_photo = input("Do you want a photo taken? Y or N.")
  if wants_photo == "Y":
    #Add $3 to their bill
    bill += 3
  
  print(f"Your final bill is {bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")

  #Greater than: >
  #Less than: <
  #Greater than or equal to: >=
  #Less than or equal to: <=
  #Equal to: ==
  #Not equal to: !=

