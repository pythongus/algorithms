"""
Grid for the game of life
"""
from algo.gol import EMPTY


class Grid:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = [[EMPTY] * self.width for _ in range(self.height)]

    def query(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def assign(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

    def __str__(self):
        return "\n".join(["".join(row) for row in self.rows])
