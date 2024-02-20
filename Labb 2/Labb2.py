from arrayQFile import ArrayQ
from linkedQFile import LinkedQ


# trollkarlsprogram med klassen ArrayQ
# card_order är en tupel med korten i den ordning man behöver ha de i korthögen för att kunna utföra tricket
def Trollkarl_ArrayQ():
    card_array = ArrayQ()           # Sapar objekt med array-atribut
    card_order = (7, 1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10)
    for number in card_order:
        card_array.enqueue(number)  # lägger till korten i array
    print('Cards in hand: ', card_array)

    table = []
    for _ in range(card_array.size()):
        card_array.enqueue(card_array.dequeue())    # tar ut kortet längst fram och lägger det underst i högen
        table.append(card_array.dequeue())          # lägger ut kortet längst fram på bordet
    print('Cards on table: ', table)
    print('Cards in hand: ', card_array)


# Trollkarlsprogram med klassen LinkedQ
def Trollkarl_LinkedQ():
    card_linked = LinkedQ()            # skapar ett länkad-lista-objekt med tomt första och sista värde
    card_order = (7, 1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10)
    for number in card_order:
        card_linked.enqueue(number)    # lägger in korten i den ordning de är i tupeln
    print('Cards in hand: ', card_linked)

    table = []
    for _ in range(card_linked.size()):
        card_linked.enqueue(card_linked.dequeue())   # plockar ut kort-objektet längst fram och lägger det längst bak
        table.append(card_linked.dequeue())          # lägger ut kort-objektet längst fram på bordet
    print('Cards on table: ', table)
    print('Cards in hand: ', card_linked)


if __name__ == '__main__':
    _ = input('Magic trick with ArrayQ. Press Enter.')
    Trollkarl_ArrayQ()
    _ = input('Magic trick with LinkedQ. Press Enter.')
    Trollkarl_LinkedQ()
