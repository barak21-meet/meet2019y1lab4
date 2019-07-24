import turtle

t=turtle.Turtle()

t1=turtle.Turtle()

t2=turtle.Turtle()


def up():
    turtle.left(90)
    turtle.forward(50)

def down():
    turtle.left(90)
    turtle.backward(50)

def left():
    turtle.forward(50)

def right():
    turtle.backward(50)

turtle.onkeypress(up, "W")
turtle.onkeypress(down, "s")
turtle.onkeypress(left, "a")
turtle.onkeypress(right, "d")

turtle.listen()

turtle.mainloop()
