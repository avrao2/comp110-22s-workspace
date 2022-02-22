from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
leo.penup()
leo.goto(0, 0)
leo.pendown()

i: int = 0
while (i<3):
    leo.forward(300)
    leo.left(120)
    i = i+1
