# please use python3
# see instructions here (https://resources.cs.rutgers.edu/docs/using-python-on-cs-linux-machines/)

from tkinter import UNITS
import turtle
import unittest


def draw(fileN, path):

    unit = 10  #change to change size
    kameP = turtle.Turtle()  #turtle to draw
    screen = turtle.Screen()

    def get_mouse_click_coor(x, y):
        if unit>x or x>(row+1)*unit or unit>y or y>(col+1)*unit:
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

    #walk through a list of coornidates
    def walk():
        kameP.color("red")
        if path==None: return
        for i in path:
            kameP.setposition(i[0]*unit,i[1]*unit)

    #read file
    f = open(fileN, 'r')
    startP=f.readline().split()
    goalP=f.readline().split()
    size=f.readline().split()
    row = int(size[0])
    col = int(size[1])

    #set up
    screen.setup(row*unit,col*unit)
    screen.setworldcoordinates(unit, ((col+1)*unit), (row+1)*unit, unit)  #enable our coordinate system
    turtle.tracer(0, 0)  # to skip animation
    kameP.penup()
    kameP.setposition(unit,unit)
    kameP.pendown()
    kameP.left(90)

    #draw grids
    for x in range(row):
        for y in range(col):
            isblocked = True if f.readline().split()[2]=='1' else False
            square(isblocked)
            kameP.forward(unit)
        kameP.penup()
        kameP.left(180)
        kameP.forward(col * unit)
        kameP.left(90)
        kameP.forward(unit)
        kameP.left(90)
        kameP.pendown()
    f.close()

    # stamps an green arrow at start point, a red arrow at goal
    kameP.penup()
    kameP.color("red")
    kameP.setposition(int(goalP[0])*unit, int(goalP[1])*unit)
    kameP.stamp()
    kameP.color("green")
    kameP.setposition(int(startP[0])*unit, int(startP[1])*unit)
    kameP.stamp()

    kameP.pendown()
    walk()
    kameP.hideturtle()

    turtle.update()

    turtle.onscreenclick(get_mouse_click_coor)
    turtle.mainloop()

