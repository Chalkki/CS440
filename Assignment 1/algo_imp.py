# this is the implementation file of both algorithms
from math import sqrt
import heapq
import math
from re import I


class Fringe:
    def __init__(self):
        self.heap = []
        self.dict = {}

    def isEmpty(self):
        return len(self.heap) == 0

    def insert(self, f, node):
        global fringeCost, fringeMax  #space track
        heapq.heappush(self.heap, (f, node))
        self.dict[str(node.x) + "/" + str(node.y)] = 1
        fringeCost+=2
        if fringeCost>fringeMax:  #space track
            fringeMax=fringeCost

    def exist(self, key):
        return key in self.dict.keys()

    def pop(self):
        global fringeCost, fringeMax  #space track
        tmp = heapq.heappop(self.heap)[1]
        del self.dict[str(tmp.x) + "/" + str(tmp.y)]
        fringeCost-=2  #space track
        return tmp

    def remove(self, f, node):
        global fringeCost, fringeMax  #space track
        self.heap.remove((f,node))
        heapq.heapify(self.heap)
        del self.dict[str(node.x) + "/" + str(node.y)]
        fringeCost-=2  #space track

def algo_main(start, goal, node_dict, algo_type, grid):
    """Returns a list of lists as a path from the given start to the given end in the given grid"""

    # Add the start node
    fringe.insert(start.g + start.h, start)
    # Loop until you find the end
    while not fringe.isEmpty():

        # Get the current node
        current = fringe.pop()
        if current == goal:
            path = []
            while current != start:
                path.append([current.x, current.y])
                current = current.parent
            path.append([start.x,start.y])
            return node_dict, path[::-1]  # Return reversed path

        if str(current.x) + "/" + str(current.y) not in closed.keys():
            closed[str(current.x) + "/" + str(current.y)] = 1

        for neighbor_pos in current.neighbor:  # Adjacent vertex
            # print(neighbor_pos)
            neighbor = node_dict[str(neighbor_pos[0]) + "/" + str(neighbor_pos[1])]
            if str(neighbor.x) + "/" + str(neighbor.y) not in closed.keys():
                if not fringe.exist(str(neighbor.x) + "/" + str(neighbor.y)):
                    neighbor.g = math.inf
                    neighbor.parent = None
                UpdateVertex(current, neighbor, algo_type, grid)
    print("Path not found")
    return node_dict, []


def LineOfSight(s, s_prime, grid):
    x0 = s.x
    y0 = s.y
    x1 = s_prime.x
    y1 = s_prime.y
    f = 0
    dy = y1 - y0
    dx = x1 - x0

    if dy < 0:
        dy = -dy
        s_y = -1
    else:
        s_y = 1
    if dx < 0:
        dx = -dx
        s_x = -1
    else:
        s_x = 1
    if s_x == -1:
        s_x_2 = -1
    else:
        s_x_2 = 0
    if s_y == -1:
        s_y_2 = -1
    else:
        s_y_2 = 0
    if dx >= dy:
        while x0 != x1:
            f = f + dy
            # print(index)
            index_1 = str(x0 + s_x_2) + "/" + str(y0 + s_y_2)
            if f >= dx:
                if index_1 not in grid.keys() or grid[index_1].isblocked:
                    return False
                y0 = y0 + s_y
                f = f - dx
            index_2 = str(x0 + s_x_2) + "/" + str(y0 + s_y_2)
            if f != 0 and (index_2 not in grid.keys() or grid[index_2].isblocked):
                return False
            if (dy == 0 and (str(x0 + s_x_2) + "/" + str(y0) not in grid.keys() or
                             grid[str(x0 + s_x_2) + "/" + str(y0)].isblocked) and
                    (str(x0 + s_x_2) + "/" + str(y0 - 1) not in grid.keys() or
                     grid[str(x0 + s_x_2) + "/" + str(y0 - 1)].isblocked)):
                return False
            x0 = x0 + s_x
    else:
        while y0 != y1:
            f = f + dx
            index_3 = str(x0 + s_x_2) + "/" + str(y0 + s_y_2)
            if f >= dy:
                if index_3 not in grid.keys() or grid[index_3].isblocked:
                    return False
                x0 = x0 + s_x
                f = f - dy
            index_4 = str(x0 + s_x_2) + "/" + str(y0 + s_y_2)
            if f != 0 and (index_4 not in grid.keys() or grid[index_4].isblocked):
                return False
            if (dx == 0 and (str(x0) + "/" + str(y0 + s_y_2) not in grid.keys() or
                             grid[str(x0) + "/" + str(y0 + s_y_2)].isblocked) and
                    (str(x0 - 1) + "/" + str(y0 + s_y_2) not in grid.keys() or
                     grid[str(x0 - 1) + "/" + str(y0 + s_y_2)].isblocked)):
                return False
            y0 = y0 + s_y
    return True


def UpdateVertex(s, s_prime, algo_type, grid):
    # if the algorithm type is theta, check line of sight. If line of sight returns False,
    # then check if path 1 is valid.
    if algo_type == "theta" and LineOfSight(s.parent, s_prime, grid):
        # Path 2
        if s.parent.g + c(s.parent, s_prime) < s_prime.g:
            if fringe.exist(str(s_prime.x) + "/" + str(s_prime.y)):
                fringe.remove(s_prime.f, s_prime)
            s_prime.g = s.parent.g + c(s.parent, s_prime)
            s_prime.parent = s.parent
            s_prime.f = s_prime.g + s_prime.h
            fringe.insert(s_prime.f, s_prime)
    else:
        # Path 1
        if s.g + c(s, s_prime) < s_prime.g:
            if fringe.exist(str(s_prime.x) + "/" + str(s_prime.y)):
                fringe.remove(s_prime.f, s_prime)
            s_prime.g = s.g + c(s, s_prime)
            s_prime.parent = s
            s_prime.f = s_prime.g + s_prime.h
            fringe.insert(s_prime.f, s_prime)

