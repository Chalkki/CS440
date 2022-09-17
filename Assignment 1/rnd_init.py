
def grid_init(sample_name):
    import random
    # get the x_cord and y_cord of start vertex and goal vertex randomly
    # x1,y1 are the x_cord and y_cord of the start vertex
    # x2,y2 are the x_cord and y_cord of the goal vertex
    x_range = range(1,100)
    y_range = range(1,50)
    x1,y1,x2,y2 = random.choice(x_range), random.choice(y_range), random.choice(x_range), random.choice(y_range)
    v_list = [[x1,y1],[x2,y2]]

    # Since we have 100 cols and 50 rows, we then have 99 x 49 = 4851 cells.
    # 10 % of the cells are blocked, let's take 485 as blocked cells.
    ones = [one for one in ("1" * 485)]
    zeros = [zero for zero in ("0" * 4366)]
    cell_status = ones + zeros
    random.shuffle(cell_status)

    # write out the data on the text file
    # first 3 lines are the start vertex, end vertex and dimension of the grid
    # the left lines are the cells' coordinates and their status
    with open(sample_name+".txt", "w") as f:
        for x in range(3):
            first_arg = None
            second_arg = None
            if x != 2:
                first_arg = str(v_list[x][0])
                second_arg = str(v_list[x][1])
            else:
                first_arg = str(99)
                second_arg = str(49)
            f.write(first_arg + " ")
            f.write(second_arg + " ")
            f.write("\n")
        count = 0
        for x_cord in x_range:
            for y_cord in y_range:
                f.write(str(x_cord) + " ")
                f.write(str(y_cord) + " ")
                f.write(cell_status[count])
                if count != 4850:
                    f.write("\n")
                count += 1

# Allow the user to choose the number of samples they want to generate
while True:
    try:
        sample_count = int(input("Enter the number of grid samples you want to generate: "))
        if sample_count <= 0:
            raise ValueError
        break
    except ValueError as err:
        print("Please enter a positive integer")
for x in range(sample_count):
    sample_name = "sample_" + str(x+1)
    grid_init(sample_name)