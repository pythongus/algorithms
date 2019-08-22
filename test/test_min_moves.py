"""MinMoves Unit Test

Unit test module for min_moves (shortest path) algorithm
"""
import os
import unittest
from algo.min_moves import minMoves
import random


class TestMinMoves(unittest.TestCase):

    def assert_test(self, maze, finish, expected):
        result = minMoves(maze, *finish)
        self.assertEqual(expected, result)

    def test_min_moves_maze_guard_rows(self):
        maze = [(0, 2, 0) for _ in range(101)]
        x = 0; y = 0
        self.assert_test(maze, (x, y), -1)

    def test_min_moves_maze_guard_cols(self):
        maze = [tuple([0 for _ in range(101)]) for _ in range(10)]
        x = 0; y = 0
        self.assert_test(maze, (x, y), -1)

    def test_min_moves_dead_start(self):
        maze = [(0, 1, 0), (1, 0, 1), (1, 1, 1)]
        x = 1; y = 1
        self.assert_test(maze, (x, y), -1)

    def test_min_moves_3x3_0(self):
        maze = [(0, 2, 0), (0, 0, 1), (1, 1, 1)]
        x = 1; y = 1
        self.assert_test(maze, (x, y), 2)

    def test_min_moves_3x3_1(self):
        maze = [(0, 1, 0), (1, 0, 1), (0, 2, 2)]
        x = 1; y = 1
        self.assert_test(maze, (x, y), -1)

    def test_min_moves_3x3_2(self):
        maze = [(0, 2, 0), (1, 1, 2), (1, 0, 0)]
        x = 2; y = 1
        self.assert_test(maze, (x, y), 5)

    def test_min_moves_5x5(self):
        random.seed(16752)
        n = 5
        array = random.choices([0, 1, 2], [.6, .3, .1], k=n ** 2)
        maze = [[elem for elem in array[start:start + n]] for start in range(0, n ** 2, n)]
        x = 4; y = 1;
        self.assert_test(maze, (x, y), 5)

    def test_min_moves_7x7(self):
        random.seed(16673)
        n = 7
        array = random.choices([0, 1, 2], [.8, .1, .1], k=n ** 2)
        maze = [[elem for elem in array[start:start + n]] for start in range(0, n ** 2, n)]
        x = 6; y = 6;
        self.assert_test(maze, (x, y), 14)

    @unittest.skipUnless(os.environ.get("bigmaze", None), "Skipping due to long execution time")
    def test_min_moves_8x8(self):
        random.seed(16573)
        n = 8
        array = random.choices([0, 1, 2], [.8, .1, .1], k=n ** 2)
        maze = [[elem for elem in array[start:start + n]] for start in range(0, n ** 2, n)]
        x = 6; y = 6;
        self.assert_test(maze, (x, y), 16)


if __name__ == "__main__":
    unittest.main()
