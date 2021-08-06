#Default argument: turtle.write("Some text", font=..., align=...) -> '...' : optional

# Unlimited Arguments
def add(*args):
    for n in args:
        print(n)

# Many Positional Argument
add(1, 2, 3, 4, 5, 6, 7)

#Unlimited Keyword Arguments
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")

# my_car = Car(make="Nissan", model="GT-R")
my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
