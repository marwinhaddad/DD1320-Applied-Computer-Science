from collections import OrderedDict
from hashClassFile import Hashtable


def ordered(arr):
    o = OrderedDict()
    for i, x in enumerate(arr):
        o[i] = x
    print(o)
    print(o.popitem(last=False))
    print(o)
    o.move_to_end(3, last=False)
    print(o)
    print()


def table(arr):
    h = Hashtable(len(arr)*2)
    for i, x in enumerate(arr):
        h[i] = x
    print(h)
    print(h[0])
    print(h)


def main():
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    ordered(arr)
    table(arr)


if __name__ == '__main__':
    main()



