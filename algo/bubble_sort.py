counter = 0



def sort(array):
    global counter
    for i in range(0, len(array) - 1):
        counter += 1; 
        for j in range(i + 1, len(array)):
            counter += 1; 
            if array[j] < array[i]:
                counter += 1; 
                swap(array, j, i)
    return array


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]
