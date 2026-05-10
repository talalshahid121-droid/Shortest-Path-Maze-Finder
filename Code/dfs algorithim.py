import numpy as np
import matplotlib.pyplot as plt
import time

# Directions: up, down, left, right
directions = [(-1,0),(1,0),(0,-1),(0,1)]

# Generate random maze
def generate_maze(size):
    maze = np.random.choice([0,1], size=(size,size), p=[0.7,0.3])
    maze[0][0] = 0
    maze[size-1][size-1] = 0
    return maze

# DFS function using stack
def dfs(maze, start, goal):
    stack = [start]
    visited = set([start])
    parent = {}
    nodes_explored = []

    while stack:
        current = stack.pop()
        nodes_explored.append(current)  # track explored nodes

        if current == goal:
            break

        # Explore neighbors in random order for more "DFS-like" traversal
        np.random.shuffle(directions)
        for d in directions:
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
    while node in parent:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()

    return path, nodes_explored

# --- Main Program ---
size = 40   # Increase maze size for measurable time
maze = generate_maze(size)
start = (0,0)
goal = (size-1,size-1)

# Measure execution time
start_time = time.time()
path, explored_nodes = dfs(maze, start, goal)
end_time = time.time()
execution_time = end_time - start_time

print(f"DFS Execution Time: {execution_time:.6f} seconds")

# --- Visualization ---
fig, ax = plt.subplots()
ax.imshow(maze, cmap='binary')  # 0=white(path),1=black(wall)

# Explored nodes in yellow
for node in explored_nodes:
    ax.plot(node[1], node[0], 'yo')  # y=column, x=row

# Final path in green line
path_rows = [node[0] for node in path]
path_cols = [node[1] for node in path]
ax.plot(path_cols, path_rows, 'g-', linewidth=2)

# Start and Goal
ax.plot(start[1], start[0], 'bs', markersize=8, label='Start')
ax.plot(goal[1], goal[0], 'ms', markersize=8, label='Goal')

ax.set_title(f"DFS Maze Solver (Time: {execution_time:.6f}s)")
ax.legend()
plt.show()
sizes = [10, 20, 30, 40, 50]  # different maze sizes
times = []

for s in sizes:
    maze = generate_maze(s)
    start = (0,0)
    goal = (s-1,s-1)
    t0 = time.time()
    dfs(maze, start, goal)  # run DFS
    t1 = time.time()
    times.append(t1 - t0)

# Plot graph
plt.figure()
plt.plot(sizes, times, marker='o', color='b')
plt.xlabel("Maze Size (NxN)")
plt.ylabel("Time (seconds)")
plt.title("DFS Execution Time vs Maze Size")
plt.show()