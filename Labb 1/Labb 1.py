# Christopher Blizzard, Marwin Haddad

import csv
import pandas as pd


class Pokemon:
    def __init__(self, poke_list):
        self.number = int(poke_list[0])
        self.name = poke_list[1]
        self.type_1 = poke_list[2]
        self.type_2 = poke_list[3]
        self.total = int(poke_list[4])
        self.hp = int(poke_list[5])
        self.Atc = int(poke_list[6])
        self.Def = int(poke_list[7])
        self.Sp_Atc = int(poke_list[8])
        self.Sp_Def = int(poke_list[9])
        self.speed = int(poke_list[10])
        self.gen = poke_list[11]
        self.legend = poke_list[12]

    def __str__(self):
        return str(
            [self.number, self.name, self.type_1, self.type_2, self.total, self.hp, self.Atc, self.Def, self.Sp_Atc,
             self.Sp_Def,
             self.speed, self.gen, self.legend])

    def __lt__(self, other):
        if self.total < other.total:
            print(self.name + ' lost to ' + other.name + ' :(')
            return True
        else:
            print(self.name + ' won!\n')
            return False

    def lvl_up(self):
        self.hp += 12
        self.Sp_Def += 3
        self.Sp_Atc += 2
        self.Atc += 4
        self.Def += 5
        self.speed += 2
        self.total = self.hp + self.Sp_Def + self.Sp_Atc + self.Atc + self.Def + self.speed
        print(self.name + ' has leveled up.\n' + self.__str__())

    def get_stats(self):

        stat_data = {'#: ': str(self.number),
                     'Name: ': self.name,
                     'Type 1: ': self.type_1,
                     'Type 2: ': self.type_2,
                     'Total: ': str(self.total),
                     'HP: ': str(self.hp),
                     'Attack: ': str(self.Atc),
                     'Defence: ': str(self.Def),
                     'SP. Attack: ': str(self.Sp_Atc),
                     'SP. Defence: ': str(self.Sp_Def),
                     'Speed: ': str(self.speed),
                     'Generation: ': str(self.gen),
                     'Legendary status: ': self.legend}

        stat_data_series = pd.Series(list(stat_data.values()), index=list(stat_data.keys()))
        print(stat_data_series)


def test():
    new_pokemon_1 = Pokemon(
        ['722', 'ChrisBlizz', 'Fire', 'Flying', '360', '60', '60', '60', '60', '60', '60', '7', 'True'])
    new_pokemon_2 = Pokemon(
        ['723', 'MarHad', 'Poison', 'Ground', '420', '70', '70', '70', '70', '70', '70', '8', 'False'])

    print(new_pokemon_1)
    print(new_pokemon_2)

    _ = input(new_pokemon_1.name + ' Vs. ' + new_pokemon_2.name + '. Press Enter to fight!')

    if new_pokemon_1 < new_pokemon_2:
        new_pokemon_2.lvl_up()
    else:
        new_pokemon_1.lvl_up()

    _ = input('Press Enter to get stats of Pokemon.')
    new_pokemon_1.get_stats()
    new_pokemon_2.get_stats()


def read_and_create():
    pokemon_list = list()
    with open('pokemon.csv') as f:
        next(f)
        for row in csv.reader(f):
            pokemon_list.append(Pokemon(row))
    return pokemon_list


def search():
    pokemon_list = read_and_create()
    while True:
        user_input = input('\nSearch for Pokemon by...\n'
                           '1. Number\n'
                           '2. Name\n'
                           '3. Type\n'
                           '4. Exit\n')
        if user_input == '1':
            number_input = int(input('Enter number: '))
            for pokemon in pokemon_list:
                if pokemon.number == number_input:
                    pokemon.get_stats()
        elif user_input == '2':
            name_input = input('Enter name: ')
            for pokemon in pokemon_list:
                if name_input in pokemon.name:
                    pokemon.get_stats()
        elif user_input == '3':
            type_input = input('Enter type: ')
            for pokemon in pokemon_list:
                if pokemon.type_1 == type_input or pokemon.type_2 == type_input:
                    pokemon.get_stats()
        elif user_input == '4':
            exit()
        else:
            pass


test()
search()
