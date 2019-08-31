from algo.heap_sort import insert


def test_insert_nothing():
    heap = insert([], [])
    assert heap == []


def test_insert_no_element():
    heap = insert([1], [])
    assert heap == [1]


def test_insert_1_element():
    heap = insert([], [1])
    assert heap == [1]


def test_insert_2_elements():
    heap = insert([], [1, 2])
    assert heap == [1, 2]


def test_insert_2_elements_reverse():
    heap = insert([], [2, 1])
    assert heap == [1, 2]


def test_insert_2_equal_elements():
    heap = insert([], [2, 2])
    assert heap == [2, 2]


def test_insert_3_elements_1():
    heap = insert([], [1, 2, 3])
    assert heap == [1, 2, 3]


def test_insert_3_elements_2():
    heap = insert([], [2, 1, 3])
    assert heap == [1, 2, 3]


def test_insert_3_elements_3():
    heap = insert([], [3, 2, 1])
    assert heap == [1, 3, 2]
