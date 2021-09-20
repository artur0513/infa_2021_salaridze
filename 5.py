import turtle
import math

turtle.shape('turtle')
turtle.speed(10)
n = 2000
k = 0.1

for i in range(n):
    c = math.cos(i*math.pi/180)
    s = math.sin(i*math.pi/180)
    turtle.setpos(k*i*c, k*i*s)

turtle.done()