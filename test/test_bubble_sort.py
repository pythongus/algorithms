from algo.bubble_sort import sort


def test_sort():
    assert sort([4, 6, 1, 3, 2]) == [1, 2, 3, 4, 6]
