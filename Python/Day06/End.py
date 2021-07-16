#5.3 The hurdles loop challenge
#work on: reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def turn_right():
  turn_left() #commands in program
  turn_left()
  turn_left()
def jump():
  move() #commands in program
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()
for step in range(6):
  jump()

#5.6 While loops
#work on: reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def turn_right():
  turn_left() #commands in program
  turn_left()
  turn_left()
def jump():
  move() #commands in program
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()
while not at_goal(): #commands in program
  jump()

#5.7 Hurdles Challenge using While Loops
#work on: reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
def turn_right():
  turn_left() #commands in program
  turn_left()
  turn_left()
def jump():
  turn_left()
  move() #commands in program
  turn_right()
  move()
  turn_right()
  move()
  turn_left()
while not at_goal(): #commands in program
  if front_is_clear(): #commands in program
    move()
  else:
    jump()

#5.8. Jumping over Hurdles with Variable Heights
#work on: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=wolrds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
def check_front():
    if wall_on_right() and wall_in_front():
        turn_left()
    elif right_is_clear() and front_is_clear():
        turn_right()
        move()
    elif wall_in_front() and right_is_clear():
        turn_right()
        move()
    else:
        move()
        
while not at_goal():
    check_front()
#or
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_in_right(): #commands in program
      move()
    turn_right()
    move()
    while front_is_clear():
      move()
    turn_left()
        
while not at_goal():
  if wall_in_front(): #commands in program
    jump()
  else:
    move()

#5.9. Final Project Escaping the Maze
# work on: unknow source
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    while wall_on_right():
        if wall_in_front():
            turn_left()
        move()
    if right_is_clear():
        turn_right()
        move()
#or
def turn_right():
  turn_left()
  turn_left()
  turn_left()
while not at_goal():
  if right_is_clear():
    turn_right()
    move()
  elif front_is_clear():
    move()
  else
    turn_left()