from linkedQFile import LinkedQ
import unittest


class MolekylTest(unittest.TestCase):

    def test_korrekt1(self):
        self.assertEqual(checkSyntax("H"), "Formeln är syntaktiskt korrekt")

    def test_korrekt2(self):
        self.assertEqual(checkSyntax("He"), "Formeln är syntaktiskt korrekt")

    def test_korrekt3(self):
        self.assertEqual(checkSyntax("H2"), "Formeln är syntaktiskt korrekt")

    def test_korrekt4(self):
        self.assertEqual(checkSyntax("He15"), "Formeln är syntaktiskt korrekt")

    # test av inkorrekta siffror
    def test_för_litet_tal(self):
        self.assertEqual(checkSyntax("H1"), "För litet tal vid radslutet ")

    def test_tal_börjar_med_noll(self):
        self.assertEqual(checkSyntax("He012345"), "För litet tal vid radslutet 12345")

    # test av inkorrekta bokstäver
    def test_liten_bokstav(self):
        self.assertEqual(checkSyntax("a"), "Saknad stor bokstav vid radslutet a")

    def test_liten_bokstav_med_siffror(self):
        self.assertEqual(checkSyntax("cl12"), "Saknad stor bokstav vid radslutet cl12")

    def test_bara_siffror(self):
        self.assertEqual(checkSyntax("12"), "Saknad stor bokstav vid radslutet 12")


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
    molekyl = input('Ange molekyl: ')
    result = checkSyntax(molekyl)
    print(result)


if __name__ == '__main__':
    main()




