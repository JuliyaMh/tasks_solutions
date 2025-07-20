import turtle

t = turtle.Pen()


def star(n):
    angle = 360 / n / 2
    t.left(angle * 2)
    for i in range(n):
        t.forward(100)
        t.right(180 - angle)
