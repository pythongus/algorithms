"""
Game Of Life, With Coroutines
"""
from collections import namedtuple


Query = namedtuple('Query', ('y', 'x'))
Transition = namedtuple('Transition', ('y', 'x', 'state'))
ALIVE = '*'
EMPTY = '-'
TICK = object()
