import pytest
from algo.heap_sort import insert, parent_position


def test_insert_7_elements_1():
    heap = insert([], [6, 5, 4, 3, 2, 1, 0])
    assert heap == [0, 3, 1, 6, 4, 5, 2]


def test_insert_1_element_in_existing_heap_1():
    heap = insert([0, 3, 1, 6, 4, 5], [2])
    assert heap == [0, 3, 1, 6, 4, 5, 2]


def test_insert_1_element_in_existing_heap_2():
    heap = insert([2, 4, 5], [3])
    assert heap == [2, 3, 5, 4]


@pytest.mark.milli
def test_insert_1000_elements_in_reverse_order():
    heap = insert([], range(1000, -1, -1))
    element = heap[500]
    assert heap[parent_position(element)] < element


def testparent_position_0():
    assert parent_position(0) == 0


def testparent_position_1():
    assert parent_position(1) == 0


def testparent_position_2():
    assert parent_position(2) == 0


def testparent_position_3_to_6():
    assert parent_position(3) == 1
    assert parent_position(4) == 1
    assert parent_position(5) == 2
    assert parent_position(6) == 2
