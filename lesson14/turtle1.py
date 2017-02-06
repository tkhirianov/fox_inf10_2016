from turtle import *

def main():
    init_turtle()
    for i in range(10):
        L = i*10
        forward(L+10)
        star(L)
    hideturtle()

def init_turtle():
    shapesize(2)
    shape('turtle')
    color('darkgreen', 'yellow')
    speed(100)

def square(length):
    begin_fill()
    for edge in range(4):
        forward(length)
        right(90)
    end_fill()

def star(length):
    begin_fill()
    for edge in range(5):
        forward(length)
        right(720/5)
    end_fill()

main()
