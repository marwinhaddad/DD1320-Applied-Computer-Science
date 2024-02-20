from linkedQFile import *
import sys


def Trollkarlsprogrammet_LinkedQ(card_order):
    card_linked = LinkedQ()
    for number in card_order:
        card_linked.enqueue(number)
    table = []
    for _ in range(card_linked.size()+1):
        card_linked.enqueue(card_linked.dequeue())
        table.append(card_linked.dequeue())
    print(*table)


if __name__ == '__main__':

    sample = sys.stdin.read()
    sample = sample.split()
    Trollkarlsprogrammet_LinkedQ(sample)
