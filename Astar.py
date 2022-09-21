from math import sqrt
import heapq


class Node:
    def __init__(self, parent=None, x=None, y=None):
        self.parent = parent
        self.g = float('inf')
        self.h = 0
        self.f = 0
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def astar(grid, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given grid"""

    # Create start and end node
    start = Node(start)
    start.g = start.h = start.f = 0
    goal = Node(end)
    goal.g = goal.h = goal.f = 0

    # Initialize both open and closed list
    fringe = []
    fringe_search = {}
    closed = {}
    # Add the start node
    heapq.heappush(fringe, (start.g + start.h, start))
    fringe_search[start] = 1
    # Loop until you find the end
    while len(fringe) > 0:

        # Get the current node
        current = heapq.heappop(fringe)
        del fringe_search[current]

        if current == goal:
            path = []
            while current is not None:
                path.append([current.x, current.y])
                current = current.parent
            return path[::-1]  # Return reversed path

        if current not in closed.keys():
            closed[current] = 1

        # # Found the goal
        # if current == goal:
        #     path = []
        #     current = current
        #     while current is not None:
        #         path.append(current.position)
        #         current = current.parent
        #     return path[::-1] # Return reversed path

        # Generate children
        neighbors = []
        for new_position in [[0, -1], [0, 1], [-1, 0], [1, 0],
                             [-1, -1], [-1, 1], [1, -1], [1, 1]]:  # Adjacent squares

            # Get node position
            node_position = [current.x + new_position[0],
                             current.y + new_position[1]]

            # Create new node
            new_node = Node(None, node_position[0], node_position[1])
            if not closed(new_node):
                if not fringe
            # Append
        #     neighbors.append(new_node)
        #
        # # Loop through children
        # for child in neighbors:
        #
        #     # Child is on the closed list
        #     for closed_child in closed:
        #         if child == closed_child:
        #             continue

            # Create the f, g, and h values
            # child.g = current.g + 1
            # child.h = sqrt(2) * (
            #     min((child.position[0] - goal.position[0]), (child.position[1] - goal.position[1]))) + max(
            #     ((child.position[0] - goal.position[0]), (child.position[1] - goal.position[1]))) - min(
            #     (child.position[0] - goal.position[0]), (child.position[1] - goal.position[1]))
            # child.f = child.g + child.h


            UpdateVertex(current, child, goal)
            # Child is already in the open list
            for open_node in fringe:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            fringe.append(child)

def UpdateVertex(fringe,s, s_prime, goal):
    # Create the f, g, and h values
    if s.g + c(s,s_prime) < s_prime.g:
        s_prime.g = s.g + c(s,s_prime)
        # here is the heuristic function for the child
        s_prime.h = sqrt(2) * (
            min((s_prime.position[0] - goal.position[0]), (s_prime.position[1] - goal.position[1]))) + max(
            ((s_prime.position[0] - s_prime.position[0]), (s_prime.position[1] - goal.position[1]))) - min(
            (s_prime.position[0] - goal.position[0]), (s_prime.position[1] - goal.position[1]))
        s_prime.parent = s
        s_prime.f = s_prime.g + s_prime.h
        heapq.heapreplace(fringe,s_prime.f)
        return fringe

def c(s, s_prime):
    if not is_path_blocked(s, s_prime):
        if s.x == s_prime.x:
            return 1
        if s.y == s_prime.y:
            return 1
        return sqrt(2)
    return float('inf')


def is_path_blocked(s, s_prime):
    return False
    return "No path found"
