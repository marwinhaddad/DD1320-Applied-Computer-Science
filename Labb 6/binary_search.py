
def binary_search(the_list, key):
    first = 0
    last = len(the_list) - 1
    while first <= last:
        mid = (first + last)//2
        if the_list[mid] == key:
            return key
        else:
            if key < the_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return None


def main():
    #Läs in listan
    indata = input().strip()
    the_list = indata.split()
    #Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()


main()
