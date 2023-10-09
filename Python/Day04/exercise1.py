import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

output = random.randint(0, 1)

if output == 0:
  print("Tails")
else:
  print("Heads")