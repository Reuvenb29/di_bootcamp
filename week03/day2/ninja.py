import time
import os

class GameOfLife:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.grid:
            print(' '.join(['■' if cell else '□' for cell in row]))
        print("\n")

    def count_neighbors(self, row, col):
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),         (0,1),
                      (1,-1), (1,0), (1,1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                count += self.grid[r][c]
        return count

    def step(self):
        next_grid = [[0]*self.cols for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                live_neighbors = self.count_neighbors(r, c)
                if self.grid[r][c] == 1:
                    if live_neighbors in [2, 3]:
                        next_grid[r][c] = 1
                else:
                    if live_neighbors == 3:
                        next_grid[r][c] = 1
        self.grid = next_grid

    def run(self, generations=10, delay=0.5):
        for _ in range(generations):
            self.display()
            self.step()
            time.sleep(delay)

if __name__ == "__main__":
    # Example starting grid
    initial_grid = [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    game = GameOfLife(initial_grid)
    game.run(generations=20, delay=0.3)