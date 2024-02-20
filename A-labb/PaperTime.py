import timeit
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate


# testa tidskomplexitet
def calc_tape(nlist):
    # definiera dimensioner på A2 ark
    long_side = 2 ** (-3 / 4)
    short_side = 2 ** (-5 / 4)

    # summa av alla tejplängder, vi börjar med längden av en A2 pga det är en
    # minsta tejpbiten man kan behöva
    sum_tape = long_side

    # eftersom varje storlek är dubbelt så stor som nästa så börjar vi med att
    # anta att vi behöver 2st A2
    sheets_needed = 2

    # current_size motsvarar antal papper av varje storlek i listan nlist
    for current_size in nlist:

        # skillnaden mellan antalet papper vi behöver och antalet vi har ger oss
        # antalet vi behöver av nästa storlek
        sheets_needed -= current_size

        # om vi inte behöver några ark av nästa storlek vet vi att vi är klara
        if sheets_needed <= 0:
            return sum_tape

        # nästa långsida är nuvarande kortsida // nästa kortsida är hälften av
        # nuvarande långsida
        long_side, short_side = short_side, long_side / 2

        # adderar till tejplängden antalet ark vi behöver av nuvarande längd multiplicerat
        # med  nästa storleks längd
        sum_tape += sheets_needed * long_side

        # antalet ark vi behöver av nästa storlek är dubbelt så många
        sheets_needed *= 2

    # returnerar 'impossible' ifall "sheets_needed" aldrig blir noll
    return 'impossible'


def main(nrow):
    nlist = [int(n) for n in nrow.split()]
    return calc_tape(nlist)


if __name__ == '__main__':
    tidlista = []
    with open('two_to_thirty') as f:
        for i, row in enumerate(f.readlines()):
            tidlista.append(timeit.timeit(stmt=lambda: main(row), number=10000))

    x = np.array(range(1, len(tidlista)+1))
    k, m = np.polyfit(x, tidlista, 1)[0], np.polyfit(x, tidlista, 1)[1]
    print()
    print(tabulate([['n', '2', '5', '10', '20', '30'],
                    ['tid(s)', tidlista[0], tidlista[3], tidlista[8], tidlista[18], tidlista[28]]],
                   headers='firstrow'))
    r = np.corrcoef(x, tidlista)
    plt.plot(x, tidlista, 'o', label='Körtid för varje pappersstorlek')
    plt.plot(x, k*x+m, 'r', label=f'{np.round(k, 5)}*x+{np.round(m, 5)}')
    plt.plot([], [], ' ', label=f'Korrelationskoefficient r = {round(r[0][1], 4)}')
    plt.legend()
    plt.title('Körtid per minsta pappersstorlek mellan 2 och 30')
    plt.xlabel('Minsta pappersstorlek')
    plt.ylabel('Körtid (s)')
    plt.show()

