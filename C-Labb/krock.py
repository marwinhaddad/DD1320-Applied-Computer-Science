from collections import OrderedDict
import csv
import matplotlib.pyplot as plt
from hashClassFile import Hashtable
from pokemonClassFile import Pokemon


def fill_dict(d, arr):
    for x in arr:
        d[x.name] = x
    return d


def read_cvs():
    pokemon_list = []
    with open('pokemon.csv') as f:
        next(f)
        for row in csv.reader(f):
            pokemon_list.append(Pokemon(row))
    return pokemon_list


def get_chart(h, o):
    total = 0
    index_h = []
    count_h = []
    index = 0
    for current in h.table:
        index_h.append(index)
        count = 0
        while current:
            count += 1
            current = current.next
        index += 1
        total += count
        count_h.append(count)

    plt.figure(1)
    plt.bar(index_h, count_h)
    plt.title('Spridning av element i Hashtable\n'
              f'Total: {total} element      Storlek: {h.size} positioner')
    plt.xlabel('Index')
    plt.ylabel('Antal per index')

    plt.figure(2)
    plt.bar([i for i in range(len(o))], [1 for _ in range(len(o))])
    plt.title('Spridning av element i OrderedDict\n'
              f'Total: {total} element      Storlek: {len(o)} positioner')
    plt.xlabel('Index')
    plt.ylabel('Antal per index')
    plt.axis([0, len(o), 0, 4])
    plt.show()


def main():
    pokemon_list = read_cvs()
    h = Hashtable(len(pokemon_list)*2)
    o = OrderedDict()
    h = fill_dict(h, pokemon_list)
    o = fill_dict(o, pokemon_list)
    get_chart(h, o)


if __name__ == '__main__':
    main()
