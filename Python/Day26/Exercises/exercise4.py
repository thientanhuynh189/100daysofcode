sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
list_str = sentence.split()
result = {string: len(string) for string in list_str}

print(result)

