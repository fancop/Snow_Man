import turtle as t
import random

t.speed(0)
t.colormode(255)
t.ht()

while True:
    # контракт
    x = random.randint(-500, 500)       # выбираем место снеговика по ширине
    y = random.randint(-300, 100)       # выбираем место снеговика по высоте
    circles = random.randint(3, 10)     # выбираем кличество комков
    radius = random.randint(50, 70)     # выбираем радиус первого комкаb
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    t.penup()
    t.goto(x, y)

    for i in range(circles):
        t.pendown()
        t.fillcolor(red, green, blue)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        t.penup()
        t.setheading(90)
        t.fd(radius * 2)
        t.setheading(0)
        radius /= 2           # седующий комок в два раза меньше предыдущего

t.done()