from math import sqrt
import heapq
import math

def astar(start, goal, node_dict):
    """Returns a list of lists as a path from the given start to the given end in the given grid"""
    # Initialize both open and closed list
    fringe = []
    fringe_search = {}
    closed = {}
    # Add the start node
    heapq.heappush(fringe, (start.g + start.h, start))
    fringe_search[str(start.x)+"/"+str(start.y)] = 1
    # Loop until you find the end
    while len(fringe) > 0:

        # Get the current node
        heap_item = heapq.heappop(fringe)
        current = heap_item[1]
        fringe_search.pop(str(current.x)+"/"+str(current.y), "not found in fringe")
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
                if str(neighbor.x)+"/"+str(neighbor.y) not in fringe_search.keys():
                    neighbor.g = math.inf
                    neighbor.parent = None
                fringe, fringe_search = UpdateVertex(fringe, fringe_search, current, neighbor, goal)
    return node_dict, []


def UpdateVertex(fringe, fringe_search, s, s_prime, goal):
    # Create the f, g, and h values
    if s.g + c(s, s_prime) < s_prime.g:
        s_prime.g = s.g + c(s,s_prime)
        # here is the heuristic function for the child
        s_prime.h = heuristic(s_prime, goal)
        s_prime.parent = s
        s_prime.f = s_prime.g + s_prime.h
        if str(s_prime.x)+"/"+str(s_prime.y) in fringe_search.keys():
            heapq.heapreplace(fringe, (s_prime.f, s_prime))
        else:
            heapq.heappush(fringe, (s_prime.f, s_prime))
        fringe_search[str(s_prime.x)+"/"+str(s_prime.y)] = 1
    return fringe, fringe_search


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

