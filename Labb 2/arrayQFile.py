import array as array


class ArrayQ:
    def __init__(self):
        self._arr = self.Queue()

    # skapar tom array
    def Queue(self):
        return array.array('i')

    # lägger till element längst bak
    def enqueue(self, element):
        self._arr.append(element)

    # plockar ut och returnerar elementet längst fram
    def dequeue(self):
        return self._arr.pop(0)

    # returnerar True om array är tom, annars False
    def isEmpty(self):
        return len(self._arr) == 0

    # returnerar längden på array
    def size(self):
        return len(self._arr)

    # printar lista mer elementen i array
    def __str__(self):
        return str([i for i in self._arr])


if __name__ == '__main__':
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if x == 1 and y == 2:
        print("OK")
    else:
        print("FAILED")

