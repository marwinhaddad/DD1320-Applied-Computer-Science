from linkedQFile import LinkedQ
import unittest


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(checkSyntax('Na'), 'Formeln är syntaktiskt korrekt')

    def test2(self):
        self.assertEqual(checkSyntax('H2O'), 'Formeln är syntaktiskt korrekt')

    def test3(self):
        self.assertEqual(checkSyntax('Si(C3(COOH)2)4(H2O)7'), 'Formeln är syntaktiskt korrekt')

    def test4(self):
        self.assertEqual(checkSyntax('Na332'), 'Formeln är syntaktiskt korrekt')

    def test5(self):
        self.assertEqual(checkSyntax('C(Xx4)5'), 'Okänd atom vid radslutet 4)5')

    def test6(self):
        self.assertEqual(checkSyntax('C(OH4)C'), 'Saknad siffra vid radslutet C')

    def test7(self):
        self.assertEqual(checkSyntax('C(OH4C'), 'Saknad högerparentes vid radslutet')

    def test8(self):
        self.assertEqual(checkSyntax('H2O)Fe'), 'Felaktig gruppstart vid radslutet )Fe')

    def test9(self):
        self.assertEqual(checkSyntax('H0'), 'För litet tal vid radslutet')

    def test10(self):
        self.assertEqual(checkSyntax('H1C'), 'För litet tal vid radslutet C')

    def test11(self):
        self.assertEqual(checkSyntax('H02C'), 'För litet tal vid radslutet 2C')

    def test12(self):
        self.assertEqual(checkSyntax('Nacl'), 'Saknad stor bokstav vid radslutet cl')

    def test13(self):
        self.assertEqual(checkSyntax('a'), 'Saknad stor bokstav vid radslutet a')

    def test14(self):
        self.assertEqual(checkSyntax('(Cl)2)3'), 'Felaktig gruppstart vid radslutet )3')

    def test15(self):
        self.assertEqual(checkSyntax(')'), 'Felaktig gruppstart vid radslutet )')

    def test16(self):
        self.assertEqual(checkSyntax('2'), 'Felaktig gruppstart vid radslutet 2')


class IncorrectSyntax(Exception):
    pass


atomlist = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S',
            'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga',
            'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd',
            'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm',
            'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os',
            'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa',
            'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg',
            'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']

stack = []


def readFormel(q):
    readMol(q)


def readMol(q):
    readGroup(q)
    if q.peek() != '#':
        if q.peek() == ')':
            return
        readMol(q)


def readGroup(q):
    if q.peek().isalpha():
        print('kollar bokstav')
        readAtom(q)
        if q.peek().isnumeric():
            readNum(q)
        return
    if q.peek() == '(':
        print(q.dequeue())
        readMol(q)
        if q.peek() == ')':
            print(q.dequeue())
            if q.peek().isnumeric():
                readNum(q)
                return
            raise IncorrectSyntax('Saknad siffra')
        raise IncorrectSyntax('Saknad högerparentes')
    raise IncorrectSyntax('Felaktig gruppstart')


def readAtom(q):
    X = readLETTER(q)
    if q.peek().islower():
        x = readletter(q)
    else:
        x = ''
        print(X+x)
    if X + x in atomlist:
        return X + x
    raise IncorrectSyntax('Okänd atom')


def readLETTER(q):
    if q.peek().isupper():
        return q.dequeue()
    raise IncorrectSyntax('Saknad stor bokstav')


def readletter(q):
    if q.peek().islower():
        return q.dequeue()
    raise IncorrectSyntax('Saknad liten bokstav')


def readNum(q):
    number = ''
    if not q.peek().isalpha():
        if q.peek() != '0':
            while q.peek().isnumeric():
                number += q.dequeue()
            if int(number) >= 2:
                print(number)
                return
            else:
                raise IncorrectSyntax('För litet tal')
        else:
            q.dequeue()
            raise IncorrectSyntax('För litet tal')
    raise IncorrectSyntax('Saknad siffra')


def storeQ(sentence):
    q = LinkedQ()
    for x in sentence:
        q.enqueue(x)
    q.enqueue('#')
    return q


def checkSyntax(sentence):
    q = storeQ(sentence)
    try:
        readFormel(q)
        return 'Formeln är syntaktiskt korrekt'
    except IncorrectSyntax as err:
        return (str(err) + ' vid radslutet ' + str(q)).rstrip()


def main():
    molekyl = input('Ange molekyl: ')
    result = checkSyntax(molekyl)
    print(result)


if __name__ == '__main__':
    main()
