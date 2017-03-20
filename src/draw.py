import turtle


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


# shankar = turtle.Turtle()
# square(shankar, 200)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


eagle = turtle.Turtle()
polygon(eagle, 8, 50)

turtle.mainloop()
