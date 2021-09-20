import turtle
turtle.shape('turtle')
turtle.speed(10)
n = 20
for i in range(n):
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.left(360/n)

turtle.done()