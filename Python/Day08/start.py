# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# def greet():
#   print("Now, give back the code.")
#   print("Say hello")
#   print("To my honour.")

# greet()

#Function that allows for input
# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How do you do {name}?")
# greet_with_name("Angela")

#Functions with more than 1 input
# def greet_answer(name, location):
#   print(f"Hello {name}")
#   print(f"Are you live in {location}?")
# greet_answer("Angela", "California")

#Functions with keyword arguments
name = ""
location = ""
def greet_answer(name, location):
  name += "Angela"
  print(f"Hello {name}")
  location += "California"
  print(f"Are you live in {location}?")
greet_answer(location, name)