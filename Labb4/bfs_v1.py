from bintreeFile import Bintree


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


def makechildren(startord):                 # skapar barn
    global svenska, dumbarnen, alfabetet

    for i in range(len(startord)):
        list_startord = list(startord)
        for j in range(len(alfabetet)):
            list_startord[i] = alfabetet[j]
            barn = ''.join(list_startord)
            if barn in svenska:
                if barn not in dumbarnen:
                    print(barn)
                    dumbarnen.put(barn)


def main():
    global slutord

    startord = input('Startord: ')
    slutord = input('Slutord: ')
    get_dict()

    dumbarnen.put(startord)
    makechildren(startord)


main()
