from algo.heap_sort import parent_position


def test_parent_position_0():
    assert parent_position(0) == 0


def test_parent_position_1():
    assert parent_position(1) == 0


def test_parent_position_2():
    assert parent_position(2) == 0


def test_parent_position_3_to_6():
    assert parent_position(3) == 1
    assert parent_position(4) == 1
    assert parent_position(5) == 2
    assert parent_position(6) == 2
