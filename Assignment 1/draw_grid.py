# please use python3
# see instructions here (https://resources.cs.rutgers.edu/docs/using-python-on-cs-linux-machines/)

from tkinter import UNITS
import turtle
import unittest


def draw(fileN, path, node_dict):

    unit = 10  #change to change size
    kameP = turtle.Turtle()  #turtle to draw
    screen = turtle.Screen()

    def findInfo(x,y):
        tmp = node_dict["{X}/{Y}".format(X="{:.0f}".format(x), Y="{:.0f}".format(y))]
        return ("({X},{Y}): h={H}, g={G}, f={F}"
                .format(X="{:.0f}".format(x), Y="{:.0f}".format(y), H=tmp.h, G=tmp.g, F=tmp.g+tmp.h))

    def get_mouse_click_coor(x, y):
        if unit>x or x>(row+1)*unit or unit>y or y>(col+1)*unit:
            return
        else:
            x//=unit
            y//=unit
        screen.title("Grid({X},{Y})".format(X="{:.0f}".format(x), Y="{:.0f}".format(y)))
        print(
            '''
            Grid({X},{Y})
            Upper left vertex: {s1}
            Upper right vertex: {s2}
            Lower left vertex: {s3}
            Lower right vertex: {s4}
            '''
            .format(X="{:.0f}".format(x), Y="{:.0f}".format(y),
                    s1=findInfo(x,y), s2=findInfo(x+1, y), s3=findInfo(x,y+1), s4=findInfo(x+1,y+1))
            )

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
    screen.setup((row+1)*unit,(col+1)*unit)
    print(unit, ((col+1)*unit), (row+1)*unit, unit)
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

