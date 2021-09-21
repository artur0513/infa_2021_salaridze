# Exercise 5

import random as rnd
import turtle

x = 200
turtle.shape('circle')
turtle.shapesize(0.5)
turtle.speed(0)
turtle.penup()
turtle.goto(-x, -x)
turtle.pendown()
turtle.goto(-x, x)
turtle.goto(x, x)
turtle.goto(x, -x)
turtle.goto(-x, -x)
turtle.hideturtle()

dt = 0.1
number_of_turtles = 10
steps_of_time_number = 1000
max_speed = 50


class Molecule:
    def __init__(self):
        self.cx = rnd.randint(-x, x)
        self.cy = rnd.randint(-x, x)
        self.vx = rnd.randint(-max_speed, max_speed)
        self.vy = rnd.randint(-max_speed, max_speed)
        self.tu = turtle.Turtle()
        self.tu.penup()
        self.tu.shape('circle')
        self.tu.shapesize(0.5)
        self.tu.speed(0)

    def update(self):
        if abs(self.cx) > x:
            self.vx *= -1
        if abs(self.cy) > x:
            self.vy *= -1
        self.cx += self.vx * dt
        self.cy += self.vy * dt
        self.tu.goto(self.cx, self.cy)


molecules = [Molecule() for i in range(number_of_turtles)]
for i in range(steps_of_time_number):
    for j in range(number_of_turtles):
        molecules[j].update()

turtle.done()
