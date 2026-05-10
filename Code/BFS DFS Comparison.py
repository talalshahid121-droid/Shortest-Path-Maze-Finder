import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import time

# Directions (Up, Down, Left, Right)
directions = [(-1,0),(1,0),(0,-1),(0,1)]

# -------- Maze Generator --------
def generate_maze(size):
    maze = np.random.choice([0,1], size=(size,size), p=[0.7,0.3])
    maze[0][0] = 0
    maze[size-1][size-1] = 0
    return maze


# -------- BFS Algorithm --------
def bfs(maze,start,goal):

    queue = deque([start])
    visited = set([start])
    parent = {}
    explored = []

    while queue:

        current = queue.popleft()
        explored.append(current)

        if current == goal:
            break

        for d in directions:

            r = current[0] + d[0]
            c = current[1] + d[1]

            if 0 <= r < len(maze) and 0 <= c < len(maze):

                if maze[r][c] == 0 and (r,c) not in visited:

                    queue.append((r,c))
                    visited.add((r,c))
                    parent[(r,c)] = current

    # Reconstruct path
    path = []
    node = goal

    while node in parent:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()

    return path, explored


# -------- DFS Algorithm --------
def dfs(maze,start,goal):

    stack = [start]
    visited = set([start])
    parent = {}
    explored = []

    while stack:

        current = stack.pop()
        explored.append(current)

        if current == goal:
            break

        dirs = directions.copy()
        np.random.shuffle(dirs)

        for d in dirs:

            r = current[0] + d[0]
            c = current[1] + d[1]

            if 0 <= r < len(maze) and 0 <= c < len(maze):

                if maze[r][c] == 0 and (r,c) not in visited:

                    stack.append((r,c))
                    visited.add((r,c))
                    parent[(r,c)] = current

    # Reconstruct path
    path = []
    node = goal

    if node not in parent:
        return [], explored

    while node in parent:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()

    return path, explored


# -------- Main Program --------
size = 30
maze = generate_maze(size)

start = (0,0)
goal = (size-1,size-1)

# BFS Execution
start_time = time.time()
bfs_path, bfs_explored = bfs(maze,start,goal)
bfs_time = time.time() - start_time

# DFS Execution
start_time = time.time()
dfs_path, dfs_explored = dfs(maze,start,goal)
dfs_time = time.time() - start_time

print("BFS Time:", bfs_time)
print("DFS Time:", dfs_time)


# -------- Maze Visualization --------

plt.figure(figsize=(8,8))
plt.imshow(maze, cmap='binary')

# BFS explored nodes (Yellow)
for node in bfs_explored:
    plt.plot(node[1], node[0], 'yo', alpha=0.3)

# DFS explored nodes (Cyan)
for node in dfs_explored:
    plt.plot(node[1], node[0], 'co', alpha=0.3)

# BFS Path (Green)
if bfs_path:
    plt.plot([n[1] for n in bfs_path],
             [n[0] for n in bfs_path],
             'g-', linewidth=2, label="BFS Path")

# DFS Path (Red)
if dfs_path:
    plt.plot([n[1] for n in dfs_path],
             [n[0] for n in dfs_path],
             'r-', linewidth=2, label="DFS Path")

# Start and Goal
plt.plot(start[1], start[0], 'bs', label="Start")
plt.plot(goal[1], goal[0], 'ms', label="Goal")

plt.title("Maze Solver BFS vs DFS")
plt.legend()

plt.show()


# -------- Performance Comparison Graph --------

sizes = [10,20,30,40,50]

bfs_times = []
dfs_times = []

for s in sizes:

    maze = generate_maze(s)
    start = (0,0)
    goal = (s-1,s-1)

    start_time = time.time()
    bfs(maze,start,goal)
    bfs_times.append(time.time()-start_time)

    start_time = time.time()
    dfs(maze,start,goal)
    dfs_times.append(time.time()-start_time)

plt.figure(figsize=(8,6))

plt.plot(sizes,bfs_times,marker='o',label="BFS")
plt.plot(sizes,dfs_times,marker='o',label="DFS")

plt.xlabel("Maze Size")
plt.ylabel("Execution Time (seconds)")
plt.title("BFS vs DFS Performance Comparison")

plt.legend()
plt.grid()

plt.show()