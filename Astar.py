from math import sqrt


class Node():
    
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(grid, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given grid"""

    # Create start and end node
    start = Node(None, start)
    start.g = start.h = start.f = 0
    goal = Node(None, end)
    goal.g = goal.h = goal.f = 0

    # Initialize both open and closed list
    fringe = []
    closed = []

    # Add the start node
    fringe.append(start)

    # Loop until you find the end
    while len(fringe) > 0:

        # Get the current node
        current = fringe[0]
        current_index = 0
        for index, item in enumerate(fringe):
            if item.f < current.f:
                current = item
                current_index = index

        # Pop current off open list, add to closed list
        fringe.pop(current_index)
        closed.append(current)

        # Found the goal
        if current == goal:
            path = []
            current = current
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        neighbors = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current.position[0] + new_position[0], current.position[1] + new_position[1])

            # Create new node
            new_node = Node(current, node_position)

            # Append
            neighbors.append(new_node)

        # Loop through children
        for child in neighbors:

            # Child is on the closed list
            for closed_child in closed:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current.g + 1
            child.h = sqrt(2) * (min((child.position[0] - goal.position[0]), (child.position[1] - goal.position[1]))) + max(((child.position[0] - goal.position[0]), (child.position[1] - goal.position[1]))) - min((child.position[0] - goal.position[0]), (child.position[1] - goal.position[1]))
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in fringe:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            fringe.append(child)

    return "No path found"        