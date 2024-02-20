from linkedQFile import ParentNode


def writechain(nod):
    if nod.parent:
        writechain(nod.parent)
        print('-->', nod.value, end='')
    if not nod.parent:
        print(nod.value, end='')


for i in [45, 84, 89, 54, 25, 10, 81, 63, 15, 51]:
    if i == 45:
        new = ParentNode(i)
    else:
         new = ParentNode(i, new)

writechain(new)

