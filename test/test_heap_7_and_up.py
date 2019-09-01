from algo.heap_sort import heapify, parent_position


def test_heapify_7_elements_1():
    heap = heapify([6, 5, 4, 3, 2, 1, 0])
    assert heap == [0, 3, 1, 6, 4, 5, 2]


def test_heapify_1_element_in_existing_heap_1():
    heap = heapify([0, 2, 3, 1, 6, 4, 5])
    assert heap == [0, 1, 3, 2, 6, 4, 5]


def test_heapify_1_element_in_existing_heap_2():
    heap = heapify([2, 4, 5, 3])
    assert heap == [2, 3, 5, 4]


def test_heapify_1000_elements_in_reverse_order():
    heap = heapify(list(range(1000, -1, -1)))
    elem_pos = heap[9]
    par_pos = parent_position(9)
    while par_pos > 0:
        assert heap[elem_pos] > heap[par_pos]
        elem_pos = par_pos
        par_pos = parent_position(elem_pos)
