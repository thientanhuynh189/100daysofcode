year = int(input("Which year do you want to check?")) #Add integer formatting

if year % 4 == 0:
  if year % 100 != 0: #Replace '!=' for a leap year
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Not leap year.")
else:
  print("Not leap year.")
  