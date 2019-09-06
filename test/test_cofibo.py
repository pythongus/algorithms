"""
Unit Test For Fibonacci With Coroutines
"""
from algo.cofibo import fibonacci
from algo import binet


def test_cofibo():
    fib = fibonacci()
    rs = next(fib)
    fib_list = [rs]
    try:
        for i in range(10000):
            rs = fib.send(rs)
            fib_list.append(rs)
    except StopIteration as e:
        fib_list.append(e.value)

    last = fib_list[-1]
    last_binet = binet.fibonacci(len(fib_list) - 1)
    assert abs(last - last_binet) / last < 1e-10
