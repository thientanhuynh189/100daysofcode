from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1.0, 5.0)
        self.penup()
        self.setpos(x_pos, y_pos)
        self.setheading(90)

    def go_up(self):
        y_new = self.ycor() + 20
        if self.ycor() < 250:
            self.goto(x=self.xcor(), y=int(y_new))

    def go_down(self):
        y_new = self.ycor() - 20
        if self.ycor() > -230:
            self.goto(x=self.xcor(), y=int(y_new))