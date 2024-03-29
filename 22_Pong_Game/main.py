from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() >290 or ball.ycor() < -290:
        ball.bounce_y()


    #detect collison with the peddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
        


    #detect if the ball has missed the paddle

    #right
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    #left
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

      

screen.exitonclick()
