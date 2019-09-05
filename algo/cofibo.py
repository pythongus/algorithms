"""
res  sec  prev
0    -    -

"""
def fibonacci():
    result = 0
    while result  < 1e50:
        second = yield result
        if second in (0, 1):
            previous = 1
        result = previous + second
        if second > 1:
            previous = second

    return result
