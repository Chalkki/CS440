import math
import Astar
from draw_grid import draw
class Cell:
    def __init__(self, isblocked=False):
        self.isblocked = isblocked
        self.upperleft = None
        self.upperright = None
        self.lowerleft  = None
        self.lowerright = None

class Node:
    def __init__(self, x, y):
        self.parent = None
        self.g = math.inf
        self.h = 0
        self.f = self.g + self.h
        self.x = x
        self.y = y
        self.neighbor = []

    def __eq__(self, other):
        # equal? function
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        # less than function, put a standard to check which one is less
        return self.f < other.f

def initialize_cell(x, y, isblocked,grid, row, node_dict):
    # initialize the cell's vertices and put the cell into the grid list
    cell = Cell(isblocked)
    cell.upperleft = node_dict.get(str(x)+"/"+str(y))
    cell.upperright = node_dict.get(str(x+1)+"/"+str(y))
    cell.lowerleft = node_dict.get(str(x)+"/"+str(y+1))
    cell.lowerright = node_dict.get(str(x+1)+"/"+str(y+1))
    grid[str(x)+"/"+str(y)] = cell
    return grid


# def vertex_touch_cell(x,y,grid):
#     # check if the start and goal is not around boundary
#     # the cell coordinate is designated by its upperleft vertex
#     cell_1 = None
#     cell_2 = None
#     cell_3 = None
#     cell_4 = None
#     # check if there is upperleft cell
#     if (x-1) * (y-1) + (y-1) > 0:
#         cell_1 = grid[(x-1) * (y+1) + (y+1)]
#     # check if there is upperright cell
#     if x * (y+1) + (y+1) < len(grid):
#         cell_2 = grid[(x+1) * (y+1) + (y+1)]
#     # check if there is  left cell
#     # if the point is at the leftmost corner, it doesn't have a left cell
#     # if the point is at the lowermost corner, it also doesn't have a left cell
#     if (x-1) * y + y > 0 | (x-1) * y + y <len(grid) :
#         cell_3 = grid[ (x-1) * y + y]
#     # check if there is a right cell
#     if x * y + y < len(grid):
#         cell_4 = grid[x * y + y]
#     cells = []
#     # if cell is None, then it means the specific cell is not existed
#     for cell in [cell_1, cell_2, cell_3, cell_4]:
#         if cell is not None:
#             cells.append(cell)
#     return cells


def read_input(file,grid,node_dict):
    with open(file, 'r') as f:
        # startP and goalP is a list of two number strings, each string need to convert to be integer
        start_p = f.readline().split()
        goal_p = f.readline().split()
        size = f.readline().split()
        col = int(size[0])
        row = int(size[1])
        # initialize the node_dict
        for i in range(col+1):
            for j in range(row+1):
                x = i+1
                y = j+1
                node_dict[str(x)+"/"+str(y)] = Node(x, y)
                # print(x,y)
        # initialize cell and put it in the grid
        for i in range(col):
            for j in range(row):
                isblocked = True if f.readline().split()[2] == '1' else False
                # since x and y start at zero in the for loop and start at one in the description,
                # both x and y need to be added one to them to draw the graph
                x = i+1
                y = j+1

                grid = initialize_cell(x, y, isblocked,grid, row, node_dict)
    return start_p, goal_p, row, col,grid,node_dict


def main():
    grid = {}
    node_dict = {}
    x1 = None
    y1 = None
    x2 = None
    y2 = None
    path = None
    row = None
    col = None
    while True:
        try:
            file = input("Please enter the file name: ")
            start_p, goal_p, row, col,grid,node_dict = read_input(file,grid,node_dict)
            x1, y1, x2, y2 = int(start_p[0]), int(start_p[1]), int(goal_p[0]), int(goal_p[1])
            break
        except FileNotFoundError as err:
            print("File is not Found, make sure the file name is correct")
            continue
    # the grid and cell is now initialized, let's decide what algorithm we want to use
    while True:
        algo = input('Please enter the algorithm you want to use (Enter the word "astar" or "theta"): ')
        if algo == "astar":
            grid, node_dict, path = Astar.astar_main(x1, y1, x2, y2, grid, node_dict,row,col)
            break
        elif algo == "theta":
            print("we are working on theta now, stay tuned")
            break
        else:
            print('Invalid input. Please enter: "astar" or "theta"!')
    print(path)
    draw(grid, node_dict, [x1, y1], [x2, y2], row, col, path)


main()
