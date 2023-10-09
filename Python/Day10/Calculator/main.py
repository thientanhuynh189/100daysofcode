from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2 #minus

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return float(n1 / n2)

operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))

  condition = True
  while condition:
    num2 = float(input("What's the next number?: "))
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    calculation_function = operations[operation_symbol]
    if operation_symbol in operations:
      answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    question = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. Top of that, type 'e' to exit.: ")
    if question.lower() == 'y':
      num1 = answer
    elif question.lower() == 'n':
      condition = False
      calculation()
    elif question.lower() == 'e':
      condition = False
    else:
      print("Unvalid number.")
      condition = False

calculator()