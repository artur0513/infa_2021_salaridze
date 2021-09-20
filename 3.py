import turtle

turtle.speed(10)

def square(n):
    turtle.penup()#идем в начало квадрата
    turtle.right(90)
    turtle.forward(n/2)
    turtle.right(90)
    turtle.forward(n / 2)
    turtle.right(180)
    turtle.pendown()

    turtle.forward(n)#рисуем квадрат
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)

    turtle.penup()#возвращаемся в центр экрана
    turtle.left(90)
    turtle.forward(n/2)
    turtle.left(90)
    turtle.forward(n / 2)
    turtle.pendown()


turtle.shape('turtle')
n = 10
k = 30
for i in range(n):
    square((i+1)*k)
turtle.done()