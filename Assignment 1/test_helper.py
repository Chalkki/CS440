from colorsys import yiq_to_rgb
import cs440_assignment_1, algo_imp, algo_imp_alt
import math
import time
import matplotlib.pyplot as plt

def pathlen(path):
    path_length = 0
    for i in range(len(path) - 1):
        block_1 = path[i]
        block_2 = path[i+1]
        x1,y1 = block_1[0], block_1[1]
        x2,y2 = block_2[0], block_2[1]
        del_x = abs(x1 - x2)
        del_y = abs(y1 - y2)
        d = math.sqrt((del_x * del_x) +(del_y * del_y))
        path_length = path_length + d
    return path_length

def runfile(fileN):
    grid = {}
    node_dict = {}
    x1 = None
    y1 = None
    x2 = None
    y2 = None
    path_a = None
    path_t=None
    row = None
    col = None
    start_a = 0
    end_a = 0
    start_t = 0
    end_t = 0

    start_p, goal_p, row, col,grid,node_dict = cs440_assignment_1.read_input(fileN,grid,node_dict)
    x1, y1, x2, y2 = int(start_p[0]), int(start_p[1]), int(goal_p[0]), int(goal_p[1])

    #astar
    start_a = time.time()
    grid, node_dict, path_a, cost_a = algo_imp.main(x1, y1, x2, y2, grid, node_dict, row, col, "astar")
    end_a = time.time()

    #theta
    start_t = time.time()
    grid, node_dict, path_t, cost_t = algo_imp.main(x1, y1, x2, y2, grid, node_dict, row, col, "theta")
    end_t = time.time()

    #return path_a, end_a-start_a, path_t, end_t-start_t
    return cost_a, cost_t

def runfile_alt(fileN):
    grid = {}
    node_dict = {}
    x1 = None
    y1 = None
    x2 = None
    y2 = None
    path_a = None
    path_t=None
    row = None
    col = None
    start_a = 0
    end_a = 0
    start_t = 0
    end_t = 0

    start_p, goal_p, row, col,grid,node_dict = cs440_assignment_1.read_input(fileN,grid,node_dict)
    x1, y1, x2, y2 = int(start_p[0]), int(start_p[1]), int(goal_p[0]), int(goal_p[1])

    #astar
    start_a = time.time()
    grid, node_dict, path_a, cost_a = algo_imp_alt.main(x1, y1, x2, y2, grid, node_dict, row, col, "astar")
    end_a = time.time()

    #theta
    start_t = time.time()
    grid, node_dict, path_t, cost_t = algo_imp_alt.main(x1, y1, x2, y2, grid, node_dict, row, col, "theta")
    end_t = time.time()

    #return path_a, end_a-start_a, path_t, end_t-start_t
    return cost_a, cost_t

def samples():
    f = open("results.txt", "w")
    for i in range(50):
        fileN = 'sample_'+str(i+1)
        ap, at, tp, tt = runfile('Assignment 1/test/'+fileN+'.txt')
        f.write('{name}:{ap}:{al}:{at}:{tp}:{tl}:{tt}\n'.format(name=fileN,ap=ap,al=pathlen(ap),at=at,tp=tp,tl=pathlen(tp),tt=tt))
        print(fileN)
    f.close()

def space_cost():
    x=[]
    ya=[]
    yt=[]
    ya_alt=[]
    yt_alt=[]
    for i in range(50):
        fileN = 'sample_'+str(i+1)
        #_, at, _, tt = runfile('Assignment 1/test/'+fileN+'.txt')
        #_, at_alt, _, tt_alt = runfile_alt('Assignment 1/test/'+fileN+'.txt')
        cost_a, cost_t = runfile('Assignment 1/test/'+fileN+'.txt')
        cost_a_alt, cost_t_alt = runfile_alt('Assignment 1/test/'+fileN+'.txt')
        x.append(i)
        ya.append(cost_a)
        yt.append(cost_t)
        ya_alt.append(cost_a_alt)
        yt_alt.append(cost_t_alt)
        print(fileN)

    plt.plot(x,yt, label='space complexity on new theta')
    #plt.plot(x,ya, label='space complexity on new astar')
    plt.plot(x,yt_alt, label='space complexity on theta')
    #plt.plot(x,ya_alt, label='space complexity on astar')

    plt.title('Space complexity on search algorithms and sample')
    plt.xlabel('sample file')
    plt.ylabel('space cost')
    plt.legend(loc='upper left')
    plt.show()



if __name__ == "__main__":
    space_cost()
    #samples()