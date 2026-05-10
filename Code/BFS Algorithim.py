import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import time

# Directions: up, down, left, right
directions = [(-1,0),(1,0),(0,-1),(0,1)]

# Generate a random maze
def generate_maze(size):
    maze = np.random.choice([0,1], size=(size,size), p=[0.7,0.3])
    maze[0][0] = 0          # Start
    maze[size-1][size-1] = 0 # Goal
    return maze

# BFS function (your logic)
def bfs(maze, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {}
    nodes_explored = []

    while queue:
        current = queue.popleft()
        nodes_explored.append(current)  # store explored nodes

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

    return path, nodes_explored

# Main program
size = 10  # maze size
maze = generate_maze(size)
start = (0,0)
goal = (size-1,size-1)

# Measure execution time
start_time = time.time()
path, explored_nodes = bfs(maze, start, goal)
end_time = time.time()
execution_time = end_time - start_time

print("Execution Time:", execution_time, "seconds")

# Visualization of maze
fig, ax = plt.subplots()
ax.imshow(maze, cmap='binary')  # 0=white(path),1=black(wall)

# Highlight explored nodes in yellow
for node in explored_nodes:
    ax.plot(node[1], node[0], 'yo')  # y=column, x=row

# Highlight final path in green line
path_rows = [node[0] for node in path]
path_cols = [node[1] for node in path]
ax.plot(path_cols, path_rows, 'g-', linewidth=2)  # line connecting path

# Highlight start and goal
ax.plot(start[1], start[0], 'bs', markersize=8, label='Start')  # blue square
ax.plot(goal[1], goal[0], 'ms', markersize=8, label='Goal')     # purple square

ax.set_title(f"BFS Maze Solver (Time: {execution_time:.4f}s)")
ax.legend()
plt.show()

# Optional: Time vs Maze Size graph
sizes = [10, 15, 20, 25, 30]
times = []

for s in sizes:
    maze = generate_maze(s)
    start = (0,0)
    goal = (s-1,s-1)
    t0 = time.time()
    bfs(maze, start, goal)
    t1 = time.time()
    times.append(t1-t0)

plt.plot(sizes, times, marker='o')
plt.xlabel("Maze Size (NxN)")
plt.ylabel("Time (seconds)")
plt.title("BFS Execution Time vs Maze Size")
plt.show()