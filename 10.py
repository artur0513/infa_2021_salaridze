import turtle

turtle.shape('turtle')
turtle.speed(10)
turtle.right(90)

n = 6
r1 = 50
r2 = 10

for i in range(n):
    turtle.circle(r1, -180)
    turtle.circle(r2, -180)
turtle.circle(r1, -180)
turtle.done()