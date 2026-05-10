import pygame
from queue import PriorityQueue
import math
import time

# --- Configuration & Colors ---
WIDTH, HEIGHT = 900, 680 # Slightly taller for winner display
GRID_SIZE = 600
ROWS = 30
SIDEBAR_WIDTH = WIDTH - GRID_SIZE

# Professional Color Palette
WHITE      = (255, 255, 255)
BLACK      = (30, 30, 30)
BLUE       = (0, 122, 204)
RED        = (231, 76, 60)
GREEN      = (46, 204, 113)
ORANGE     = (230, 126, 34)
PURPLE     = (155, 89, 182)
GREY       = (189, 195, 199)
DARK_GREY  = (52, 73, 94)
UI_BG      = (236, 240, 241)
ACCENT     = (41, 128, 185)
GOLD       = (255, 215, 0) # For the winner

pygame.init()
FONT_S = pygame.font.SysFont('Segoe UI', 14)
FONT_M = pygame.font.SysFont('Segoe UI', 16)
FONT_B = pygame.font.SysFont('Segoe UI', 18, bold=True)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Advanced Analytics Lab - Final Week 7")

HEURISTICS = ["Manhattan", "Euclidean", "Octile"]
current_heuristic = 0
history = {"Manhattan": "-", "Euclidean": "-", "Octile": "-"}

# Global metrics
current_nodes = 0
current_cost = 0
current_time = 0
current_status = "Idle"

