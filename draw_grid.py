# please use python3
# see instructions here (https://resources.cs.rutgers.edu/docs/using-python-on-cs-linux-machines/)

from tkinter import UNITS
import turtle
import unittest
class Cell:
    def __init__(self, isblocked=False):
        self.isblocked = isblocked
        self.upperleft = []
        self.upperright = []
        self.lowerleft = []
        self.lowerright = []


grid = []


def vertexBelongsToCell(x1, y1, x2, y2):
    start_cell = []
    end_cell = []
    for cell in grid:
        if [x1, y1] == cell.upperleft:
            start_cell.append(cell)
            continue
        elif [x2, y2] == cell.upperleft:
            end_cell.append(cell)
            continue
        if [x1, y1] == cell.upperright:
            start_cell.append(cell)
            continue
        elif [x2, y2] == cell.upperright:
            end_cell.append(cell)
            continue
        if [x1, y1] == cell.lowerleft:
            start_cell.append(cell)
            continue
        elif [x2, y2] == cell.lowerleft:
            end_cell.append(cell)
            continue
        if [x1, y1] == cell.lowerright:
            start_cell.append(cell)
            continue
        elif [x2, y2] == cell.lowerright:
            end_cell.append(cell)
            continue
    path_cells = [cell for cell in start_cell if cell in end_cell]
    return path_cells

def path_blocked_astar(path_cells):
    blocked = True
    for cell in path_cells:
        blocked = blocked & cell.isblocked
    return blocked

def initialize_cell(x, y, isblocked):
    # initialize the cell and put it into the grid list
    cell = Cell(isblocked)

    cell.upperleft = [x, y]
    cell.upperright = [x+1, y]
    cell.lowerleft = [x, y-1]
    cell.lowerright = [x+1, y-1]
    print(x,y)
    grid.append(cell)
def draw(file):

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
            kameP.left(90)
        if isblock:
            kameP.end_fill()
            kameP.color("black")

    f = open(file, 'r')
    startP=f.readline().split()
    goalP=f.readline().split()
    size=f.readline().split()
    row = int(size[0])
    col = int(size[1])

    screen.setup(row*unit,col*unit)
    screen.setworldcoordinates(unit, ((col+1)*unit), (row+1)*unit, unit)  #enable our coordinate system
    turtle.tracer(0, 0)  # to skip animation
    kameP.penup()
    kameP.setposition(unit,unit)
    kameP.pendown()

    for x in range(col):
        for y in range(row):
            isblocked = True if f.readline().split()[2]=='1' else False
            # initialize the cell
            initialize_cell(x, y, isblocked)
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
    kameP.setposition(int(startP[0])*unit, int(startP[1])*unit)
    kameP.stamp()
    kameP.color("red")
    kameP.setposition(int(goalP[0])*unit, int(goalP[1])*unit)
    kameP.stamp()

    turtle.update()
    f.close()

    turtle.onscreenclick(get_mouse_click_coor)
    #turtle.mainloop()
    turtle.done()




#
# fileN = input("File name? ")
# draw('Assignment 1/'+fileN)
