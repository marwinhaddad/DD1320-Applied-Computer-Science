# linjärsökning

def exists_index(my_list, key):
    for x in my_list:
        if x == key:
            return my_list.index(x)
    return False


# eller en count

def exists_count(my_list, key):
    count = 0
    for y in my_list:
        if y == key:
            return count
        count += 1
    return False


# binärsökning

def binary_search(data, key):
    low = 0
    high = len(data)-1

    while low <= high:
        middle = (low+high)//2
        if data[middle] == key:
            return True
        else:
            if key < data[middle]:
                high = middle-1
            else:
                low = middle+1
    return False


# interpolationssökning

def inter_search(data, key):
    low = 0
    high = len(data)-1

    while low <= high:
        middle = round(low + (key - data[low])*((high-low)/(data[high]-data[low])))
        if data[middle] == key:
            return True
        else:
            if key < data[middle]:
                high = middle-1
            else:
                low = middle+1
    return False


# rekursiva funktioner

def S(n):
    if n == 1:
        return 1
    else:
        return S(n-1) + n


def len_linked_list(node):
    if node is None:
        return 0
    else:
        return 1 + len_linked_list(node.next)


print(exists_index([9, 14, 23, 54, 92, 104], 54))
print(exists_count([9, 14, 23, 54, 92, 104], 54))
print(binary_search([9, 14, 23, 54, 92, 104], 105))
print(inter_search([9, 14, 23, 54, 92, 104], 104))
print(S(10))