class Button:
    def __init__(self, x, y, width, height, text, color, active_color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.active_color = active_color if active_color else color
        self.is_active = False
        self.is_hovered = False

    def draw(self, win):
        draw_color = self.active_color if (self.is_active or self.is_hovered) else self.color
        pygame.draw.rect(win, (150, 150, 150), (self.rect.x+2, self.rect.y+2, self.rect.width, self.rect.height), border_radius=5)
        pygame.draw.rect(win, draw_color, self.rect, border_radius=5)
        pygame.draw.rect(win, DARK_GREY, self.rect, 2, border_radius=5)
        text_surf = FONT_M.render(self.text, True, WHITE if draw_color != GREY else BLACK)
        win.blit(text_surf, (self.rect.x + (self.rect.width - text_surf.get_width())//2, 
                             self.rect.y + (self.rect.height - text_surf.get_height())//2))

    def update_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

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
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for d in directions:
            r, c = self.row + d[0], self.col + d[1]
            if 0 <= r < ROWS and 0 <= c < ROWS and not grid[r][c].is_barrier():
                cost = 1 if (d[0] == 0 or d[1] == 0) else 1.414
                self.neighbors.append((grid[r][c], cost))

def heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx, dy = abs(x1 - x2), abs(y1 - y2)
    if HEURISTICS[current_heuristic] == "Manhattan": return dx + dy
    if HEURISTICS[current_heuristic] == "Euclidean": return math.sqrt(dx**2 + dy**2)
    if HEURISTICS[current_heuristic] == "Octile": return max(dx, dy) + (math.sqrt(2) - 1) * min(dx, dy)

def a_star(draw_fn, grid, start, end):
    global current_nodes, current_cost, current_time, current_status
    start_time = time.time()
    count = 0
    current_nodes = 0
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
        current_nodes += 1

        if current == end:
            while current in came_from:
                current = came_from[current]
                if current != start: current.make_path()
                draw_fn()
            end.make_end()
            current_time = round((time.time() - start_time) * 1000, 2)
            current_cost = g_score[end]
            current_status = "PATH FOUND!"
            return current_nodes

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
        
        current_status = "Searching..."
        current_cost = g_score[current]
        draw_fn()
        if current != start: current.make_closed()
        
    current_status = "NO PATH FOUND"
    return -1

def draw_window(win, grid, buttons):
    win.fill(WHITE)
    for row in grid:
        for spot in row: spot.draw(win)
    
    gap = GRID_SIZE // ROWS
    for i in range(ROWS + 1):
        pygame.draw.line(win, GREY, (0, i * gap), (GRID_SIZE, i * gap))
        pygame.draw.line(win, GREY, (i * gap, 0), (i * gap, GRID_SIZE))

    # --- SIDEBAR UI ---
    pygame.draw.rect(win, UI_BG, (GRID_SIZE, 0, SIDEBAR_WIDTH, HEIGHT))
    pygame.draw.line(win, DARK_GREY, (GRID_SIZE, 0), (GRID_SIZE, HEIGHT), 3)
    win.blit(FONT_B.render("A* PERFORMANCE LAB", True, BLACK), (GRID_SIZE + 25, 20))

    for btn in buttons: btn.draw(win)

    # --- LIVE METRICS ---
    metrics_y = 330
    pygame.draw.rect(win, WHITE, (GRID_SIZE + 15, metrics_y, SIDEBAR_WIDTH - 30, 110), border_radius=8)
    pygame.draw.rect(win, ACCENT, (GRID_SIZE + 15, metrics_y, SIDEBAR_WIDTH - 30, 110), 2, border_radius=8)
    
    win.blit(FONT_B.render("LIVE METRICS", True, ACCENT), (GRID_SIZE + 25, metrics_y + 10))
    st_color = GREEN if "PATH FOUND" == current_status else (RED if "NO" in current_status else BLACK)
    win.blit(FONT_M.render(f"Status: {current_status}", True, st_color), (GRID_SIZE + 25, metrics_y + 35))
    win.blit(FONT_M.render(f"Nodes Explored: {current_nodes}", True, BLACK), (GRID_SIZE + 25, metrics_y + 55))
    win.blit(FONT_M.render(f"Time: {current_time} ms", True, BLACK), (GRID_SIZE + 25, metrics_y + 75))

    # --- EFFICIENCY ANALYSIS (THE WOW FACTOR) ---
    table_y = 460
    win.blit(FONT_B.render("HEURISTIC COMPARISON", True, BLACK), (GRID_SIZE + 25, table_y))
    
    valid_results = {k: v for k, v in history.items() if isinstance(v, int)}
    winner = min(valid_results, key=valid_results.get) if valid_results else None

    for i, h_name in enumerate(HEURISTICS):
        val = history[h_name]
        is_winner = (h_name == winner)
        
        # Highlighting logic
        bg_col = (255, 249, 210) if is_winner else WHITE
        row_rect = pygame.Rect(GRID_SIZE + 20, table_y + 30 + (i * 35), SIDEBAR_WIDTH - 40, 30)
        pygame.draw.rect(win, bg_col, row_rect, border_radius=5)
        if is_winner: pygame.draw.rect(win, GOLD, row_rect, 2, border_radius=5)

        h_text = FONT_M.render(f"{h_name}:", True, BLACK)
        v_text = FONT_M.render(f"{val} nodes", True, DARK_GREY if not is_winner else GREEN)
        win.blit(h_text, (row_rect.x + 10, row_rect.y + 5))
        win.blit(v_text, (row_rect.x + 100, row_rect.y + 5))
        if is_winner:
            win.blit(FONT_S.render("★ MOST EFFICIENT", True, ORANGE), (row_rect.x + 100, row_rect.y + 20))

    if winner:
        pygame.draw.rect(win, GREEN, (GRID_SIZE + 15, 610, SIDEBAR_WIDTH - 30, 40), border_radius=8)
        msg = FONT_B.render(f"BEST: {winner.upper()}", True, WHITE)
        win.blit(msg, (GRID_SIZE + 50, 620))

    pygame.display.update()

def main():
    global current_heuristic, history, current_nodes, current_cost, current_time, current_status
    grid = make_grid()
    start, end = grid[5][5], grid[25][25]
    start.make_start(); end.make_end()

    buttons = [
        Button(625, 70, 120, 35, "Manhattan", GREY, ACCENT),
        Button(625, 110, 120, 35, "Euclidean", GREY, ACCENT),
        Button(625, 150, 120, 35, "Octile", GREY, ACCENT),
        Button(625, 205, 250, 45, "SOLVE MAZE", DARK_GREY, GREEN),
        Button(625, 260, 250, 45, "CLEAR BOARD", DARK_GREY, RED)
    ]
    buttons[current_heuristic].is_active = True

    run = True
    while run:
        draw_window(WIN, grid, buttons)
        m_pos = pygame.mouse.get_pos()
        for btn in buttons: btn.update_hover(m_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False

            if pygame.mouse.get_pressed()[0]:
                if m_pos[0] < GRID_SIZE:
                    row, col = m_pos[1] // (GRID_SIZE // ROWS), m_pos[0] // (GRID_SIZE // ROWS)
                    grid[row][col].make_barrier() if grid[row][col] not in [start, end] else None
                else:
                    for i, btn in enumerate(buttons[:3]):
                        if btn.is_clicked(m_pos):
                            for b in buttons[:3]: b.is_active = False
                            btn.is_active = True
                            current_heuristic = i
                    
                    if buttons[3].is_clicked(m_pos): # Solve
                        for row in grid:
                            for spot in row:
                                if spot.color in [BLUE, RED, GREEN]: spot.reset()
                                spot.update_neighbors(grid)
                        res = a_star(lambda: draw_window(WIN, grid, buttons), grid, start, end)
                        if res != -1: history[HEURISTICS[current_heuristic]] = res

                    if buttons[4].is_clicked(m_pos): # Clear
                        grid = make_grid()
                        start, end = grid[5][5], grid[25][25]
                        start.make_start(); end.make_end()
                        current_nodes, current_time, current_status = 0, 0, "Idle"
                        history = {h: "-" for h in HEURISTICS} # Resetting history too on Clear

            if pygame.mouse.get_pressed()[2]: # Right click erase
                if m_pos[0] < GRID_SIZE:
                    row, col = m_pos[1] // (GRID_SIZE // ROWS), m_pos[0] // (GRID_SIZE // ROWS)
                    grid[row][col].reset()

    pygame.quit()

def make_grid():
    return [[Spot(i, j, GRID_SIZE // ROWS) for j in range(ROWS)] for i in range(ROWS)]

if __name__ == "__main__":
    main()