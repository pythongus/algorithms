"""
l=3,2,3,1,1
i  pos  nl
3  0    3
2       2,3
3       2,3,3
1       1,2,3,3
1       1,2,3,3,1

p  c    len(heap) nl

1  3    5         1,2,3,3,1


"""
from math import log
from operator import gt, lt


def heapify(heap, min_heap=True):
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
    _ = [_sift_down(index) for index in range(len(heap))]
    return heap


def parent_position(pos):
    """Calculates the parent position given the current one, pos.
    Adds an error epsilon, so floating point precision is addressed
    by calculations.
    """
    epsilon = 0.001
    if pos == 0:
        return pos
    n = log(pos) / log(2)
    return round(2 ** (n - 1) - 1 + epsilon)

