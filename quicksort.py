import random


def qSort(array):
    if len(array) <= 1:
        return array
    if len(array) == 2:
        if array[0] > array[1]:
            return array[::-1]
        return array
    pivot = random.choice(array)
    arrmin = []
    arrmax = []
    for x in array:
        if x <= pivot:
            arrmin.append(x)
        else:
            arrmax.append(x)

    qSort(arrmin)
    qSort(arrmax)

    return arrmin+arrmax


def qselect(array, k, pivot_fn):
    pivot = pivot_fn(array)
    lesser = []
    greater = []
    for x in array:
        if x <= pivot:
            lesser.append(x)
        else:
            greater.append(x)
    if len(lesser) >= len(greater):
        return qselect(lesser, k, pivot_fn)
    else:
        return qselect(greater, k-len(lesser)+1, pivot_fn)

print(qSort([5, 2, 3, 9, 4, 7, 13]))
