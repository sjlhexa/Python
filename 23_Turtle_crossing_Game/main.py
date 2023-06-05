import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(player.go_up, "space")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()


    #collison with car
    for car in car_manager.all_car:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()


    #crossing
    if player.finish():
        player.start()
        scoreboard.level_up()


screen.exitonclick()