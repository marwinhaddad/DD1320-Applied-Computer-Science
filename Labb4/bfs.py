from bintreeFile import Bintree
from linkedQFile import LinkedQ

global svenska, dumbarnen, slutord
alfabetet = 'abcdefghijklmnopqrstuvwxyzåäö'


def get_dict():                 # skapar ordboken och dumbarnslistan
    global svenska, dumbarnen

    svenska = Bintree()
    dumbarnen = Bintree()
    with open('word3.txt', 'r', encoding='utf-8') as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            if ordet in svenska:
                pass
            else:
                svenska.put(ordet)


def makechildren(nod, q):           # skapar barn och lägger till de i länkad lista, returnerar True om det finns en väg
    global svenska, dumbarnen       # urfadern och länkade listan som inparameter

    for i in range(len(nod)):
        list_value = list(nod)
        for j in range(len(alfabetet)):
            list_value[i] = alfabetet[j]
            barn = ''.join(list_value)
            if barn in svenska:
                if barn not in dumbarnen:
                    dumbarnen.put(barn)
                    q.enqueue(barn)
                if barn == slutord:
                    print('Det finns en väg till', slutord)
                    return True


def main():
    global slutord

    startord = input('Startord: ')
    slutord = input('Slutord: ')
    get_dict()

    q = LinkedQ()
    q.enqueue(startord)
    dumbarnen.put(startord)
    while not q.isEmpty():
        nod = q.dequeue()
        hittat = makechildren(nod, q)
        if hittat:
            break
    if not hittat:
        print(f'Det finns ingen väg från {startord} till {slutord}')


main()
