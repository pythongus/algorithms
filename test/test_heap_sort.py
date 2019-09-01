import pytest
from algo.heap_sort import heapify, parent_position, sort


def test_max_heap_with_10_elements():
    heap = heapify(list(range(10, 0, -1)), min_heap=False)
    assert heap == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def test_sort_1():
    array = [4, 6, 7, 1, 3, 6]
    sort(array)
    assert  array == sorted(array)


def test_sort_with_10_elements():
    heap = heapify(list(range(10, -1, -1)), min_heap=False)
    sort(heap)
    assert heap == list(range(11))


@pytest.mark.skip
def test_sort_with_10_000_elements():
    big_number = 10_000
    heap = heapify(list(range(big_number, -1, -1)), min_heap=False)
    sort(heap)
    assert heap == list(range(big_number + 1))
