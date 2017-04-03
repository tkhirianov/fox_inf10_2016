from turtle import *

def main():
    init()
    #koh_snowflake()
    for x, col in enumerate(('red', 'green', 'blue', 'cyan', 'lightgreen',
                              'brown', 'magenta', 'black', 'gray')):
        init()
        color(col)
        dragon_curve(200, x+1)


def levi_curve(L, depth):
    if depth == 0:
        forward(L)
    else:
        left(45)
        levi_curve(L/2**0.5, depth-1)
        right(90)
        levi_curve(L/2**0.5, depth-1)
        left(45)


def dragon_curve(L, depth, sign=1):
    if depth == 0:
        forward(L)
    else:
        left(45*sign)
        dragon_curve(L/2**0.5, depth-1, +1)
        right(90*sign)
        dragon_curve(L/2**0.5, depth-1, -1)
        left(45*sign)


def init():
    speed(100)
    color('black', 'cyan')
    width(3)
    penup()
    goto(0, 0)
    pendown()
    #clear()


def koh_curve(L):
    if L <= 10:
        forward(L)
    else:
        koh_curve(L/3)

        left(60)
        koh_curve(L/3)
        right(120)
        koh_curve(L/3)
        left(60)
        
        koh_curve(L/3)

def koh_snowflake():
    begin_fill()
    for edge in range(3):
        koh_curve(300)
        right(120)
    end_fill()

if __name__ == '__main__':
    main()
