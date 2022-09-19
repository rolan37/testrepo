import turtle as bob

bob.bgcolor("red")   # because the space has no color (dark)

# we need to draw the star?

size = 100
points = 5
angle = 180 - (180/points)


for i in range(points):
    bob.forward(size)
    bob.left(angle)
