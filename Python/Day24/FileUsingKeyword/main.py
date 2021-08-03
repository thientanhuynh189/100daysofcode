with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("Add new string")

with open("new_file.txt", mode="w") as file:
    file.write("Create a new string")


#direct path
with open("/github/python/my_file.txt") as file:
    file.read()

with open("../../../github/100daysofcode/new_file.txt") as file:
    contents = file.read()
    print(contents)