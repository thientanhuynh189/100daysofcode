number = int(input("Which number do you want to check? "))

number_devide = number % 2

if number_devide == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")