"""
Binet's Formula For Fibonacci Sequence

"""

from algo.binet import fibonacci


def test_fibonnaci():
    result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i in range(10):
        assert fibonacci(i) == result[i]
