from algo.heap_sort import heapify


def test_heapify_4_elements_1():
    heap = heapify([3, 4, 2, 1])
    assert heap == [1, 2, 3, 4]


def test_heapify_4_elements_2():
    heap = heapify([3, 4, 4, 1])
    assert heap == [1, 3, 4, 4]


def test_heapify_4_elements_3():
    heap = heapify([3, 3, 3, 3])
    assert heap == [3, 3, 3, 3]


def test_heapify_5_elements_1():
    heap = heapify([3, 2, 1, 5, 4])
    assert heap == [1, 3, 2, 5, 4]


def test_heapify_5_elements_2():
    heap = heapify([3, 2, 3, 1, 1])
    assert heap == [1, 1, 3, 3, 2]


def test_heapify_6_elements_1():
    heap = heapify([3, 2, 4, 1, 5, 0])
    assert heap == [0, 2, 1, 3, 5, 4]


def test_heapify_6_elements_2():
    heap = heapify([0, 2, 1, 4, 5, 3])
    assert heap == [0, 2, 1, 4, 5, 3]


def test_heapify_6_elements_3():
    heap = heapify([5, 4, 3, 2, 1, 0])
    assert heap == [0, 2, 1, 5, 3, 4]
