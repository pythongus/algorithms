import pytest
from algo.heap_sort import heapify, parent_position


def test_max_heap_with_10_elements():
    heap = heapify(list(range(10, 0, -1)), min_heap=False)
    assert heap == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
