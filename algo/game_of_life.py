"""
Game Of Life, With Coroutines
"""
from collections import namedtuple, deque
from random import choices


Query = namedtuple('Query', ('y', 'x'))
Transition = namedtuple('Transition', ('y', 'x', 'state'))
ALIVE = '*'
EMPTY = '-'
TICK = object()


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
    if state == ALIVE and not neighbours in [2, 3]:
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


class ColumnPrinter:

    def __init__(self):
        self.columns = []

    def append(self, grid):
        self.columns.append(grid)

    def __str__(self):
        return "|".join([f"{i}\n{col}" for i, col in enumerate(self.columns)])

    def __repr__(self):
        return self.__str__


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
    assert isinstance(t1, Transition)

    print(f"Me:{'' * 4}: {q0}")


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
