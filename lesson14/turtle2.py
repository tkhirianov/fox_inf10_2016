from turtle import *

def main():
    init_turtle()
    for i in range(3):
        snowy_forward(200)
        right(360/3)
    hideturtle()

def init_turtle():
    shapesize(2)
    shape('turtle')
    color('darkgreen', 'yellow')
    speed(100)

def snowy_forward(L):
    if L <= 10:
        forward(L)
    else:
        snowy_forward(L/3)
        left(60)
        snowy_forward(L/3)
        right(120)
        snowy_forward(L/3)
        left(60)
        snowy_forward(L/3)

main()
