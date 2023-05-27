import turtle as t
import random

is_race_on = False
screen = t.Screen()

screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make a bet", prompt="Which Turtle will win the race? Enter a colour")
colours= ["red", "orange","yellow", "green", "blue", "purple"]

y_pos = [-70, -40, -10, 20,50,80]
all_turtle = []


for turtle_index in range(0,6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.color(random.choice(colours))
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You have won")
            else:
                print(f"You have lost, The winner is {winning_colour}")
        dist = random.randint(0,10)
        turtle.forward(dist)



screen.exitonclick()


