print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
total_float = float(total)
tip = input("What percentage tip would you l ike to give? 10, 12, or 15? ")
total_float += total_float * (int(tip) / 100)
people = input("How many people to split the bill? ")
price = round(total_float / int(people), 2)
print(f"Each person should pay: ${price}")