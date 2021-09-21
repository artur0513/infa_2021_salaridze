#Exercise 10 - flowers

import turtle

turtle.shape('turtle')
turtle.speed(10)

n = 3
for i in range(n):
    turtle.circle(50)
    turtle.circle(-50)
    turtle.right(180/n)

turtle.done()
