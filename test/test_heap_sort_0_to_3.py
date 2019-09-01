from algo.heap_sort import heapify


def test_heapify_nothing():
    heap = heapify([])
    assert heap == []


def test_heapify_1_element():
    heap = heapify([1])
    assert heap == [1]


def test_heapify_2_elements():
    heap = heapify([1, 2])
    assert heap == [1, 2]


def test_heapify_2_elements_reverse():
    heap = heapify([2, 1])
    assert heap == [1, 2]


def test_heapify_2_equal_elements():
    heap = heapify([2, 2])
    assert heap == [2, 2]


def test_heapify_3_elements_1():
    heap = heapify([1, 2, 3])
    assert heap == [1, 2, 3]


def test_heapify_3_elements_2():
    heap = heapify([2, 1, 3])
    assert heap == [1, 2, 3]


def test_heapify_3_elements_3():
    heap = heapify([3, 2, 1])
    assert heap == [1, 3, 2]
