"""
Game Of Life, With Coroutines
"""
from collections import deque
from algo.gol.grid import Grid
from algo.gol import Query, Transition, ALIVE, EMPTY, TICK


def count_neighbours(y, x):
    """Count the ALIVE neighbour cells from the given coordinates y and x,
    after receiving its state from the environment.
    """
    i_coords = deque([1, 1, 0, -1, -1, -1, 0, 1])
    j_coords = i_coords.copy()
    j_coords.rotate(2)
    i_j = tuple(zip(i_coords, j_coords))
    queries = [Query(y + i, x + j) for i, j in i_j]
    states = ["n_", "ne", "e_", "se", "s_", "sw", "w_", "nw"]
    neighbour_states = dict(zip(states, queries))
    count = 0
    for name, query in neighbour_states.items():
        state = yield query
        if state == ALIVE:
            count += 1

    return count


def game_logic(state, neighbours):
    if state == ALIVE and neighbours not in [2, 3]:
        return EMPTY
    elif neighbours == 3:
        return ALIVE

    return state


def step_cell(y, x):
    state = yield Query(y, x)
    neighbours = yield from count_neighbours(y, x)
    next_state = game_logic(state, neighbours)
    yield Transition(y, x, next_state)


def simulate(height, width):
    while True:
        for y in range(height):
            for x in range(width):
                yield from step_cell(y, y)
        yield TICK


def live_a_generation(grid, sim):
    progeny = Grid(grid.height, grid.width)
    item = next(sim)
    while item is not TICK:
        if isinstance(item, Query):
            state = grid.query(item.y, item.x)
            item = sim.send(state)
        else:
            progeny.assign(item.y, item.x, item.state)
            item = next(sim)
    return progeny
