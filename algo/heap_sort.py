"""
Heap Sort Algorithm
"""
from math import log2
from operator import gt, lt


def sort(array):
    for i in range(len(array), 0, -1):
        heapify(array, i, min_heap=False)
        array[0], array[i - 1] = array[i - 1], array[0]


def heapify(heap, limit=None, min_heap=True):
    """Inserts the elements in the heap."""

    def _sift_down(index):
        pos = index
        parent = parent_position(pos)
        while parent >= 0 and oper(heap[pos], heap[parent]):
            heap[parent], heap[pos] = heap[pos], heap[parent]
            pos = parent
            parent = parent_position(parent)

    if not heap:
        return heap

    oper = lt if min_heap else gt
    _ = [_sift_down(index) for index in range(limit if limit else len(heap))]
    return heap


def parent_position(pos):
    """Calculates the parent position given the current one, pos.
    Adds an error epsilon, so floating point precision is addressed
    by calculations.
    """
    epsilon = 0.001
    if pos == 0:
        return pos
    return round(2 ** (log2(pos) - 1) - 1 + epsilon)
