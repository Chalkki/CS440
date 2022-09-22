# please use python3
# see instructions here (https://resources.cs.rutgers.edu/docs/using-python-on-cs-linux-machines/)

from tkinter import UNITS
import turtle
import unittest


def draw(grid, node_dict, startP, goalP, row, col, path):

    unit = 10  #change to change size
    kameP = turtle.Turtle()  #turtle to draw
    screen = turtle.Screen()

    def get_mouse_click_coor(x, y):
        if unit>x or x>(col+1)*unit or unit>y or y>(row+1)*unit:
            return
        else:
            x//=unit
            y//=unit
        screen.title("Grid({X},{Y})".format(X="{:.0f}".format(x), Y="{:.0f}".format(y)))

    def square(isblock):
        if isblock:
            kameP.color("grey")
            kameP.begin_fill()
        for i in range(4):
            kameP.forward(unit)
            kameP.right(90)
        if isblock:
            kameP.end_fill()
            kameP.color("black")

    def walk():
        if path==None: return
        for i in path:
            kameP.setposition(i[0]*unit, i[1]*unit)

    #set up
    screen.setup(col*unit,row*unit)
    screen.setworldcoordinates(unit, ((row+1)*unit), (col+1)*unit, unit)  #enable our coordinate system
    turtle.tracer(0, 0)  # to skip animation
    kameP.penup()
    kameP.setposition(unit,unit)
    kameP.pendown()
    kameP.left(90)

    for i in range(col):
        for j in range(row):
            x = i + 1
            y = j + 1
            isblocked = grid[str(x)+"/"+str(y)].isblocked
            print(isblocked)
            square(isblocked)
            kameP.forward(unit)
        kameP.penup()
        kameP.left(180)
        kameP.forward(row * unit)
        kameP.left(90)
        kameP.forward(-unit)
        kameP.left(90)
        kameP.pendown()

    # stamps an arrow in start point, a turtle in goal
    kameP.penup()
    kameP.color("green")
    kameP.setposition(startP[0]*unit, startP[1]*unit)
    kameP.stamp()
    kameP.color("red")
    kameP.setposition(goalP[0]*unit, goalP[1]*unit)
    kameP.stamp()

    kameP.pendown()
    walk()
    kameP.hideturtle()

    turtle.update()

    turtle.onscreenclick(get_mouse_click_coor)
    turtle.mainloop()

