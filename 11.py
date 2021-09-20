import turtle

turtle.shape('turtle')
turtle.speed(10)

turtle.begin_fill()
turtle.circle(100)
turtle.color("yellow")
turtle.end_fill()

turtle.penup()
turtle.setpos(-40, 130)
turtle.pendown()

turtle.color("black")
turtle.begin_fill()
turtle.circle(20)
turtle.color("blue")
turtle.end_fill()

turtle.penup()
turtle.setpos(40, 130)
turtle.pendown()

turtle.color("black")
turtle.begin_fill()
turtle.circle(20)
turtle.color("blue")
turtle.end_fill()

turtle.width(10)
turtle.penup()
turtle.setpos(0, 100)
turtle.pendown()
turtle.right(90)
turtle.forward(20)

turtle.penup()
turtle.setpos(-30, 60)
turtle.pendown()
turtle.color("red")
turtle.circle(30, 180)
turtle.done()