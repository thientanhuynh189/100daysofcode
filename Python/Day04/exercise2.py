import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
end_number = len(names) - 1
number_choice = random.randint(0, end_number)

name_choice = names[number_choice]
# name_choice = random.choice(names)
print(f"{name_choice} is going to buy the meal today!")