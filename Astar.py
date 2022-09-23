from math import sqrt
import heapq
import math

class Fringe:
    def __init__(self):
        self.heap=[]
        self.dict={}

    def isEmpty(self):
        return len(self.heap)==0

    def insert(self,f, node):
        heapq.heappush(self.heap, (f, node))
        self.dict[str(node.x)+"/"+str(node.y)] = 1

    def exist(self, key):
        return key in self.dict.keys()

    def pop(self):
        tmp = heapq.heappop(self.heap)[1]
        self.dict.pop(str(tmp.x)+"/"+str(tmp.y), "not found in fringe")
        return tmp

    def remove(self, f, node):
        heapq.heapreplace(self.heap, (f, node))

closed = {}
fringe=Fringe()
def astar(start, goal, node_dict):
    """Returns a list of lists as a path from the given start to the given end in the given grid"""

    # Add the start node
    fringe.insert(start.g+start.h, start)
    # Loop until you find the end
    while not fringe.isEmpty():

        # Get the current node
        current = fringe.pop()
        #print(x)
        if current == goal:
            path = []
            while current is not None:
                path.append([current.x, current.y])
                current = current.parent
            return node_dict, path[::-1]  # Return reversed path

        if str(current.x)+"/"+str(current.y) not in closed.keys():
            closed[str(current.x)+"/"+str(current.y)] = 1

        for neighbor_pos in current.neighbor:  # Adjacent vertex
            neighbor = node_dict[str(neighbor_pos[0])+"/"+str(neighbor_pos[1])]
            if str(neighbor.x)+"/"+str(neighbor.y) not in closed.keys():
                if not fringe.exist(str(neighbor.x)+"/"+str(neighbor.y)):
                    neighbor.g = math.inf
                    neighbor.parent = None
                UpdateVertex(current, neighbor, goal)
    return node_dict, []


def UpdateVertex(s, s_prime, goal):
    # Create the f, g, and h values
    if s.g + c(s, s_prime) < s_prime.g:
        s_prime.g = s.g + c(s,s_prime)
        # here is the heuristic function for the child
        s_prime.h = heuristic(s_prime, goal)
        s_prime.parent = s
        s_prime.f = s_prime.g + s_prime.h
        if fringe.exist(str(s_prime.x)+"/"+str(s_prime.y)):
            fringe.remove(s_prime.f, s_prime)
        else:
            fringe.insert(s_prime.f, s_prime)


def heuristic(s, goal):
    return sqrt(2) * (
        min(abs(s.x - goal.x), abs(s.y - goal.y))) + max(
        (abs(s.x - goal.x), abs(s.y - goal.y))) - min(
        abs(s.x - goal.x), abs(s.y - goal.y))


def c(s, s_prime):
        if s.x == s_prime.x:
            return 1
        if s.y == s_prime.y:
            return 1
        return sqrt(2)


# check surrounding
'''
1 2 3
4 x 5
6 7 8
'''
def initialize_neighbor(x,y,grid, node, row, col):
    if not block_check(x, y, grid, row, col):
        # self not blocked, add vertex 578
        if [x + 1, y] not in node.neighbor: node.neighbor.append([x + 1, y])
        if [x + 1, y + 1] not in node.neighbor: node.neighbor.append([x + 1, y + 1])
        if [x, y + 1] not in node.neighbor: node.neighbor.append([x, y + 1])
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
        if [x + 1, y + 1] not in node.neighbor: node.neighbor.append([x + 1, y + 1])
    return node


def block_check(x, y, grid, row, col):
    # check if grid is blocked
    index = str(x)+"/"+str(y)
    if x < 1 or y < 1 or x > col or y > row:
        return True
    if grid[index].isblocked:
        return True
    return False


def astar_main(x1, y1, x2, y2, grid, node_dict, row, col):
    # Create start and goal node
    start = node_dict.get(str(x1)+"/"+str(y1))
    goal = node_dict.get(str(x2)+"/"+str(y2))

    start.g = 0
    start.h = heuristic(start, goal)
    start.f = start.g + start.h

    goal.h = 0
    goal.f = goal.g + goal.h
    for i in range(col + 1):
        for j in range(row + 1):
            x = i + 1
            y = j + 1
            node_dict[str(x)+"/"+str(y)] = initialize_neighbor(x, y, grid,  node_dict[str(x)+"/"+str(y)], row, col)
    node_dict, path = astar(start, goal, node_dict)
    # return the grid for drawing the path
    return grid, node_dict, path

