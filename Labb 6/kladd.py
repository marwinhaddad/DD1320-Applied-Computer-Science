
def quicksort(data):
    right = len(data) - 1
    left = 0
    return _quicksort(data, left, right)


def _quicksort(data, left, right):
    index_pivot = (left+right)//2
    # flytta pivot till kanten
    data[index_pivot], data[right] = data[right], data[index_pivot]

    # damerna först med avseende på pivotdata
    pivotmid = partition(data, left, right, data[right])

    # flytta tillbaka pivot
    data[pivotmid], data[right] = data[right], data[pivotmid]

    if pivotmid - left > 1:
        _quicksort(data, left, pivotmid-1)
    if right - pivotmid > 1:
        _quicksort(data, pivotmid+1, right)
    return data


def partition(data, left, right, pivot):
    while True:
        right -= 1
        while data[left] < pivot:
            left += 1
        while right > 0 and data[right] > pivot:
            right -= 1
        data[left], data[right] = data[right], data[left]
        print(data)
        if left >= right:
            break

    data[left], data[right] = data[right], data[left]
    print(data)
    return left


def quacksort(data):
    sista = len(data) - 1
    return qsort(data, 0, sista)


def qsort(data, low, high):
    pivotindex = (low+high)//2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]

    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low-1, high, data[high])

    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]

    if pivotmid-low > 1:
        qsort(data, low, pivotmid-1)
    if high-pivotmid > 1:
        qsort(data, pivotmid+1, high)
    return data


def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and data[h] > pivot:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h:
            break
    data[v], data[h] = data[h], data[v]
    return v


print(quicksort([3, 7, 10, 8, 4, 1, 5, 9, 6, 2]))
# lista = [65, 28, 90, 72, 37, 93, 46, 25, 44, 25, 76,
#          94, 42, 51, 56, 42, 19, 97, 35, 80, 18, 27,
#          79, 42, 61, 62, 78, 65, 89, 24, 78, 34, 97,
#          34, 12, 52, 89, 9, 50, 17, 59, 51, 25, 34,
#          4, 28, 35, 95, 44, 69, 45, 4, 55, 28, 49,
#          61, 1, 40, 60, 69, 85, 60, 75, 27, 24, 94,
#          18, 48, 2, 88, 82, 73, 51, 88, 42, 8, 7,
#          98, 44, 25, 98, 50, 13, 85, 38, 20, 81,
#          10, 79, 60, 45, 85, 64, 67, 53, 84, 28, 3, 76, 76]
# print(quacksort(lista) == quicksort(lista))
# print(quicksort(lista))





