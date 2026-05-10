import heapq
import random
import math
import time
import matplotlib.pyplot as plt
import numpy as np

random.seed(42)
np.random.seed(42)

# --------------------------
# Heuristic Functions
# --------------------------

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def euclidean(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def octile(a, b):
    dx = abs(a[0]-b[0])
    dy = abs(a[1]-b[1])
    return max(dx,dy) + (math.sqrt(2)-1)*min(dx,dy)


# --------------------------
# Maze Generator
# --------------------------

def generate_maze(rows, cols, density):

    maze = np.zeros((rows,cols))

    for i in range(rows):
        for j in range(cols):

            if random.random() < density:
                maze[i][j] = 1

    maze[0][0] = 0
    maze[rows-1][cols-1] = 0

    return maze


# --------------------------
# Neighbor Finder
# --------------------------
def get_neighbors(node, grid, diag):
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    if diag:
        directions += [(1,1),(1,-1),(-1,1),(-1,-1)]

    neighbors = []

    for d in directions:
        nx = node[0] + d[0]
        ny = node[1] + d[1]

        if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
            if grid[nx][ny] == 0:
                
                # çapraz mı düz mü kontrolü
                if abs(d[0]) == 1 and abs(d[1]) == 1:
                  # corner cutting kontrolü
                    if grid[node[0] + d[0]][node[1]] == 1 or grid[node[0]][node[1] + d[1]] == 1:
                        continue

                    move_cost = math.sqrt(2)

                else:
                    move_cost = 1

                neighbors.append(((nx, ny), move_cost))

    return neighbors


# --------------------------
# A* Algorithm
# --------------------------

def astar(grid,start,goal,heuristic,diag):

    open_list = []
    heapq.heappush(open_list,(0,start))

    came_from = {}
    g_score = {start:0}

    nodes_explored = 0

    start_time = time.perf_counter()   # high precision timer

    while open_list:

        current = heapq.heappop(open_list)[1]

        nodes_explored += 1

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            runtime = time.perf_counter() - start_time

            return path, nodes_explored, runtime, g_score[goal]


        for neighbor, move_cost in get_neighbors(current,grid,diag):

            tentative_g = g_score[current] + move_cost

            if neighbor not in g_score or tentative_g < g_score[neighbor]:

                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                f = tentative_g + heuristic(neighbor,goal)

                heapq.heappush(open_list,(f,neighbor))

    runtime = time.perf_counter() - start_time
    return None, nodes_explored, runtime, None


# --------------------------
# Maze Visualization
# --------------------------

def show_maze(grid, path, start, goal, title):

    display = np.copy(grid)

    if path:
        for p in path:
            display[p] = 0.5

    display[start] = 0.8
    display[goal] = 0.9

    plt.figure(figsize=(5,5))
    plt.imshow(display, cmap="viridis")
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
    plt.show()


# --------------------------
# Comparison Graph
# --------------------------

def compare_results(results):

    names = [r[0] for r in results]
    runtime = [r[3] for r in results]

    best = names[runtime.index(min(runtime))]

    plt.figure(figsize=(7,4))

    plt.bar(names,runtime)

    plt.title(f"Heuristic Runtime Comparison\nMost Efficient: {best}")
    plt.xlabel("Heuristic")
    plt.ylabel("Runtime (milliseconds)")

    for i,v in enumerate(runtime):
        plt.text(i,v+0.001,f"{v:.3f}",ha='center')

    plt.show()


def compare_nodes(results):
    names = [r[0] for r in results]
    nodes = [r[2] for r in results]

    plt.bar(names, nodes)
    plt.title("Nodes Explored Comparison")
    plt.xlabel("Heuristic")
    plt.ylabel("Nodes Explored")
    plt.show()
# --------------------------
# MAIN PROGRAM
# --------------------------

if __name__ == "__main__":

    sizes = [20, 50, 100]
    density = 0.25

    heuristics = {
        "Manhattan": (manhattan, True),
        "Euclidean": (euclidean, True),
        "Octile": (octile, True)
    }

    for size in sizes:

        rows = size
        cols = size

        print("\n=======================")
        print("A* Pathfinding Demo")
        print("=======================\n")
        print("Maze Size:", rows, "x", cols)

        maze = generate_maze(rows, cols, density)

        start = (0, 0)
        goal = (rows - 1, cols - 1)

        results = []

        for name, (func, diag) in heuristics.items():

            path, nodes, runtime, path_cost = astar(maze, start, goal, func, diag)
            runtime_ms = runtime * 1000

            print("Heuristic:", name)

            if path:
                print("Path Cost:", round(path_cost, 4))
                print("Path Length:", len(path))
                print("Nodes Explored:", nodes)
                print("Runtime:", round(runtime_ms, 4), "ms\n")

                show_maze(
                    maze,
                    path,
                    start,
                    goal,
                    f"{name} A* Result ({size}x{size})"
                )
            else:
                print("No Path Found\n")

            results.append((name, path_cost if path else 0, nodes, runtime_ms))

        compare_nodes(results)
        compare_results(results)