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
