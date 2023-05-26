# import colorgram
import random
import turtle as t
# colour = colorgram.extract('image.jpeg',30)
#
# rgb_colour = []
# for c in colour:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     new_colour = (r, g, b)
#     rgb_colour.append(new_colour)
# print(rgb_colour)
tim = t.Turtle()
t.colormode(255)
colour_list = [(239, 242, 241), (231, 237, 243), (174, 79, 33), (241, 224, 78), (245, 236, 240), (48, 36, 27), (214, 152, 83), (142, 29, 42), (22, 24, 66), (44, 44, 117), (166, 22, 16), (51, 86, 154), (208, 87, 128), (152, 52, 85), (126, 161, 217), (140, 181, 138), (26, 44, 29), (211, 81, 65), (116, 109, 199), (61, 31, 36), (79, 116, 59), (197, 129, 158), (82, 89, 32), (160, 177, 229), (154, 211, 191), (80, 148, 115), (61, 146, 169), (198, 136, 50), (56, 101, 21)]
tim.speed('fastest')
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_of_dot = 100
for dot_count in range(1, num_of_dot + 1):
    tim.dot(20,random.choice(colour_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
