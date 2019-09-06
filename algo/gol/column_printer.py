"""
Column Printer for the Game Of Life
"""


class ColumnPrinter:

    def __init__(self):
        self.columns = []

    def append(self, grid):
        self.columns.append(grid)

    def __str__(self):
        return "|".join([f"{i}\n{col}" for i, col in enumerate(self.columns)])

    def __repr__(self):
        return self.__str__
