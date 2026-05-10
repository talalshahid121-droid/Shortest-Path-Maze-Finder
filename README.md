[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MIT Licence](https://img.shields.io/badge/licence-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![A* Pathfinding](https://img.shields.io/badge/Algorithm-A%2a%20Search-orange?style=for-the-badge)](https://en.wikipedia.org/wiki/A*_search_algorithm)

# Shortest-Path-Maze-Finder
A comprehensive AI pathfinding system implementing A*, BFS, and DFS algorithms to solve dynamic mazes with various heuristic optimizations.

## 📍 Table of Contents
* [🔬 Overview](#-overview)
* [📁 Setup & Installation](#-setup--installation)
* [✨ Key Features](#-key-features)
* [📁 Project Structure](#-project-structure)
* [📊 Performance Benchmarks](#-performance-benchmarks)
* [📜 Publication & Reports](#-publication--reports)
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
