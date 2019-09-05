"""
Unit Test For Coroutines.
"""
from algo.coroutines import simple, power_of_2

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


def test_power_of_2_list():
    pow2 = power_of_2()
    next(pow2)
    results = []
    try:
        results.extend([pow2.send(n) for n in range(0, 10)])
    except StopIteration as sie:
        message = sie.value
    else:
        print('No StopIteration exception raised')
    finally:
        assert results[9] == 2 ** 9


def test_accumulator():
    pass
