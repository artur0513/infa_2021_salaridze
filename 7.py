import math
import turtle

turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)


def figure(n, l):
    angle = 180 - 180 * (n - 2) / n
    turtle.left(angle / 2)
    for i in range(n):
        turtle.forward(l)
        turtle.left(angle)
    turtle.right(angle / 2 + 90)


r = 50
c = 10
step = 30
for i in range(3, c):
    l = r * 2 * math.sin(math.pi / i)

    figure(i, l)
    r += step
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()
    turtle.left(90)

turtle.done()
