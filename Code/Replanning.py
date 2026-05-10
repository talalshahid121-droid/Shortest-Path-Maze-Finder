import pygame
from queue import PriorityQueue
import math

# Initialize Pygame and Font
pygame.init()
FONT = pygame.font.SysFont('Arial', 16)
BOLD_FONT = pygame.font.SysFont('Arial', 18, bold=True)

WIDTH = 600
ROWS = 30
# Extra height for the legend and instructions
UI_HEIGHT = 100 
WIN = pygame.display.set_mode((WIDTH, WIDTH + UI_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)      # Path
RED = (255, 100, 100)    # Explored (Closed)
GREEN = (100, 255, 100)  # Frontier (Open)
ORANGE = (255, 165, 0)   # Start
PURPLE = (128, 0, 128)   # End
GREY = (128, 128, 128)
UI_BG = (240, 240, 240)

# Heuristic Modes
HEURISTICS = ["Manhattan", "Euclidean", "Octile"]
current_heuristic = 0

class Spot:
    def __init__(self, row, col, width):
        self.row, self.col = row, col
        self.x, self.y = col * width, row * width
        self.color = WHITE
        self.neighbors = []
        self.width = width

    def get_pos(self): return self.row, self.col
    def is_barrier(self): return self.color == BLACK
    def reset(self): self.color = WHITE
    def make_start(self): self.color = ORANGE
    def make_end(self): self.color = PURPLE
    def make_barrier(self): self.color = BLACK
    def make_path(self): self.color = BLUE
    def make_closed(self): self.color = RED
    def make_open(self): self.color = GREEN

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        # 8-direction movement
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for d in directions:
            r, c = self.row + d[0], self.col + d[1]
            if 0 <= r < ROWS and 0 <= c < ROWS and not grid[r][c].is_barrier():
                # Cost is 1 for straight, 1.4 for diagonal (handled in A* g_score)
                cost = 1 if (d[0] == 0 or d[1] == 0) else 1.414
                self.neighbors.append((grid[r][c], cost))

def heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx, dy = abs(x1 - x2), abs(y1 - y2)
    if HEURISTICS[current_heuristic] == "Manhattan":
        return dx + dy
    elif HEURISTICS[current_heuristic] == "Euclidean":
        return math.sqrt(dx**2 + dy**2)
    elif HEURISTICS[current_heuristic] == "Octile":
        return max(dx, dy) + (math.sqrt(2) - 1) * min(dx, dy)

def reconstruct_path(came_from, current, draw_fn):
    while current in came_from:
        current = came_from[current]
        if current.color != ORANGE:
            current.make_path()
        draw_fn()

def a_star(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}; g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}; f_score[start] = heuristic(start.get_pos(), end.get_pos())
    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor, cost in current.neighbors:
            temp_g = g_score[current] + cost
            if temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score[neighbor] = temp_g + heuristic(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    if neighbor != end: neighbor.make_open()

        draw()
        if current != start: current.make_closed()
    return False

def make_grid():
    return [[Spot(i, j, WIDTH // ROWS) for j in range(ROWS)] for i in range(ROWS)]

def draw(win, grid):
    win.fill(WHITE)
    for row in grid:
        for spot in row: spot.draw(win)
    
    gap = WIDTH // ROWS
    for i in range(ROWS):
        pygame.draw.line(win, GREY, (0, i * gap), (WIDTH, i * gap))
        pygame.draw.line(win, GREY, (i * gap, 0), (i * gap, WIDTH))
    
    # UI Area
    pygame.draw.rect(win, UI_BG, (0, WIDTH, WIDTH, UI_HEIGHT))
    
    # Current Search Mode
    h_text = BOLD_FONT.render(f"MODE: {HEURISTICS[current_heuristic]}", True, BLACK)
    win.blit(h_text, (20, WIDTH + 10))

    # Legend Rendering
    legend_data = [
        (ORANGE, "Start"), (PURPLE, "End"), (BLACK, "Wall"),
        (RED, "Explored"), (GREEN, "Frontier"), (BLUE, "Path")
    ]
    
    for i, (color, label) in enumerate(legend_data):
        x_pos = 20 + (i % 3) * 120
        y_pos = WIDTH + 40 if i < 3 else WIDTH + 60
        pygame.draw.rect(win, color, (x_pos, y_pos, 15, 15))
        win.blit(FONT.render(label, True, BLACK), (x_pos + 20, y_pos - 2))

    # Instructions
    instr = FONT.render("[SPACE] Run   [C] Mode   [R] Reset Maze", True, (50, 50, 50))
    win.blit(instr, (WIDTH - 280, WIDTH + 10))

    pygame.display.update()

def clear_search_visuals(grid):
    for row in grid:
        for spot in row:
            if spot.color in [BLUE, RED, GREEN]: spot.reset()

def main():
    global current_heuristic
    grid = make_grid()
    start, end = grid[2][2], grid[25][25]
    start.make_start(); end.make_end()
    run = True
    
    while run:
        draw(WIN, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if pos[1] < WIDTH:
                    row, col = pos[1] // (WIDTH // ROWS), pos[0] // (WIDTH // ROWS)
                    spot = grid[row][col]
                    if spot != start and spot != end: spot.make_barrier()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    clear_search_visuals(grid)
                    for row in grid:
                        for spot in row: spot.update_neighbors(grid)
                    a_star(lambda: draw(WIN, grid), grid, start, end)
                if event.key == pygame.K_c:
                    current_heuristic = (current_heuristic + 1) % 3
                    clear_search_visuals(grid)
                if event.key == pygame.K_r:
                    grid = make_grid()
                    start, end = grid[2][2], grid[25][25]
                    start.make_start(); end.make_end()
    pygame.quit()

if __name__ == "__main__":
    main()