def calc_tape(nlist):

    # definiera dimensioner på A2 ark
    long_side = 2**(-3/4)
    short_side = 2**(-5/4)

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
        long_side, short_side = short_side, long_side/2

        # adderar till tejplängden antalet ark vi behöver av nuvarande längd multiplicerat
        # med  nästa storleks längd
        sum_tape += sheets_needed * long_side

        # antalet ark vi behöver av nästa storlek är dubbelt så många
        sheets_needed *= 2

    # returnerar 'impossible' ifall "sheets_needed" aldrig blir noll
    return 'impossible'

def main():
    n = int(input('Ange minsta storlek: '))
    nlist = [int(x) for x in input(f'\nAnge antal per storlek från A2 till A{n}:\n').split()][:n-1]

    # funktion som beräknar och returnerar längden av tejpen
    print(calc_tape(nlist))

if __name__ == '__main__':
    main()

