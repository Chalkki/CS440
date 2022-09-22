from math import sqrt
import heapq
import draw_grid as dg
import math
grid = dg.grid


class Node:
    def __init__(self, parent=None, x=None, y=None):
        self.parent = parent
        self.g = math.inf
        self.h = 0
        self.f = self.g + self.h
        self.x = x
        self.y = y

    def __eq__(self, other):
        # equal? function
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        # less than function, put a standard to check which one is less
        return self.f < other.f


def astar(start, goal):
    """Returns a list of tuples as a path from the given start to the given end in the given grid"""
    # Initialize both open and closed list
    fringe = []
    fringe_search = {}
    closed = {}
    # Add the start node
    heapq.heappush(fringe, (start.g + start.h, start))
    fringe_search[start.x*start.y+start.y] = 1
    # Loop until you find the end
    while len(fringe) > 0:

        # Get the current node
        heap_item = heapq.heappop(fringe)
        current = heap_item[1]
        x = fringe_search.pop(current.x*current.y+current.y, "not found in fringe")
        print(x)
        if current == goal:
            path = []
            while current is not None:
                path.append([current.x, current.y])
                current = current.parent
            return path[::-1]  # Return reversed path

        if current.x*current.y+current.y not in closed.keys():
            closed[current.x*current.y+current.y] = 1


        # Generate children
        for new_position in [[0, -1], [0, 1], [-1, 0], [1, 0],
                             [-1, -1], [-1, 1], [1, -1], [1, 1]]:  # Adjacent squares

            # Get node position
            node_position = [current.x + new_position[0],
                             current.y + new_position[1]]

            # Create new node
            new_node = Node(None, node_position[0], node_position[1])
            # see if the new path is valid
            if is_path_blocked(current, new_node):
                continue
            if new_node.x*new_node.y+new_node.y not in closed.keys():
                if new_node.x*new_node.y+new_node.y not in fringe_search.keys():
                    new_node.g = math.inf
                    new_node.parent = None
                fringe, fringe_search = UpdateVertex(fringe, fringe_search, current, new_node, goal)

    return []


def UpdateVertex(fringe, fringe_search, s, s_prime, goal):
    # Create the f, g, and h values
    if s.g + c(s, s_prime) < s_prime.g:
        s_prime.g = s.g + c(s,s_prime)
        # here is the heuristic function for the child
        s_prime.h = heuristic(s_prime, goal)
        s_prime.parent = s
        s_prime.f = s_prime.g + s_prime.h
        if s_prime.x*s_prime.y+s_prime.y in fringe_search.keys():
            heapq.heapreplace(fringe, (s_prime.f, s_prime))
        else:
            heapq.heappush(fringe, (s_prime.f, s_prime))
        fringe_search[s_prime.x*s_prime.y+s_prime.y] = 1
        return fringe, fringe_search


def heuristic(s, goal):
    return sqrt(2) * (
        min(abs(s.x - goal.x), abs(s.y - goal.y))) + max(
        (abs(s.x - goal.x), abs(s.y - goal.y))) - min(
        abs(s.x - goal.x), abs(s.y - goal.y))


def c(s, s_prime):
    if not is_path_blocked(s, s_prime):
        if s.x == s_prime.x:
            return 1
        if s.y == s_prime.y:
            return 1
        return sqrt(2)
    return float('inf')


def is_path_blocked(start_node, end_node):
    path_cells = dg.vertexBelongsToCell(start_node.x, start_node.y,
                                        end_node.x, end_node.y)
    return dg.path_blocked(path_cells)


def astar_main():
    fileN = input("File name? ")
    dg.draw('Assignment 1/' + fileN)
    with open('Assignment 1/' + fileN, 'r') as f:
        start_p = f.readline().split()
        goal_p = f.readline().split()
    # Create start and goal node
    start = Node(None, int(start_p[0]), int(start_p[1]))
    goal = Node(None, int(goal_p[0]), int(goal_p[1]))

    start.g = 0
    start.h = heuristic(start, goal)
    start.f = start.g + start.h

    goal.h = 0
    goal.f = goal.g + goal.h
    print(astar(start, goal))

astar_main()