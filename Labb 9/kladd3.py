from linkedQFile import LinkedQ


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
    if stack:
        raise IncorrectSyntax('Felaktig gruppstart')


def readMol(q):
    readGroup(q)
    if q.peek() != '#':
        if q.peek() == ')':
            return
        readMol(q)


def readGroup(q):
    if q.peek().isalpha():
        readAtom(q)
        if q.peek().isnumeric():
            readNum(q)
        return
    elif q.peek() == '(':
        checkP(q)
        readMol(q)
        checkP(q)
        if q.peek().isnumeric():
            readNum(q)
            return
        else:
            raise IncorrectSyntax('Saknad siffra')
    else:
        raise IncorrectSyntax('Felaktig gruppstart')


def readAtom(q):
    X = readLETTER(q)
    if q.peek().islower():
        x = readletter(q)
    else:
        x = ''
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
    if q.peek() != '0':
        while q.peek().isnumeric():
            number += q.dequeue()
        if int(number) >= 2:
            return
        else:
            raise IncorrectSyntax('För litet tal')
    else:
        q.dequeue()
        raise IncorrectSyntax('För litet tal')


def storeQ(sentence):
    q = LinkedQ()
    for x in sentence:
        q.enqueue(x)
    q.enqueue('#')
    return q


def checkP(q):
    print(stack)
    if q.peek() == '(':
        stack.append(q.dequeue())
    elif q.peek() == ')':
        q.dequeue()
        if q.peek().isalpha():
            raise IncorrectSyntax('Saknad siffra')
        elif not stack:
            raise IncorrectSyntax('Felaktig gruppstart')
        else:
            stack.pop()
    else:
        raise IncorrectSyntax('Saknad högerparentes')


def checkSyntax(sentence):
    q = storeQ(sentence)
    try:
        readFormel(q)
        return 'Formeln är syntaktiskt korrekt'
    except IncorrectSyntax as err:
        return (str(err) + ' vid radslutet ' + str(q)).rstrip()


def main():
    molekyl = 'C(OH4C'
    result = checkSyntax(molekyl)
    print(result)


if __name__ == '__main__':
    main()
