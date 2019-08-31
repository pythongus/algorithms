import pytest
from algo.heap_sort import insert


def test_insert_7_elements_1():
    heap = insert([], [6, 5, 4, 3, 2, 1, 0])
    assert heap == [0, 4, 1, 6, 5, 3, 2]
