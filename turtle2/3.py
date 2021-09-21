# Exercise 3

import turtle
import math

turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)


def draw_line(direct, k=1, pd=1):
    length = 50
    if direct == 1:
        turtle.pen(pendown=pd)
        turtle.forward(length * k)
        turtle.pendown()

    if direct == 3:
        turtle.pen(pendown=pd)
        turtle.right(90)
        turtle.forward(length * k)
        turtle.left(90)
        turtle.pendown()

    if direct == 2:
        turtle.pen(pendown=pd)
        turtle.right(45)
        turtle.forward(length * k * math.sqrt(2))
        turtle.left(45)
        turtle.pendown()


def draw_number(n):
    for i in range(len(n)):
        draw_line(n[i][0], n[i][1], n[i][2])


n = []
alln = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
file = open('file_for_3.txt', 'r')
for j in range(10):
    s = file.readline()
    s = s.split()

    for i in range(len(s)):
        s[i] = int(s[i])

    for i in range(round(len(s) / 3)):
        b = [0, 0, 0]
        b[0] = s[i * 3 + 0]
        b[1] = s[i * 3 + 1]
        b[2] = s[i * 3 + 2]
        n.append(b)

    alln[j] = n.copy()
    n.clear()

draw_number(alln[1])
draw_number(alln[4])
draw_number(alln[1])
draw_number(alln[7])
draw_number(alln[0])
draw_number(alln[0])


turtle.done()
