"""EX04 - A mountain landscape."""

__author__ = "730478127"

from turtle import Turtle, done 
import turtle
from random import randint
bert: Turtle = Turtle()
bert.speed(10)
screen = turtle.Screen()
screen.bgcolor("#87CEFA")
    

def main() -> None: 
    """The entrypoint of my scene."""
    draw_sun(bert, 0, 200)
    draw_birds(bert, randint(-200, 200), randint(250, 275))
    draw_birds(bert, randint(-200, 200), randint(250, 275))
    draw_big_mountain(bert, -500, -320)
    draw_small_mountain(bert, -550, -320)
    draw_grass(bert, -360, -320)
    done() 


def draw_small_mountain(bert: Turtle, x: float, y: float) -> None: 
    """Draw multiple short mountains going across the bottom of the screen."""
    bert.penup()
    bert.goto(x, y)
    bert.color("grey")
    bert.pendown()
    i: int = 0
    while i < 4:
        bert.setheading(0.0)
        bert.begin_fill()
        bert.left(45)
        bert.forward(300)
        bert.right(90)
        bert.forward(300)
        bert.right(135)
        bert.end_fill()
        bert.penup()
        bert.forward(200)
        bert.pendown() 
        i += 1 


def draw_big_mountain(bert: Turtle, x: float, y: float) -> None: 
    """Draw multiple tall mountains going behind the shorter mountains."""
    bert.penup()
    bert.goto(x, y)
    bert.color("maroon")
    bert.pendown()
    i: int = 0
    while i < 5:
        bert.setheading(0.0)
        bert.begin_fill()
        bert.left(75)
        bert.forward(500)
        bert.right(150)
        bert.forward(500)
        bert.setheading(0.0)
        bert.left(180)
        bert.end_fill()
        bert.penup()
        bert.forward(80)
        bert.pendown() 
        i += 1


def draw_sun(bert: Turtle, x: float, y: float) -> None: 
    """Draw a sun in the center behind the mountains."""
    bert.penup()
    bert.goto(x, y)
    bert.color("yellow")
    bert.pendown()
    bert.begin_fill()
    bert.circle(50) 
    bert.end_fill()


def draw_birds(bert: Turtle, x: float, y: float) -> None:
    """Draws birds in random spots in the sky."""
    bert.setheading(90.0)
    bert.penup()
    bert.goto(x, y)
    bert.color("#000080")
    bert.pensize(5)
    bert.pendown()
    bert.circle(10, 180)
    bert.setheading(90.0)
    bert.circle(10, 180) 


def draw_triangle(bert: Turtle, side: int) -> None: 
    """Draws a triangle to be later used to draw a tree."""
    bert.begin_fill()
    bert.setheading(0.0)
    bert.forward(side) 
    bert.left(120)
    bert.forward(side)
    bert.left(120)
    bert.forward(side)
    bert.end_fill()
    bert.penup()
    bert.setheading(0.0)
    bert.forward(side)


def draw_grass(bert: Turtle, x: float, y: float) -> None: 
    """Uses a while loop to draw multiple bushes and utilizes the draw_singular_bush function."""
    bert.penup()
    bert.goto(x, y)
    bert.color("green")
    i: int = 0
    while i < 30:
        bert.pendown()
        draw_triangle(bert, 30)
        bert.penup() 
        bert.forward(5) 
        i += 1


if __name__ == "__main__":
    main() 