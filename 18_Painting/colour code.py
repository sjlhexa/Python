colour = colorgram.extract('image.jpeg',30) #change the image name

rgb_colour = []
for c in colour:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    new_colour = (r, g, b)
    rgb_colour.append(new_colour)
print(rgb_colour)