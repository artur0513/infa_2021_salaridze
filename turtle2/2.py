# Exercise 2

import turtle
import math

turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)


#Функция, рисующая линии для цифр:
#Первый аргумент - направление, 1 - вверх, 2 - наискосок вправо вверх, 3 - вправо
#Второй аргумент - длина, если указать -1, то рисуем в другую сторону, для рисования диагонали расстояние умножается на sqrt(2) автоматически
#Третий аргумент - поднятие пера, если 1 - рисуем, если 0 - не рисуем
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


n0 = ((1, -2, 1), (3, 1, 1), (1, 2, 1), (3, -1, 1), (3, 2, 0))
n1 = ((1, -1, 0), (2, 1, 1), (1, -2, 1), (1, 2, 1), (3, 1, 0))
n2 = ((3, 1, 1), (1, -1, 1), (2, -1, 1), (3, 1, 1), (1, 2, 0), (3, 1, 0))
n3 = ((3, 1, 1), (2, -1, 1,), (3, 1, 1), (2, -1, 1,), (1, 2, 0), (3, 2, 0))
n4 = ((1, -1, 1), (3, 1, 1), (1, -1, 1), (1, 2, 1), (3, 1, 0))
n5 = ((1, -1, 1), (3, 1, 1), (1, -1, 1), (3, -1, 1), (1, 2, 0), (3, 1, 1), (3, 1, 0))
n6 = ((1, -1, 0), (1, -1, 1), (3, 1, 1), (1, 1, 1), (3, -1, 1), (2, 1, 1), (3, 1, 0))
n7 = ((3, 1, 1), (2, -1, 1), (1, -1, 1), (1, 2, 0), (3, 2, 0))
n8 = ((1, -2, 1), (3, 1, 1), (1, 2, 1), (3, -1, 1), (1, -1, 1), (3, 1, 1), (1, 1, 1), (3, 1, 0))
n9 = ((3, 1, 1), (1, -1, 1), (2, -1, 1), (2, 1, 1), (3, -1, 1), (1, 1, 1), (3, 2, 0))

draw_number(n1)
draw_number(n4)
draw_number(n1)
draw_number(n7)
draw_number(n0)
draw_number(n0)

turtle.done()
