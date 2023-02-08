def paint_calc(height, width, cover):
  if (height * width) % cover == 0:
    number_of_cans = (height * width) / cover
  else:
    number_of_cans = (height * width) // cover + 1

  print(f"You'll need {round(number_of_cans)} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
