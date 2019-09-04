"""Minimum Moves

A maze solver, calculating the weighted shortest path between two points.
"""
from collections import deque


def minMoves(maze, x, y):
    """ Shortest path in a n x m graph (maze), with finish in coordinates
    x and y.

    Node definition:
    - 0 free
    - 1 blocked
    - 2 free with a coin
    """

    def maze_guard():
        """Guard function to block oversized dimensions"""
        cell_guard = all([1 <= len(row) <= 100 for row in maze])
        row_guard = 1 <= len(maze) <= 100
        return cell_guard and row_guard

    def walk_maze(finish):
        """Walks the maze, finding the shortest path including all coins.
        Finishes when reach the coordenate finish, a tuple with row and
        column numbers
        """
        i, j = (0, 0)
        result = -1
        weight = -1
        while nodes:
            i, j, path, coins = nodes.popleft()
            cell = maze[i][j]
            if (i, j) == finish:
                weight, result = check_result(coins, path, weight, result)
            elif cell != 1:
                adjacent_nodes(i, j, path, coins)

        return result

    def adjacent_nodes(i, j, path, coins):
        """Adds the node in positions i, j, with its path added to
        accumulated path. The path is transformed into a binary
        number, i.e, 2 ** (i * n + j), being n the number of rows
        in the maze matrix.
        """
        def neighbour(x, y):
            this_path = 2 ** (i * n + j)
            if not this_path & path:
                coin = coins + 1 if maze[i][j] == 2 else coins
                nodes.append((x, y, path + this_path, coin))

        coord = [(i + 1, j, i + 1 < n), (i - 1, j, i - 1 >= 0),
                 (i, j + 1, j + 1 < m), (i, j - 1, j - 1 >= 0)]
        _ = [neighbour(x, y) for x, y, test in coord if test]

    if not maze_guard():
        return -1

    n = len(maze)
    m = len(maze[0])
    nodes = deque([(0, 0, 0, 0)])
    return walk_maze((x, y))


def check_result(coins, path, previous_weight, result):
    """Checks the current result with a weighted value of
    coins and the path. Once path is read from the binary
    form, the formula is *coins + 1/path_count*.
    """
    pcount = path_count(path)
    weight = coins + 1 / pcount
    if weight > previous_weight:
        return weight, pcount
    return previous_weight, result


def path_count(path):
    """Counts the nodes in the path by checking the binary number."""

    def x_is_contained_in_y(bin_num):
        x_and_y = bin_num & path == bin_num
        x_or_y = bin_num | path == path
        x_and_y_complement = bin_num & (-path - 1) == 0
        return x_and_y and x_or_y and x_and_y_complement

    return sum([x_is_contained_in_y(bin_num) for bin_num in pow2(path)])


def pow2(limit):
    """Generator for binary numbers, i.e., 2 ** n, up to the limit."""
    i = 0
    bin_num = 1
    while bin_num <= limit:
        yield bin_num
        i += 1
        bin_num = 2 ** i
