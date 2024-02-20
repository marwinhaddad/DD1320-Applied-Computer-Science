import matplotlib.pyplot as plt


class DictHash:
    def __init__(self):
        self.dicthash = {}

    def store(self, key, value):
        self.dicthash[key] = value

    def search(self, key):
        try:
            return self.dicthash[key]
        except KeyError:
            return None

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):
        return key in self.dicthash


class HashNode:
    def __init__(self, key='', value=None):
        self.key = key
        self.value = value
        self.next = None


class Hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def store(self, key, value):

        # get hashed index of key
        index = self._hashfunction(key)
        current = self.table[index]

        # test if hashtable at index is empty or not
        # if empty insert new node
        if current is None:
            self.table[index] = HashNode(key, value)

        # if occupied iterate through nodes until empty and insert new node
        else:
            while current.next is not None and current.key != key:
                current = current.next

            # if key value already exists replace with new key value
            if current.key == key:
                current.value = value

            # else create new node at end of linked list
            else:
                current.next = HashNode(key, value)

    def search(self, key):

        # get hashed index of key
        index = self._hashfunction(key)
        current = self.table[index]

        # iterate through linked list at index until key is found and return value
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        # otherwise raise KeyError
        raise KeyError

    def hashfunction(self, key):
        hashsum = 0
        if isinstance(key, str):
            for x, i in enumerate(key):
                hashsum += hashsum * 10**x + ord(i)
        else:
            hashsum += key**2
            hashsum = int(str(hashsum)[len(str(hashsum))//2 - 1: len(str(hashsum))//2 + 2])
        return hashsum % self.size

    def __contains__(self, key):
        if self.search(key):
            return True
        return False

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        return self.store(key, value)

    def get_chart(self):
        total = 0
        indexlist = []
        countlist = []
        index = 0
        for current in self.table:
            indexlist.append(index)
            count = 0
            while current is not None:
                count += 1
                current = current.next
            index += 1
            total += count
            countlist.append(count)

        plt.bar(indexlist, countlist)
        plt.title('Spridning av element i Hashtable\n'
                  f'Total: {total} element      Storlek: {self.size} positioner')
        plt.xlabel('Index')
        plt.ylabel('Antal per index')
        plt.show()

