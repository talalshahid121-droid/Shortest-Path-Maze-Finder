import pygame
from queue import PriorityQueue

# Window setup
WIDTH = 600
ROWS = 30
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Pathfinding Visualization (Press SPACE)")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)       # closed set
GREEN = (0, 255, 0)     # open set
BLUE = (0, 0, 255)      # path
ORANGE = (255, 165, 0)  # start
PURPLE = (128, 0, 128)  # end
GREY = (200, 200, 200)

class Spot:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = col * width   # FIXED
        self.y = row * width   # FIXED
        self.color = WHITE
        self.neighbors = []
        self.width = width

    def get_pos(self):
        return self.row, self.col

    def is_barrier(self):
        return self.color == BLACK

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = PURPLE

    def make_path(self):
        self.color = BLUE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []

        # Down
        if self.row < ROWS - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        # Up
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        # Right
        if self.col < ROWS - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        # Left
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])


# Heuristic (Manhattan)
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def a_star(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))

    came_from = {}

    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g = g_score[current] + 1

            if temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score[neighbor] = temp_g + h(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()
        pygame.time.delay(20)  # Smooth animation

        if current != start:
            current.make_closed()

    return False


def make_grid(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap)
            grid[i].append(spot)

    return grid


def draw_grid(win):
    gap = WIDTH // ROWS
    for i in range(ROWS):
        pygame.draw.line(win, GREY, (0, i * gap), (WIDTH, i * gap))
        pygame.draw.line(win, GREY, (i * gap, 0), (i * gap, WIDTH))


def draw(win, grid):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win)
    pygame.display.update()


def main(win):
    grid = make_grid(ROWS, WIDTH)

    start = grid[2][2]
    end = grid[25][25]

    start.make_start()
    end.make_end()

    # Obstacles
    for i in range(5, 20):
        grid[i][10].make_barrier()

    for row in grid:
        for spot in row:
            spot.update_neighbors(grid)

    run = True
    started = False

    while run:
        draw(win, grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if not started:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        started = True
                        a_star(lambda: draw(win, grid), grid, start, end)

    pygame.quit()


main(WIN)