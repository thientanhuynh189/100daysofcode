import turtle
import random

turtle_go = turtle.Turtle()

# turtle_go.forward(100)

# for _ in range(4):
#     turtle_go.forward(100)
#     turtle_go.left(90)

# for _ in range(10):
#     turtle_go.forward(10)
#     turtle_go.penup()
#     turtle_go.forward(10)
#     turtle_go.pendown()

# def draw_shape(edge_number):
#     angle = 360 / edge_number
#     for _ in range(edge_number):
#         turtle_go.forward(50)
#         turtle_go.right(angle)
# for loop in range(3, 10):
#     draw_shape(edge_number=loop)

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# turtle_go.pensize(15)
# turtle_go.speed("fastest")
# for _ in range(200):
#     turtle_go.color(random.choice(colours))
#     turtle_go.forward(30)
#     turtle_go.setheading((random.choice(directions)))

# turtle.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
# direction = [0, 90, 180, 270]
# turtle_go.pensize(15)
# turtle_go.speed("fastest")
# for _ in range(200):
#     turtle_go.color(random_color())
#     turtle_go.forward(30)
#     turtle_go.setheading(random.choice(direction))

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


turtle_go.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle_go.color(random_color())
        turtle_go.circle(100)
        current_heading = turtle_go.heading()
        turtle_go.setheading(current_heading + size_of_gap)


draw_spirograph(5)

screen_show = turtle.Screen()
screen_show.exitonclick()
