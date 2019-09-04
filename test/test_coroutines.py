"""
Unit Test For Coroutines.
"""


def simple(message):
    print(message)
    while message != 'END':
        message = yield 
        print(f"Message: {message}")

    return f'Final message should be {message}'


def power_of_2():
    number = yield
    while number > 0:
        number = yield 2 ** number

    return number


def test_simple():
    smpl = simple("First message")
    next(smpl)
    smpl.send("One more")
    smpl.send("Another one")
    try:
        smpl.send("END")
    except StopIteration as sie:
        message = sie.value
    finally:
        assert message == 'Final message should be END'


def test_power_of_2():
    pow2 = power_of_2()
    next(pow2)
    assert [pow2.send(1), pow2.send(2)] == [2, 4]
    try:
        pow2.send(-1)
    except StopIteration as sie:
        message = sie.value
    else:
        print('No StopIteration exception raised')
    finally:
        assert message == -1


def test_accumulator():
    pass
