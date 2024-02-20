from songClassFile import *
import timeit

"""
number = 10 000
n:                      250 000         500 000         1 000 000       
Linjärsökning:          174.579s        341.3407s       670.4868s
Binärsökning:           0.1174s         0.1245s         0.1465s
Hashsökning:            0.0018s         0.0016s         0.0016s

Linjärsökning är O(n)      ==>     T(n) = k * n
Binärsökning är O(log2(n)) ==>     T(n) = k * log2(n)
Hashsökning är O(1)        ==>     T(n) = k

Vi söker efter element som inte existerar i listan för att kunna jämföra längsta tänkbara söktid.
"""

def linsok(the_list, key):
    for element in the_list:
        if element.låttitel == key:
            return True
    return False

def binsok(the_list, key):
    first = 0
    last = len(the_list) - 1
    while first <= last:
        mid = (first + last)//2
        if the_list[mid] == key:
            return True
        else:
            if key < the_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False

def hashsok(the_list, key):
    if key in the_list:
        return True
    return False

def sokning():
    n = int(input('Ange antal element: '))
    print("Antal element =", n)

    # wanted element
    searchkey_lin = 'SongTitle'
    searchkey_bin = Song(['TrackId', 'TrackTime', 'Artist', 'SongTitle'])
    searchkey_hash = searchkey_bin.låttitel

    # unsorted list
    searchlist = song_list[:n]

    # sorted list
    sortedlist = sorted(searchlist, key=lambda x: x.låttitel)

    # hashmap
    searchdict = dict(zip(track_list, searchlist))

    # test time
    lintid = timeit.timeit(stmt=lambda: linsok(searchlist, searchkey_lin), number=10000)
    print(f'Linjärsökning tar {round(lintid, 4)} sekunder.')

    bintid = timeit.timeit(stmt=lambda: binsok(sortedlist, searchkey_bin), number=10000)
    print(f'Binärsökning tar {round(bintid, 4)} sekunder.')

    hashtid = timeit.timeit(stmt=lambda: hashsok(searchdict, searchkey_hash), number=10000)
    print(f'Hashsökning tar {round(hashtid, 4)} sekunder.')


"""
number = 10
n:                  1000        10 000      100 000         1 000 000
Urvalssortering:   0.4901s     49.5334s      *5000s         *500000s
Quicksort:         0.0129s      0.1811s      2.7452s         33.6877s

Urvalssortering är O(n^2)  ==>     T(n) = k * n^2
Quicksort är O(nlog(n))    ==>     T(n) = k * nlog(n)
* (ungefärlig) beräknad tid
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
        if left >= right:
            break
    data[left], data[right] = data[right], data[left]
    return left


def sortering():
    n = int(input('Ange antal element: '))
    print('Antal element =', n)

    data = track_list[:n]

    urvalstid = timeit.timeit(stmt=lambda: urvalssort(data), number=10)
    print(f'Urvalssortering tog {round(urvalstid, 4)} sekunder att sortera {n} element.')

    quicktid = timeit.timeit(stmt=lambda: quicksort(data), number=10)
    print(f'Quicksort tog {round(quicktid, 4)} sekunder att sortera {n} element.')


"""
Tidskomplexiteten för de algoritmer vi använt verkar stämma överens med teorin. Vid jämgörelse av
beräknad körtid och faktiskt körtid har vi sett att de stämmer hyffsat överrens.

Som förväntat tar det avsevärt längre tid att sortera element än att hitta ett element.
Tex om vi jämför linjärsökningen och urvalssorteringen - båda långsammast inom sin kategori -
är linjärsökningen endast O(n) och urvalssökningen O(n^2), detta pga att for-loopen i linjärsökningen
har störst tidskomplexitet i och med att den går igenom minst n-antal element medan urvalssorteringen
inte bara måste flytta element utan har nästlade for-loopar vilket ger att tidskoplexiteten ges av
(n^2) eftersom den måste gå igenom n antal element n antal gånger.

Det är inte heller förvånande att quicksort tar längre tid än sin ''sökmotsvarighet'' binärsökning.
Binärsökningen halverar antalet element den kollar efter varje iteration medan quicksort utför log(n)
antal partitioner/halveringar där metoden måste iterera över alla n antal element, därav är quicksort
O(nlog(n)) och binärslningen O(log2(n)).

Hashsökningen är O(1) (konstant tidskomplexitet).

** Alla angivna tidskomplexiteter är genomsnittliga.
"""

if __name__ == '__main__':
    sokning()
    sortering()





























