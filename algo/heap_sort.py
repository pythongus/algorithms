"""
l=3,2,3,1,1
i  pos  nl
3  0    3
2       2,3
3       2,3,3
1       1,2,3,3
1       1,2,3,3,1

p  c    len(heap) nl

1  3    5         1,2,3,3,1


"""
def insert(heap, elements):
    """Inserts the elements in the heap."""

    def _new(pos):
        for elem in elements:
            if heap and elem < heap[pos]:
                heap[pos], elem = elem, heap[pos]
            heap.append(elem)

    def _rearrange():
        ppos, cpos = next(counter), next(counter)
        while cpos < len(heap):
            for i in range(ppos, cpos):
                end = min(i * 2 + 2, len(heap))
                for j in range(cpos, end):
                    if heap[i] > heap[j]:
                        heap[i], heap[j] = heap[j], heap[i]
            ppos, cpos = next(counter), next(counter)

    if not (heap or elements) or not elements:
        return heap

    counter = range2(0, 2 ** (len(elements) + len(heap) + 1), 2)
    _new(next(counter))
    _rearrange()
    return heap

def range2(start, stop, step=1):
    """Returns the elements in the range start up to stop,
    moving step ** count, with count starting at zero.
    """
    num = start
    count = 0
    while num < stop and step > 0:
        yield num
        num = num + step ** count
        count += 1
