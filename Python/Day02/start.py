#Data Types
#String
# "Hello"

#Integer
# 123 + 345

#Float
# 3.14592

#Boolean
# True
# False

#TypeError: object of type 'int' has no len()
# print(len(23))
#Check type: type()

#Change type: str(), float()
num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("You have " + new_num_char + " characters")

#PEMDAS
#Parentheses: ()
#Exponents: **
#Multiplication: *
#Division: /
#Addition: +
#Subtraction: -

print(3 * 3 / 3 + 3 - 3)
#print(3 * (3 + 3) / 3 - 3)

#round() >< int()
print(round(8/3,2))

score = 0
height = 1.8
isWinning = True
#f-String
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")