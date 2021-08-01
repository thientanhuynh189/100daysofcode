import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

#create the screen
screen = Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")

#create and move a paddle
#create another paddles
r_paddle = Paddle(x_pos=350, y_pos=0)
l_paddle = Paddle(x_pos=-350, y_pos=0)

#move a paddle
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

#create the ball and make it move
ball = Ball()
#keep score
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    #make the ball moves
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 270 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # detect when paddle misses
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_point()

screen.exitonclick()