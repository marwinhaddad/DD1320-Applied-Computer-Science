from collections import OrderedDict
import csv
import pympler.asizeof as asizeof
from hashClassFile import Hashtable
from pokemonClassFile import Pokemon


def read_cvs():
    pokemon_list = []
    with open('pokemon.csv') as f:
        next(f)
        for row in csv.reader(f):
            pokemon_list.append(Pokemon(row))
    return pokemon_list


def fill_dict(d, arr):
    for x in arr:
        d[x.name] = x
    return d


def main():
    pokemon_list = read_cvs()
    h = Hashtable(len(pokemon_list)*2)
    o = OrderedDict()

    h = fill_dict(h, pokemon_list)
    o = fill_dict(o, pokemon_list)

    print(asizeof.asizeof(h))
    print(asizeof.asizeof(o))


if __name__ == '__main__':
    main()
