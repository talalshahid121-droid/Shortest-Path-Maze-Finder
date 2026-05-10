[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MIT Licence](https://img.shields.io/badge/licence-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![A* Pathfinding](https://img.shields.io/badge/Algorithm-A%2a%20Search-orange?style=for-the-badge)](https://en.wikipedia.org/wiki/A*_search_algorithm)
# Shortest-Path-Maze-Finder
A comprehensive AI pathfinding system implementing A*, BFS, and DFS algorithms to solve dynamic mazes with various heuristic optimizations.

## 📁 Project Structure

```text
Shortest-Path-Maze-Finder/
│
├── src/                        # Core AI Algorithms
│   ├── astar.py                # A* Implementation (Week 3)
│   ├── search.py               # BFS & DFS Baselines (Week 2)
│   └── heuristics.py           # Manhattan, Euclidean, Octile (Week 4)
│
├── gui/                        # Week 7 - Pygame Interface
│   └── app.py                  # Main entry point
│
├── data/                       # Dataset & Benchmarks
│   ├── performance_data.csv    # Results from Week 4/8
│   └── visuals/                # Bar charts and tables
│
├── publication/                # Week 8 - IEEE Research Paper
│   └── report.pdf
│
└── README.md                   # Project Overview
