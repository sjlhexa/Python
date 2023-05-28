from snake import Snake
import turtle as t
import time

screen = t.Screen()
screen.setup(width=1280, height=720)
screen.bgcolor("black")
screen.title('My Snack game')
screen.tracer(0)

segments = []


snake = Snake()
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


screen.exitonclick()


