import turtle

turtle.shape('turtle')
turtle.speed(10)
turtle.right(90)

n = 5
step = 10
r = 50

for i in range(n):
    turtle.circle(r+step*i)
    turtle.circle(-r-step*i)

turtle.done()