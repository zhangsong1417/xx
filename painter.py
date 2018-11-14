import turtle

painter = turtle.Turtle()
painter.pencolor("blue")

for i in range(50):
    painter.forward(100)
    painter.left(123)

painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)

turtle.done()