def heuristic_astar(s, goal):
    return sqrt(2) * (
        min(abs(s.x - goal.x), abs(s.y - goal.y))) + max(
        (abs(s.x - goal.x), abs(s.y - goal.y))) - min(
        abs(s.x - goal.x), abs(s.y - goal.y))


def heuristic_theta(s, goal):
    # use pythagorean theorem to get the any-angle path
    dx = abs(s.x - goal.x)
    dy = abs(s.y - goal.y)
    return sqrt((dx * dx) + (dy * dy))


def c(s, s_prime):
    dx = abs(s.x - s_prime.x)
    dy = abs(s.y - s_prime.y)
    return sqrt((dx * dx) + (dy * dy))


# check surrounding
'''
if x is not in the first row and first col
1 2 3
4 x 5
6 7 8

if x is in the first row
4 x 5
6 7 8

if x is in the first column
2 3
x 5
7 8

'''
def initialize_neighbor(x, y, grid, node, row, col):
    if not block_check(x, y, grid, row, col):
        # self not blocked, add vertex 578
        if [x + 1, y] not in node.neighbor: node.neighbor.append([x + 1, y])
        if [x, y + 1] not in node.neighbor: node.neighbor.append([x, y + 1])
        if [x + 1, y + 1] not in node.neighbor: node.neighbor.append([x + 1, y + 1])
    if not block_check(x - 1, y - 1, grid, row, col):
        # upper left not blocked, add vertex 124
        if [x - 1, y - 1] not in node.neighbor: node.neighbor.append([x - 1, y - 1])
        if [x, y - 1] not in node.neighbor: node.neighbor.append([x, y - 1])
        if [x - 1, y] not in node.neighbor: node.neighbor.append([x - 1, y])
    if not block_check(x, y - 1, grid, row, col):
        # upper right not blocked, add vertex 235
        if [x, y - 1] not in node.neighbor: node.neighbor.append([x, y - 1])
        if [x + 1, y - 1] not in node.neighbor: node.neighbor.append([x + 1, y - 1])
        if [x + 1, y] not in node.neighbor: node.neighbor.append([x + 1, y])
    if not block_check(x - 1, y, grid, row, col):
        # left block not blocked, add vertex 467
        if [x - 1, y] not in node.neighbor: node.neighbor.append([x - 1, y])
        if [x - 1, y + 1] not in node.neighbor: node.neighbor.append([x - 1, y + 1])
        if [x, y + 1] not in node.neighbor: node.neighbor.append([x, y + 1])
    return node

def vg_neighbor(x,y,col,row,node_dict,grid):
    s = node_dict[str(x)+"/"+str(y)]
    # start from the next element to check the neighbors
    for i in range(x-1,col+1):
        for j in range(y, row+1):
            x_prime = i+1
            y_prime = j+1
            s_prime = node_dict[str(x_prime)+"/"+str(y_prime)]
            if LineOfSight(s, s_prime, grid):
                # if the two nodes can touch each other, make them be neighbors of each other
                node_dict[str(x) + "/" + str(y)].neighbor.append([x_prime, y_prime])
                node_dict[str(x_prime)+"/"+str(y_prime)].neighbor.append([x, y])
    return node_dict

def block_check(x, y, grid, row, col):
    # check if grid is blocked
    index = str(x) + "/" + str(y)
    if x < 1 or y < 1 or x > col or y > row:
        return True
    if grid[index].isblocked:
        return True
    return False

closed = {}
fringe = Fringe()
fringeCost=0  #space track
fringeMax=0
def main(x1, y1, x2, y2, grid, node_dict, row, col, algo_type):
    global closed, fringe, fringeCost
    closed = {}
    fringe = Fringe()
    fringeCost=0  #space track
    fringeMax=0
    # Create start and goal node
    start = node_dict.get(str(x1) + "/" + str(y1))
    goal = node_dict.get(str(x2) + "/" + str(y2))

    start.g = 0
    start.parent = start
    if algo_type == "astar":
        start.h = heuristic_astar(start, goal)
    else:
        start.h = heuristic_theta(start, goal)
    start.f = start.g + start.h

    goal.h = 0
    goal.f = goal.g + goal.h

    for i in range(col + 1):
        for j in range(row + 1):
            x = i + 1
            y = j + 1
            if algo_type == "astar" or algo_type == "vg":
                node_dict[str(x) + "/" + str(y)].h = heuristic_astar(node_dict[str(x) + "/" + str(y)], goal)
            else:
                node_dict[str(x) + "/" + str(y)].h = heuristic_theta(node_dict[str(x) + "/" + str(y)], goal)
            if algo_type == "astar" or algo_type == "theta":
                node_dict[str(x) + "/" + str(y)] = initialize_neighbor(x, y, grid, node_dict[str(x) + "/" + str(y)], row,
                                                                   col)
            else:
                node_dict = vg_neighbor(x, y, col, row, node_dict, grid)
    if algo_type == "vg":
        # after initializing the neighbors in visibility graph, we could change the algo_type to astar for the
        # remaining calculation.
        algo_type = "astar"
    node_dict, path = algo_main(start, goal, node_dict, algo_type, grid)
    # return the grid for drawing the path
    return grid, node_dict, path, fringeMax+len(closed) #space track
