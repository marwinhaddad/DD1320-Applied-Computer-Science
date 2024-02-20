from collections import OrderedDict
import csv
import timeit
from hashClassFile import Hashtable
from pokemonClassFile import Pokemon
from tabulate import tabulate


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


def time_find(d, searchkey):
    return d[searchkey]


def main():
    pokemon_list = read_cvs()
    h = Hashtable(len(pokemon_list)*2)
    o = OrderedDict()
    hash_200 = timeit.timeit(stmt=lambda: fill_dict(h, pokemon_list[:200]), number=10000)
    ord_200 = timeit.timeit(stmt=lambda: fill_dict(o, pokemon_list[:200]), number=10000)
    hash_400 = timeit.timeit(stmt=lambda: fill_dict(h, pokemon_list[:400]), number=10000)
    ord_400 = timeit.timeit(stmt=lambda: fill_dict(o, pokemon_list[:400]), number=10000)
    hash_800 = timeit.timeit(stmt=lambda: fill_dict(h, pokemon_list), number=10000)
    ord_800 = timeit.timeit(stmt=lambda: fill_dict(o, pokemon_list), number=10000)
    h = fill_dict(h, pokemon_list)
    o = fill_dict(o, pokemon_list)
    hash_find = timeit.timeit(stmt=lambda: time_find(h, 'Pikachu'), number=10000)
    ord_find = timeit.timeit(stmt=lambda: time_find(o, 'Pikachu'), number=10000)
    table = [['antal element', '200', '400', '800'],
             ['Hashtabell', round(hash_200, 4), round(hash_400, 4), round(hash_800, 4)],
             ['OrderedDict', round(ord_200, 4), round(ord_400, 4), round(ord_800, 4)]]
    print(tabulate(table, headers='firstrow'))
    print('\nBland 800 element tog det:')
    print(f'Hashtabell {round(hash_find, 4)}s att hitta Pikachu\n'
          f'OrderedDict {round(ord_find, 4)}s att hitta Pikachu')


if __name__ == '__main__':
    main()

