from turtle import Turtle
from food import Food

a ="center"
f = ("Arial",24,"normal")






class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,320)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=a, font=f)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER" , align=a, font=f)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()