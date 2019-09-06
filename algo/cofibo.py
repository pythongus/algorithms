"""
Fibonacci Using Coroutines

Using the previously yielded value, calculates the following one.
Stops if the current element is greater or equal to 1e100

Simulation
----------
cur  prev  ele
-    -     -
-    1     1
1    1     1
1    1     2
"""


def fibonacci():
    """Yields the next value of the Fibonacci sequence,
    given the previous one.
    """
    yield 0
    element = yield 1
    previous = element
    while element < 1e100:
        current = yield element
        element = previous + current
        if current > 1:
            previous = current

    return element
