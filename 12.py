import turtle

turtle.shape('turtle')
turtle.speed(10)


def zvezda(n):
    for i in range(n):
        turtle.forward(100)
        turtle.right(180 - 180 / n)


turtle.penup()
turtle.setpos(-100, 0)
turtle.pendown()
zvezda(5)

turtle.penup()
turtle.setpos(100, 0)
turtle.pendown()
zvezda(11)

turtle.penup()
turtle.setpos(100, 200)
turtle.pendown()
zvezda(7)

turtle.penup()
turtle.setpos(-100, 200)
turtle.pendown()
zvezda(9)

turtle.done()