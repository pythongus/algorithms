"""
Coroutines Examples
"""


def simple(message):
    """A simple message printing function"""
    print(message)
    while message != 'END':
        message = yield 
        print(f"Message: {message}")

    return f'Final message should be {message}'


def power_of_2():
    """Calculates the power of 2 of a given number"""
    number = yield
    while number >= 0:
        number = yield 2 ** number

    return number


def power_of_2_no_yielding(number):
    """Power of 2"""
    return 2 ** number
