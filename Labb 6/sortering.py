from songClassFile import *
import timeit


"""
number = 10
n:                  1000        10 000      100 000         1 000 000
Urvalssortering:   0.4901s     49.5334s      *5000s         *500000 (ca 40h)
Quicksort:         0.0129s      0.1811s      2.7452s          33.6877s
* (ungefärlig) beräknad tid

Urvalssortering har O(n^2)  ==>     T(n) = k * n^2
Quicksort har O(nlog(n))    ==>     T(n) = k * nlog(n)
"""


# taget från canvas föreläsning 8

def urvalssort(data):
    n = len(data)
    for i in range(n):
        low = i
        for j in range(i+1, n):
            if data[j] < data[low]:
                low = j
        data[low], data[i] = data[i], data[low]


# taget från cavnas föreläsning 8

def quicksort(data):
    sista = len(data) - 1
    qsort(data, 0, sista)


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


def main():
    n = int(input('Ange antal element: '))
    print('Antal element =', n)

    data = track_list[:n]

    urvalstid = timeit.timeit(stmt=lambda: urvalssort(data), number=10)
    print(f'Urvalssortering tog {round(urvalstid, 4)} sekunder att sortera {n} element.')

    quicktid = timeit.timeit(stmt=lambda: quicksort(data), number=10)
    print(f'Quicksort tog {round(quicktid, 4)} sekunder att sortera {n} element.')


if __name__ == '__main__':
    main()


"""
Tidskomplexiteten för de algoritmer vi använt verkar stämma överens med teorin. Vid jämgörelse av
beräknad körtid och faktiskt körtid har vi sett att de stämmer hyffsat överrens.

"""
