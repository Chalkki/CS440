import math
import time

import algo_imp
from draw_grid import draw


class Cell:
    def __init__(self, isblocked=False):
        self.isblocked = isblocked
        self.upperleft = None
        self.upperright = None
        self.lowerleft = None
        self.lowerright = None


class Node:
    def __init__(self, x, y):
        self.parent = None
        self.g = math.inf
        self.h = 0
        self.f = math.inf
        self.x = x
        self.y = y
        self.neighbor = []

    def __eq__(self, other):
        # equal? function
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        # less than function, put a standard to check which one is less
        return self.f < other.f


def initialize_cell(x, y, isblocked, grid, row, node_dict):
    # initialize the cell's vertices and put the cell into the grid list
    cell = Cell(isblocked)
    cell.upperleft = node_dict.get(str(x) + "/" + str(y))
    cell.upperright = node_dict.get(str(x + 1) + "/" + str(y))
    cell.lowerleft = node_dict.get(str(x) + "/" + str(y + 1))
    cell.lowerright = node_dict.get(str(x + 1) + "/" + str(y + 1))
    grid[str(x) + "/" + str(y)] = cell
    return grid


def read_input(file, grid, node_dict):
    with open(file, 'r') as f:
        # startP and goalP is a list of two number strings, each string need to convert to be integer
        start_p = f.readline().split()
        goal_p = f.readline().split()
        size = f.readline().split()
        col = int(size[0])
        row = int(size[1])
        # initialize the node_dict
        for i in range(col + 1):
            for j in range(row + 1):
                x = i + 1
                y = j + 1
                node_dict[str(x) + "/" + str(y)] = Node(x, y)
                # print(x,y)
        # initialize cell and put it in the grid
        for i in range(col):
            for j in range(row):
                isblocked = True if f.readline().split()[2] == '1' else False
                # since x and y start at zero in the for loop and start at one in the description,
                # both x and y need to be added one to them to draw the graph
                x = i + 1
                y = j + 1

                grid = initialize_cell(x, y, isblocked, grid, row, node_dict)
    return start_p, goal_p, row, col, grid, node_dict


if __name__ == "__main__":
    grid = {}
    node_dict = {}
    x1 = None
    y1 = None
    x2 = None
    y2 = None
    path = None
    row = None
    col = None
    start = 0
    end = 0
    while True:
        try:
            fileN = input("Please enter the file name: ")
            start_p, goal_p, row, col, grid, node_dict = read_input(fileN, grid, node_dict)
            x1, y1, x2, y2 = int(start_p[0]), int(start_p[1]), int(goal_p[0]), int(goal_p[1])
            break
        except FileNotFoundError as err:
            print("File is not Found, make sure the file name is correct")
            continue
    # the grid and cell is now initialized, let's decide what algorithm we want to use
    while True:
        algo_type = input('Please enter the algorithm you want to use (Enter the word "astar" or "theta" or "vg" '
                          'for visibility graph): ')
        if algo_type == "astar" or algo_type == "theta" or algo_type == "vg":
            start = time.time()
            grid, node_dict, path = algo_imp.main(x1, y1, x2, y2, grid, node_dict, row, col, algo_type)
            end = time.time()
            break
        # elif algo_type == "theta":
        #     start = time.time()
        #     grid, node_dict, path = algo_imp.main(x1, y1, x2, y2, grid, node_dict, row, col, algo_type)
        #     end = time.time()
        #     break
        else:
            print('Invalid input. Please enter: "astar" or "theta" or "vg"!')
    print(path)
    print("Time elapsed in seconds: ", end - start)
    path_length = 0
    for i in range(len(path) - 1):
        block_1 = path[i]
        block_2 = path[i + 1]
        x1, y1 = block_1[0], block_1[1]
        x2, y2 = block_2[0], block_2[1]
        del_x = abs(x1 - x2)
        del_y = abs(y1 - y2)
        d = math.sqrt((del_x * del_x) + (del_y * del_y))
        path_length = path_length + d
    print("The total path length: ", path_length)
    draw(fileN, path, node_dict)
