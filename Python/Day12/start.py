################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope

# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)

# drink_potion()
# print(potion_strength) #Error

# Global Scope
# player_health = 10

# # Global function
# def game():
#   # Local function
#   def drink_potion():
#     postion_strength = 2
#     print(player_health)

#   drink_potion()

# print(player_health)

# There is no Block Scope
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#   new_enemy = enemies[0]

# print(new_enemy)

#There is Block Scope
# game_level = 3
# def create_enemy():
#   enemies = ["Skeleton", "Zombie", "Alien"]
#   if game_level < 5:
#     new_enemy = enemies[0]

#   print(new_enemy)

#Modifying Global Scope

# enemies = 1

# def increase_enemies():
#   global enemies
#   enemies += 1
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")
# #and
# enemies = 1

# def increase_enemies():
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

#Global Constants

pi = 1.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

