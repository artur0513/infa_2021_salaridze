#Exercise 8 - square "spiral"

import turtle

turtle.shape('turtle')
turtle.speed(10)

n = 20 # число квадратов
k = 15 # шаг
m = 15 # начальная длина стороны

for i in range(n):
    turtle.forward(m+k*i)
    turtle.left(90)
    turtle.forward(m+k*i)
    turtle.left(90)

turtle.done()
