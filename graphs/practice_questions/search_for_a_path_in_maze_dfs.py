import random

maze1 = [
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

maze2 = [
    [0, 1, 1],
    [0, 0, 0],
    [1, 0, 0]
]

#use dfs when we want to check if a path exists
def find_if_path_exists(start_x, start_y, end_x, end_y, maze):
    print("Starting at: (" + str([start_x, start_y]) + ")")
    print("Ending at: (" + str([end_x, end_y]) + ")")

    if maze == None or (start_x < 0 or start_x > len(maze)) or (start_y < 0 or start_y > len(maze[0])) or \
        (end_x < 0 or end_x > len(maze)) or (end_y < 0 or end_y > len(maze[0])):
        return -1

    visited = []
    stack = []
    directional_vectors = [[1,0], [0,1], [-1, 0], [0, -1]]

    stack.append([start_x, start_y])

    while stack:
        curr_x, curr_y = stack.pop()

        visited.append([curr_x, curr_y])

        if (curr_x == end_x and curr_y == end_y):
            #print("Found end: " + str([curr_x, curr_y]))
            print_graph(visited)
            return visited
        
        for each_vector in directional_vectors:
            x_dir = each_vector[0]
            y_dir = each_vector[1]

            new_x = curr_x - x_dir
            new_y = curr_y - y_dir

            if (new_x >= 0 and new_x < len(maze) and new_y >= 0 and new_y < len(maze[0]) and maze[new_x][new_y] == 0 and [new_x, new_y] not in visited):
                #print("Appending: " + str([new_x, new_y]))
                stack.append([new_x, new_y])
    
    print("Could not find the end ...")
    return -1

def print_graph(ans):
    for i in range(0, len(ans)-1):
        print(ans[i], end="")
        print("->", end="")
    print(ans[-1]) 

start_x = 0
start_y = 0
end_x = 1
end_y = 8
find_if_path_exists(start_x, start_y, end_x, end_y, maze1)

start_x = 0
start_y = 0
end_x = 2
end_y = 2
find_if_path_exists(start_x, start_y, end_x, end_y, maze2)