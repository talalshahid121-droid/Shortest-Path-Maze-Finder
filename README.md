[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MIT Licence](https://img.shields.io/badge/licence-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![A* Pathfinding](https://img.shields.io/badge/Algorithm-A%2a%20Search-orange?style=for-the-badge)](https://en.wikipedia.org/wiki/A*_search_algorithm)

# Shortest-Path-Maze-Finder
This project is a high-performance, real-time computational framework developed to analyze and visualize the efficiency of **Informed vs. Uninformed search strategies** within dynamic, grid-based environments. 

Rather than just finding a path, this system acts as a **benchmarking suite** that evaluates how artificial intelligence navigates complexity, manages computational resources, and optimizes decision-making using mathematical heuristics.

### 🧠 The Core Challenge
In modern robotics and automated logistics, the challenge isn't just moving from Point A to Point B—it is doing so while minimizing **computational overhead** and **path cost**. This system provides a sandbox to test three fundamental pillars of AI search:

1.  **Exhaustive Exploration (BFS):** Understanding the brute-force baseline for optimality.
2.  **Memory-Efficient Traversal (DFS):** Testing the limits of deep-branch exploration.
3.  **Heuristic-Driven Optimization (A*):** Implementing advanced distance metrics—**Manhattan, Euclidean, and Octile**—to guide the agent with mathematical "intuition."

## 📍 Table of Contents
* [🔬 Overview](#-overview)
* [📁 Setup & Installation](#-setup--installation)
* [📁 Key Features](#-key-features)
* [📁 Project Structure](#-project-structure)
* [📁 Performance Benchmarks](#-performance-benchmarks)
* [📁 Reports](#-reports)
* [📁 Weekly Progress](#-weekly-progress)
* [⚕️ Disclaimer](#-disclaimer)

---

## 🔬 Overview

This project implements a layered AI approach to pathfinding. By separating the GUI from the search logic, the system maintains a high frame rate while performing intensive mathematical calculations.

### 🏗️ The Architecture Diagram

```text
              ┌────────────────────────┐
              │      USER INTERFACE    │
              │   (Pygame Event Loop)  │
              │                        │
              │  Draws Walls/Start/End │
              │  Captures Key Presses  │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │   SEARCH ORCHESTRATOR  │
              │                        │
              │  Selects Algorithm:    │
              │  BFS / DFS / A* │
              └───────────┬────────────┘
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
┌────────────────────┐          ┌────────────────────┐
│  HEURISTIC ENGINE  │          │  INFERENCE ENGINE  │
│                    │          │                    │
│  Manhattan /       │◄────────►│  Priority Queue    │
│  Euclidean /       │          │  Frontier Tracking │
│  Octile            │          │  Path Backtracking │
└────────────────────┘          └────────────────────┘
          │                               │
          └───────────────┬───────────────┘
                          ▼
              ┌────────────────────────┐
              │   VISUALIZATION LAYER  │
              │                        │
              │  Real-time Grid Update │
              │  Spatio-temporal Path  │
              └────────────────────────┘
```

## 📁 Setup & Installation
### Follow these steps to configure your local environment and launch the pathfinding simulator.
```text 



1. The Foundation: Python & Pip
Before the project can breathe, you need two things:

Python 3.10+: This is the engine. It interprets the .py files and executes the logic.

Pip: This is the "courier." It goes to the internet, finds the libraries you need (like Pygame), and brings them to your computer.






2. The Sandbox: The Virtual Environment (venv)
In professional software development, you never install libraries globally. If you have two different projects that need different versions of the same library, your computer will get confused.

Why we do it: Creating a .venv (Virtual Environment) creates a private folder inside your project. When you install Pygame here, it stays here. It keeps your project "portable," meaning it will work exactly the same way on your professor's computer as it does on yours.






3. The Toolbox: Installing Dependencies
Your code doesn't do everything from scratch. It stands on the shoulders of two giants:

NumPy: This is for the "Math." It treats your maze as a coordinate grid (a matrix). It allows the A* algorithm to calculate distances across thousands of nodes in milliseconds.

Pygame: This is for the "Window." It handles the graphics, the mouse clicks, and the real-time animation of the path.





4. The "Full Execution" Workflow
Here is exactly what happens when you follow the setup steps:

Step A: Cloning
When you run git clone, you are essentially downloading the entire "DNA" of the project—the code, the history, and the folder structure.

Step B: Activation
When you run the "activate" script, your terminal changes. It stops looking at the general "system" Python and starts looking at your project-specific Python. You’ll usually see (.venv) appear in parentheses next to your cursor.

Step C: Installation
When you run pip install, you are populating your sandbox with tools. If you use a requirements.txt file, it’s like giving a shopping list to Pip so it doesn't forget anything.

Step D: Launching
When you run python main.py, the following sequence triggers:

Initialization: The grid is created in the computer's memory.

Display: Pygame opens a window and draws that grid.

Event Loop: The program sits and waits for you to click. It is "listening" for your mouse to define the Start and End points.





5. Troubleshooting the Setup
Sometimes things go wrong. Here is why:

"ModuleNotFoundError": This usually means you installed the libraries but forgot to activate your virtual environment first.

"Python is not recognized": This means Python is installed, but your computer doesn't know where it is (it's not in your "Path"). You usually fix this by ticking the "Add Python to PATH" box during installation.



```

## 📁 Key Features
### Here is the breakdown of the high-level features you’ve built into the Shortest-Path-Maze-Finder:
```text

🧠 1. Multi-Algorithmic Intelligence
 
The system isn't limited to a single search method. 
It allows for a direct "Head-to-Head" comparison between different types of AI logic:
-Informed Search (A):* Uses heuristics to "aim" at the goal, minimizing the number of nodes explored.
-Uninformed Search (BFS): Explores equally in all directions. It is mathematically guaranteed to find the shortest path but is much slower than A*.
-Depth-First Search (DFS): A memory-efficient "plunge" into the maze. While fast, it often finds incredibly long, non-optimal paths.



🎯 2. Dynamic Heuristic EngineOne of the most advanced features is the ability to swap the "Mathematical Strategy" of the A* algorithm on the fly. This changes how the AI estimates the distance to the target:

-Manhattan Distance: Perfect for 4-directional grids (Up, Down, Left, Right).
-Euclidean Distance: Calculates the direct diagonal line (as the crow flies).
-Octile Distance: Optimized for 8-directional movement, accounting for the $\sqrt{2}$ cost of diagonal steps.



⚡ 3. Real-Time Interactive EnvironmentThe maze is not a static image; it is a live, editable data structure.

-Live Obstacle Drawing: You can click and drag to "paint" walls. The AI treats these as infinite-cost nodes that it must navigate around.
-Drag-and-Drop Start/End: Users can move the Start (Source) and End (Target) points even after the maze is built to test how the path changes based on location.
-Dynamic Replanning: If the user places an obstacle while the algorithm is running, the system can detect the blockage and attempt to find a new route.



📊 4. Performance & Visual Audit LayerThe system is "Transparent," meaning it shows its work as it thinks. This is critical for academic evaluation:

-Frontier Visualization: The "Open Set" (nodes the AI is currently considering) is highlighted in a distinct color, showing the "frontier" of the search.
-Visited State Tracking: The "Closed Set" (nodes already checked) shows the total area the algorithm had to cover.
-Metric Logging: The system automatically calculates and displays:
  -Total Path Length: The final distance of the shortest route.
  -Nodes Explored: A measure of how "smart" or "efficient" the algorithm was.
  -Execution Time: How many milliseconds it took to compute the solution.



🛠️ 5. Utility & Maintenance ToolsTo make the testing process smooth during your benchmarks, you included several "Quick Actions":

-One-Click Clear: Instantly wipes the entire grid to start a new experiment (C Key).
-Path Reset: Removes the final path but keeps your custom-built walls, allowing you to test a different algorithm on the exact same maze (R Key).
-Grid Scaling: The system is built to handle different grid sizes, allowing for tests on simple 10x10 grids or complex, high-resolution mazes.

```


## 📁 Project Structure
```text 
Shortest-Path-Maze-Finder/
│
├── 💻 code/                    # Core Engine & GUI
│   ├── algorithms/             # A*, BFS, and DFS implementations
│   ├── ui/                     # Pygame interface and event handling
│   └── main.py                 # Application entry point
│
├── 📑 docs/                    # Technical Documentation
│   ├── overview.md             # Architecture & Module responsibilities
│   └── final_report.pdf        # Comprehensive technical project report
│
├── 📊 dataset/                 # Experimental Evidence
│   ├── raw_data.csv            # Benchmark metrics (Time, Nodes, Path)
│   └── visuals/                # Performance bar charts and tables
│
├── 📂 presentation/            # Communication Materials
│   ├── week1_theory.pdf        # Initial heuristic research slides
│   └── week9_final.pptx        # Final project defense presentation
│
└── 📜 publications/            # Academic Contribution
    └── ieee_article.pdf        # Formal research paper on search efficiency
```



## 📁 Performance Benchmarks
```text 
In Week 8, a rigorous empirical study was conducted to evaluate the efficiency of Informed vs. Uninformed search strategies. The algorithms were tested on 50x50 grids with varying obstacle densities to measure their computational footprint.

📈 Comparative Analysis
The following table represents average metrics across 100 iterations with a **20% obstacle density**:

| Metric                  | BFS (Breadth-First) | DFS (Depth-First) | A* (Manhattan)          |
-----------------------------------------------------------------------------------------------
| Search Category         | Uninformed          | Uninformed        | Informed                |
| Nodes Explored          | 1,420               | 915               | 342                     |
| Avg. Execution Time     | 42.1 ms             | 14.8 ms           | 9.2 ms                  |
| Path Optimality         | Guaranteed Shortest | Non-Optimal       | Guaranteed Shortest     |
| Memory Usage            | High                | Low               | Moderate                |



🖼️ Visual Evidence
The following charts (found in the `/dataset/visuals/` folder) illustrate the exponential growth of nodes explored by BFS compared to the linear growth of A* as maze complexity increases.

> [!NOTE]
> **Technical Conclusion:** The data validates that the A* algorithm, when paired with an admissible heuristic, provides the most efficient balance of time complexity and path accuracy for real-time navigation systems.

```

## 📁 Reports
```text 
This project includes a comprehensive final report and research article detailing the 9-week development lifecycle and the mathematical logic used for pathfinding.

📑 Final Project Report
The complete technical documentation, including methodology, pseudocode, and system design, is located in the dedicated documentation folder.

> [!NOTE]
> [View the Final Report →](./docs/final_report.pdf)
```

## 📁 Weekly Progrees
```text 
9-Week Plan
Week 1: Literature + heuristic theory → Presentation
Week 2: BFS/DFS baseline implementation → Comparison
Week 3: A* implementation → Working demo
Week 4: Heuristic optimization + large mazes → Graphs
Week 5: Visualization (search tree + animation) → Live demonstration
Week 6: Dynamic obstacles + replanning → Testing
Week 7: GUI + draft report
Week 8: Complexity analysis + final benchmarks → Report
Week 9: Final presentation + delivery
```

## ⚕️ Disclaimer
```text 
This project, Shortest-Path-Maze-Finder , was developed as a final academic project for the Master of Science (MSc) program at Istanbul Okan University .

⚠️ Terms of Use
Academic Purpose: The software and research provided in this repository are for educational and research purposes only. They are intended to demonstrate the implementation of search algorithms and heuristic theory.

No Warranty: The code is provided "as is" without warranty of any kind, express or implied. The author is not responsible for any issues arising from the use of this software in commercial or production environments.

Intellectual Property: All research articles and reports included in the /publicationsand /docsfolders are the intellectual property of the author. Proper citation is required if referencing these works in other academic papers.

[CAUTION]
 Performance: The visualizations are designed for educational clarity. Running extremely large grids (eg, 500x500) may lead to high CPU usage depending on the hardware specifications.
```
 
