from bintreeFile import Bintree
from linkedQFile import *

global svenska, dumbarnen, slutord

alfabetet = 'abcdefghijklmnopqrstuvwxyzåäö'


def main():
    global slutord

    startord = input('Startord: ')
    slutord = input('Slutord: ')

    get_dict()
    dumbarnen.put(startord)

    q = LinkedQ()
    urfader = ParentNode(startord)
    q.enqueue(urfader)
    try:
        while not q.isEmpty():
            nod = q.dequeue()
            makechildren(nod, q)
        print(f'Det finns ingen väg från {startord} till {slutord}')
    except SolutionFound:
        pass


def get_dict():
    global svenska, dumbarnen

    dumbarnen = Bintree()
    svenska = Bintree()
    with open('word3.txt', 'r', encoding='utf-8') as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            if ordet in svenska:
                pass
            else:
                svenska.put(ordet)


def makechildren(nod, q):
    global slutord, svenska

    for i in range(len(nod.value)):
        list_barn = list(nod.value)
        for j in range(len(alfabetet)):
            list_barn[i] = alfabetet[j]
            nytt_barn = ''.join(list_barn)
            nytt_barn = ParentNode(nytt_barn, nod)
            if nytt_barn.value in svenska:
                if nytt_barn.value not in dumbarnen:
                    dumbarnen.put(nytt_barn.value)
                    q.enqueue(nytt_barn)
                if nytt_barn.value == slutord:
                    print('Det finns en väg till', slutord)
                    writechain(nytt_barn)
                    raise SolutionFound


def writechain(nod):
    if nod.parent:
        writechain(nod.parent)
        print(' -->', nod.value, end='')
    if not nod.parent:
        print(nod.value, end='')


main()
