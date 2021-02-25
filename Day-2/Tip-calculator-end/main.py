print("Welcaome to the tip calculator.")
totalbill = input("What was the total bill? $")
percent_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip = float(totalbill) * int(percent_tip) / 100
tip = int(tip)
people_split = input("How many people to split the bill? ")
split = (float(totalbill) + tip) / int(people_split)
split = round(split,2)
print(f"Each person should pay: ${split}")