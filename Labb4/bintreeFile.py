
# klass som definierar nod-objekt
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# klass som definierar binärt sökträd
class Bintree:
    def __init__(self):
        self.root = None    # den första noden i det binära sökträdet

    # stoppar in element i sökträdet
    def put(self, new_value):
        if self.root is None:   # om första noden är tom skapar vi en nod med nya värdet
            self.root = Node(new_value)
        else:
            putta(new_value, self.root) # finns det en rot kallar vi på hjälpfunktion putta med nya värdet och roten

    # kollar om ett input-värde finns i sökträdet
    def __contains__(self, value):
        if self.root is not None:   # om det finns en rot kallar vi på hjälpfunktion finns
            return finns(self.root, value)
        else:
            return False    # om det inte finns en rot returnerar vi False, dvs det finns inget värde som matchar input

    # skriver ut alla värden i sökrädet
    def write(self):   # om vi har en rot kallar vi på hjälpfunktionen skriv med roten som inparameter
        skriv(self.root)
        print('\n')


# hjälpfunktion till Bintree.put()
# tar värdet man vill stoppa in och roten som inparameter
def putta(value, current_node):
    if value < current_node.value:  # om value är mindre än föräldern sorteras det till vänster
        if current_node.left is None: # om föräldern inte har ett vänsterbarn blir value det barnet
            current_node.left = Node(value)
        else:
            putta(value, current_node.left) # annars kallas putta rekursivt med value och nästa nod till vänster som inparameter
    elif value > current_node.value:    # om value är större än föräldern sorteras det till höger
        if current_node.right is None:  # om föräldern inte har ett högerbarn blir value det barnet
            current_node.right = Node(value)
        else:
            putta(value, current_node.right) # annars kallas putta rekursivt med value och nästa nod till höger som inparameter
    else:
        print(f'{value} is already in tree') # är värdet varken större eller mindre finns värdet redan i trädet


# hjälpfunktion till Bintree.__contains__()
# kollar om value finns i trädet
def finns(current_node, value):
    if current_node is None:    # om current_node är barnet till ett löv, dvs None, returneras False
        return False
    if value == current_node.value:     # om värdet finns i föräldern returneras True
        return True
    elif value < current_node.value:
        return finns(current_node.left, value)  # annars kollas vänster barn mha rekursion
    elif value > current_node.value:
        return finns(current_node.right, value) # annars kollas höger barn mha rekursion


# hjälpfunktion till Bintree.write()
# printar alla värden i trädet i storleksordning från min -> max
def skriv(current_node):
    if current_node is not None:
        skriv(current_node.left)    # går igenom vänstra sidan till löv är None
        print(current_node.value)   # printar nodens värde
        skriv(current_node.right)   # går igenom högra sidan tills löv är None

