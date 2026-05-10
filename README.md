[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MIT Licence](https://img.shields.io/badge/licence-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![A* Pathfinding](https://img.shields.io/badge/Algorithm-A%2a%20Search-orange?style=for-the-badge)](https://en.wikipedia.org/wiki/A*_search_algorithm)
# Shortest-Path-Maze-Finder
A comprehensive AI pathfinding system implementing A*, BFS, and DFS algorithms to solve dynamic mazes with various heuristic optimizations.

## 📍 Table of Contents
* [🔬 Overview](#-overview)
* [🚀 Setup & Installation](#-setup--installation)
* [✨ Key Features](#-key-features)
* [📁 Project Structure](#-project-structure)
* [📊 Performance Benchmarks](#-performance-benchmarks)
* [📜 Publication & Reports](#-publication--reports)
* [⚕️ Disclaimer](#-disclaimer)

## 📁 The Architecture Diagram
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





## 📁Setup & Installation


Follow these steps to get the environment ready and run the pathfinding system on your local machine.

### 📋 Prerequisites

Before installation, ensure you have the following installed:
* **Python 3.10** or higher 🐍
* **pip** (Python package manager)
* A virtual environment (recommended)

### 🛠️ Installation Steps

1. **Clone the Repository**
   First, clone the project from GitHub and navigate into the project directory:
   ```bash
   git clone [https://github.com/YourUsername/Shortest-Path-Maze-Finder.git](https://github.com/YourUsername/Shortest-Path-Maze-Finder.git)
   cd Shortest-Path-Maze-Finder
Create a Virtual Environment (Optional but Recommended) 
Keeping your dependencies isolated is a best practice:

Bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
Install Dependencies 
Install the required libraries (Pygame, NumPy) using the provided requirements file:

Bash
pip install -r requirements.txt
Launch the Application 
Run the main entry point to start the GUI and interact with the pathfinder:

Bash

python main.py

[!IMPORTANT]

 GPU Acceleration: While the algorithms run on the CPU, ensure your graphics drivers are up to date for the best performance with the Pygame visualization.

💻 Usage Instructions
Once the application is running, you can interact with the grid using your keyboard and mouse:

Left Click: Place start/end nodes or draw obstacles.

Right Click: Erase nodes or obstacles.

Spacebar: Begin the A* Pathfinding search.

'C' Key: Clear the entire grid to start over.

'R' Key: Reset the path while keeping the obstacles.
pygame
numpy


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



