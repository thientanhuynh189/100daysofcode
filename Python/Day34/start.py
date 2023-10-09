# age : int
# # age = "Between" #Expected type 'int', got 'str' instead
# age = 12

# def police_check(age):
#     if age > 18:
#         can_drive = True
#     else:
#         can_drive = False
#     return can_drive
#
# # if police_check("twelve") #'>' not supported between instances of 'str' and 'int'
# if police_check(19):
#     print("You may pass")
# else:
#     print("Pay a fine.")

# def police_check(age: int) -> bool:
#     if age > 18:
#         can_drive = True
#     else:
#         can_drive = False
#     return "They can drive"

#Type Hints
#def greeting(name: str) -> str:
#   return 'Hello ' + name