def prime_checker(number):
  prime_number = [2, 3, 5]
  if number not in prime_number and number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
    print("It's not a prime number.")
  else:
    print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)