from bintreeFile import Bintree


# testar om write() fungerar

def write_test(tree, data):
    print('tree should print: ')
    data.sort()
    for i in data:
        print(i)
    print('\ntree prints: ')
    tree.write()


# testar om contains() fungerar

def contains_test(tree):
    print('3 is in tree. contains function says: ')
    if 3 in tree:
        print('3 is in tree\n')
    else:
        print('3 is not in tree\n')

    print('5 is not in tree. contains function says: ', sep='')
    if 5 in tree:
        print('5 is in tree\n')
    else:
        print('5 is not in tree\n')

    print('69 is in tree. contains function says: ', sep='')
    if 3 in tree:
        print('69 is in tree\n')
    else:
        print('69 is not in tree\n')


# testar om det fungerar att stoppa in värden i trädet

def put_test(tree, data):
    for i in data:
        tree.put(i)


# skapar träd och testar ovannämnda

def uppgift_1():
    tree = Bintree()
    data = [3, 33, 45, 88, 69, 16, 13, 42, 66, 29]

    put_test(tree, data)

    write_test(tree, data)

    contains_test(tree)


# skapar Bintree-objekt och printar ord som redan finns i sökträdet svenska

def uppgift_2():
    svenska = Bintree()
    with open('word3.txt', 'r', encoding='utf-8') as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                print(ordet, end=' ')
            else:
                svenska.put(ordet)             # in i sökträdet
    print('\n')
    return svenska


# skapar sökträdet engelska och stoppar in ord som inte redan finns i sökträdet
# om ordet finns i engelska sökträdet kollar vi ifall samma ord existerar i det svenska
# om så är fallet printar vi ordet

def uppgift_3(svenska):
    engelska = Bintree()
    dumbarn = Bintree()
    with open('engelska.txt', 'r', encoding='utf-8') as engelskafil:
        for rad in engelskafil:
            for ordet in rad.split():
                if ordet in engelska:
                    dumbarn.put(ordet)
                else:
                    engelska.put(ordet)
                    if ordet in svenska:
                        print(ordet, end=' ')
    print()


uppgift_1()
svenska = uppgift_2()
uppgift_3(svenska)



