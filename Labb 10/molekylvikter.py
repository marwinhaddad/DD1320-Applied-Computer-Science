from linkedQFile import LinkedQ
from molgrafik import *

atoms = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S',
         'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga',
         'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd',
         'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm',
         'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os',
         'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa',
         'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg',
         'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']

atomdata = "H  1.00794;\
            He 4.002602;\
            Li 6.941;\
            Be 9.012182;\
            B  10.811;\
            C  12.0107;\
            N  14.0067;\
            O  15.9994;\
            F  18.9984032;\
            Ne 20.1797;\
            Na 22.98976928;\
            Mg 24.3050;\
            Al 26.9815386;\
            Si 28.0855;\
            P  30.973762;\
            S  32.065;\
            Cl 35.453;\
            K  39.0983;\
            Ar 39.948;\
            Ca 40.078;\
            Sc 44.955912;\
            Ti 47.867;\
            V  50.9415;\
            Cr 51.9961;\
            Mn 54.938045;\
            Fe 55.845;\
            Ni 58.6934;\
            Co 58.933195;\
            Cu 63.546;\
            Zn 65.38;\
            Ga 69.723;\
            Ge 72.64;\
            As 74.92160;\
            Se 78.96;\
            Br 79.904;\
            Kr 83.798;\
            Rb 85.4678;\
            Sr 87.62;\
            Y  88.90585;\
            Zr 91.224;\
            Nb 92.90638;\
            Mo 95.96;\
            Tc 98;\
            Ru 101.07;\
            Rh 102.90550;\
            Pd 106.42;\
            Ag 107.8682;\
            Cd 112.411;\
            In 114.818;\
            Sn 118.710;\
            Sb 121.760;\
            I  126.90447;\
            Te 127.60;\
            Xe 131.293;\
            Cs 132.9054519;\
            Ba 137.327;\
            La 138.90547;\
            Ce 140.116;\
            Pr 140.90765;\
            Nd 144.242;\
            Pm 145;\
            Sm 150.36;\
            Eu 151.964;\
            Gd 157.25;\
            Tb 158.92535;\
            Dy 162.500;\
            Ho 164.93032;\
            Er 167.259;\
            Tm 168.93421;\
            Yb 173.054;\
            Lu 174.9668;\
            Hf 178.49;\
            Ta 180.94788;\
            W  183.84;\
            Re 186.207;\
            Os 190.23;\
            Ir 192.217;\
            Pt 195.084;\
            Au 196.966569;\
            Hg 200.59;\
            Tl 204.3833;\
            Pb 207.2;\
            Bi 208.98040;\
            Po 209;\
            At 210;\
            Rn 222;\
            Fr 223;\
            Ra 226;\
            Ac 227;\
            Pa 231.03588;\
            Th 232.03806;\
            Np 237;\
            U  238.02891;\
            Am 243;\
            Pu 244;\
            Cm 247;\
            Bk 247;\
            Cf 251;\
            Es 252;\
            Fm 257;\
            Md 258;\
            No 259;\
            Lr 262;\
            Rf 265;\
            Db 268;\
            Hs 270;\
            Sg 271;\
            Bh 272;\
            Mt 276;\
            Rg 280;\
            Ds 281;\
            Cn 285;\
            () 0"

atomlist = atomdata.split(";")
atomdict = {}
for atom in atomlist:
    key, value = atom.split()
    atomdict[key] = float(value)


class IncorrectSyntax(Exception):
    pass


def readFormel(q):
    mol = readMol(q)
    if q.peek() == ')':
        raise IncorrectSyntax('Felaktig gruppstart')
    return mol


def readMol(q):
    mol = readGroup(q)
    if q.peek() == '#':
        return mol
    elif q.peek() == ')':
        return mol
    else:
        mol.next = readMol(q)
        return mol


def readGroup(q):
    rutan = Ruta()
    if q.peek().isalpha():
        rutan.atom = readAtom(q)
        if q.peek().isdigit():
            rutan.num = readNum(q)
        return rutan
    elif q.peek() == '(':
        q.dequeue()
        rutan.down = readMol(q)
        if q.peek() == ')':
            q.dequeue()
            if q.peek().isdigit():
                rutan.num = readNum(q)
                return rutan
            else:
                raise IncorrectSyntax('Saknad siffra')
        else:
            raise IncorrectSyntax('Saknad högerparentes')
    else:
        raise IncorrectSyntax('Felaktig gruppstart')


def readAtom(q):
    X = readLETTER(q)
    if q.peek().islower():
        x = readletter(q)
    else:
        x = ''
    if X + x in atoms:
        return X + x
    else:
        raise IncorrectSyntax('Okänd atom')


def readLETTER(q):
    if q.peek().isupper():
        X = q.dequeue()
        return X
    raise IncorrectSyntax('Saknad stor bokstav')


def readletter(q):
    if q.peek().islower():
        x = q.dequeue()
        return x
    raise IncorrectSyntax('Saknad liten bokstav')


def readNum(q):
    number = ''
    while q.peek().isdigit():
        if number == '0':
            break
        number += q.dequeue()
    if int(number) >= 2:
        return int(number)
    raise IncorrectSyntax('För litet tal')


def storeQ(sentence):
    q = LinkedQ()
    for x in sentence:
        q.enqueue(x)
    q.enqueue('#')
    return q


def weight(mol):
    if mol is None:
        return 0
    return atomdict[mol.atom] * mol.num + weight(mol.next) + weight(mol.down) * mol.num


def checkSyntax(sentence):
    q = storeQ(sentence)
    try:
        mol = readFormel(q)
        print(round(weight(mol), 4), 'g/mol')
        Molgrafik().show(mol)
        return 'Formeln är syntaktiskt korrekt'
    except IncorrectSyntax as err:
        return (str(err) + ' vid radslutet ' + str(q)).strip()


def main():
    molecule = input('Ange molekylformel: ')
    result = checkSyntax(molecule)
    print(result)


if __name__ == '__main__':
    main()

"""
Si(C2(CO(AuCl(KNa)6)6OH)3)4(H2O)7(Na(OH)4(Fe(NaCl)2(COO(OH2)3(Fe(Na(F(Cl)2)3)5)4)77)34)5
"""
