for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    number = "FizzBuzz"
    # print(number)
  elif number % 3 == 0:
    number = "Fizz"
    # print(number)
  elif number % 5 == 0:
    number = "Buzz"
    # print(number)
  print(number)
