from snake import Snake
import turtle as t
import time
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=1280, height=720)
screen.bgcolor("black")
screen.title('My Snack game')
screen.tracer(0)

segments = []


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# moving the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #detect collision with wall.
    if snake.head.xcor() > 630 or snake.head.xcor() < -630 or snake.head.ycor() > 360 or snake.head.ycor() < -360:
        game_is_on = False
        scoreboard.game_over()



    #detect Head and Tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()


