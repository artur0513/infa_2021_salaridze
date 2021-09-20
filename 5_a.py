import turtle

turtle.shape('turtle')
turtle.speed(10)

n = 1000
k = 0.002
step = 2

for i in range(n):
    turtle.right(step)
    turtle.forward(k*i)

turtle.done()