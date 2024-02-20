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

