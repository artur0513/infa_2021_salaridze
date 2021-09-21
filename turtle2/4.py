# Exercise 4

import turtle
import math

turtle.shape('turtle')
turtle.speed(10)

x = 0
y = 1
Vy = 20
Vx = 5
dt = 0.05
ay = -2

for i in range(1500):
    x += Vx * dt
    y += Vy * dt + ay * dt ** 2 / 2
    Vy += ay * dt

    if y < 0:
        Vy = -Vy * 0.7

    turtle.goto(x, y)
turtle.done()
