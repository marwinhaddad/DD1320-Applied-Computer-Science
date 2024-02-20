import unittest


class SolutionFound(Exception):
    pass


# klass som skapar nod
class ParentNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent


# klass som skapar nod
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# klass som skapar länkad lista
class LinkedQ:
    def __init__(self):
        self._first = None
        self._last = None

    # returnerar True om listan är tom, annars False
    def isEmpty(self):
        return self._first is None

    # om listan är tom är första elementet samma som sista
    # annars länkas nya elemntet med tidigare och hamnar längst bak i listan
    def enqueue(self, element):
        new_node = Node(element)
        if self.isEmpty():
            self._first = new_node
            self._last = self._first
        else:
            self._last.next = new_node
            self._last = new_node

    # returnerar none om listan är tom
    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty!')
            self._last = self._first
            return None
        else:
            node_value = self._first.value
            self._first = self._first.next
            return node_value

    # returnerar längden på listan genom att addera 1 till count så länge nästa nod inte är tom
    def size(self):
        current = self._first
        count = 1
        while current.next:
            temp = current.next
            current = temp
            count += 1
        return count

    # printar objektens värden i den ordning objekten ligger i länkade listan
    def __str__(self):
        current = self._first
        valuestr = ''
        while current.value != '#':
            valuestr += current.value
            current = current.next
        return str(valuestr)

    # returnerar det första elementet i kön
    def peek(self):
        return self._first.value


class TestQueue(unittest.TestCase):

    def test_isEmpty(self):
        # isEmpty ska returnera True för tom kö, False annars
        q = LinkedQ()
        self.assertTrue(q.isEmpty(), "isEmpty på tom kö")
        q.enqueue(17)
        self.assertFalse(q.isEmpty(), "isEmpty på icke-tom kö")

    def test_order(self):
        # Kontrollerar att kö-ordningen blir rätt
        q = LinkedQ()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)


if __name__ == "__main__":
    unittest.main()
