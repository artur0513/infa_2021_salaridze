# Exercise 1

import turtle
import random as rnd

turtle.shape('turtle')
turtle.speed(10)

n = 100
max_step = 50

for i in range(n):
    turtle.right(rnd.randint(-180, 179))
    turtle.forward(rnd.randint(0, max_step))

turtle.done()
