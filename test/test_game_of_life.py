"""
Unit Testing For Game Of Life.

A coroutine experiment.
"""
from algo.gol.game_of_life import (
        step_cell,
        live_a_generation,
        simulate,
        count_neighbours,
        )
from algo.gol.grid import Grid
from algo.gol.column_printer import ColumnPrinter
from random import choices
from algo.gol import ALIVE, EMPTY, Transition


def test_step_cell():
    it = step_cell(10, 5)
    q0 = next(it)
    q1 = it.send(ALIVE)
    q2 = it.send(ALIVE)
    q3 = it.send(ALIVE)
    q4 = it.send(ALIVE)
    q5 = it.send(ALIVE)
    q6 = it.send(ALIVE)
    q7 = it.send(ALIVE)
    q8 = it.send(EMPTY)
    t1 = it.send(EMPTY)
    print(f"Me:{'' * 4}: {q0}")
    assert isinstance(t1, Transition)


def test_grid():
    grid = Grid(5, 9)
    grid.assign(0, 3, ALIVE)
    grid.assign(0, 2, ALIVE)
    grid.assign(1, 2, ALIVE)
    grid.assign(0, 0, ALIVE)
    live_a_generation(grid, simulate(grid.height, grid.width))
    print(grid)


def test_column_printer():
    columns = ColumnPrinter()
    grid = Grid(5, 9)
    grid.assign(0, 3, ALIVE)
    grid.assign(0, 2, ALIVE)
    grid.assign(1, 1, ALIVE)
    grid.assign(0, 0, ALIVE)
    sim = simulate(grid.height, grid.width)
    for i in range(5):
        columns.append(str(grid))
        grid = live_a_generation(grid, sim)

    print(columns)
    assert True


def test_count_neighbours():

    def _state():
        return choices([ALIVE, EMPTY], [.7, .3]).pop()

    from random import seed
    seed(12783)
    it = count_neighbours(10, 5)
    qs = [next(it)]
    qs.extend([it.send(_state()) for _ in range(7)])
    try:
        it.send(_state())
    except StopIteration as e:
        count = e.value

    assert count == 6
