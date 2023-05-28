import turtle as t
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0







move_dis = 20
starting_position = [(0,0), (-20,0), (-40,0)]


class Snake:
    def __init__(self):
       self.segments = []
       self.create_snake()
       self.head = self.segments[0]


    def create_snake(self,): #creating the snake
       for i in starting_position:
            tim= t.Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(i)
            
            self.segments.append(tim)


    def move(self): # moving the snake
        for seg in range(len(self.segments) -1,0,-1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(move_dis)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)




    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)



    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


