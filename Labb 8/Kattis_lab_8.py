from linkedQFile import LinkedQ
import sys


class IncorrectSyntax(Exception):
    pass


"""
Regler:

<molekyl> ::= <atom> | <atom><num>
<atom>    ::= <LETTER>  | <LETTER><letter>
<LETTER>  ::= A | B | C | ... | Z
<letter>  ::= a | b | c | ... | z
<num>     ::= 2 | 3 | 4 | ...

"""


def readMolekyl(q):
    readAtom(q)
    if q.peek() == '#':
        q.dequeue()
    else:
        readNum(q)


def readAtom(q):
    readLETTER(q)
    if q.peek().isalpha():
        readletter(q)


def readLETTER(q):
    if q.peek().isupper():
        q.dequeue()
        return
    raise IncorrectSyntax('Saknad stor bokstav')


def readletter(q):
    if q.peek().islower():
        q.dequeue()
        return
    raise IncorrectSyntax('Saknad liten bokstav')


def readNum(q):
    number = ''
    while q.peek() != '#':
        if number == '0':
            break
        number += q.dequeue()
    if number.isnumeric() and int(number) >= 2:
        return
    raise IncorrectSyntax('För litet tal')


def storeQ(sentence):
    q = LinkedQ()
    for x in sentence:
        q.enqueue(x)
    q.enqueue('#')
    return q


def checkSyntax(sentence):
    q = storeQ(sentence)
    try:
        readMolekyl(q)
        return 'Formeln är syntaktiskt korrekt'
    except IncorrectSyntax as err:
        return str(err) + ' vid radslutet ' + str(q)


def main():
    mlist = ['Mm0987654321']
    # for x in sys.stdin.readlines():
    #     mlist.append(x.strip('\n'))
    for molekyl in mlist:
        if molekyl != "#":
            result = checkSyntax(molekyl)
            print(result)


if __name__ == '__main__':
    main()
