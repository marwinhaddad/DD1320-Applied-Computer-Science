import math


def transposition(msg, col):
    for i in range(len(msg) // col):
        print(msg[i * col:col + i * col])


def rot13(word):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_word = ''
    for letter in word:
        index = (alphabet.index(letter) + 13) % len(alphabet)
        new_word += alphabet[index]
    return new_word


def bokchiffer(secret):
    secret = secret.split()
    pagelist = secret[::2]
    wordlist = secret[1::2]

    for i in range(len(pagelist)):
        page = ('0000' + pagelist[i])[-4:]
        word = int(wordlist[i])

        with open('C:/Users/marwi/PycharmProjects/pythonProject/tilda_labbar/Pages/' + page[-4:] + '.txt', 'r', encoding='utf-8') as f:
            n = 0
            while n < word:
                for j in f.readline().split():
                    n += 1
                    if n == word:
                        print(j)
                        break


bokchiffer('44 5 236 5 47 1 243 32')

print('ROT13: ABCDEFGHIJKLM -->', rot13('ABCDEFGHIJKLM'))

message = input("Message: ")
columns = int(input("Columns: "))
transposition(message, columns)

msg = 0b1001
key = 0b1110
cleartxt = msg ^ key
print('{} ^ {} = {}'.format(chr(msg), chr(key), chr(cleartxt)))

'''
Krypteringsmetoderna ovan är exempel på symetrisk kryptering,
dvs där avsändare och mottagare har samma dekrypteringsnyckel.
'''

'''
Hur kan man veta att det är rätt person som skickat meddelandet?
Användaren kan skicka med en krypterad version av sin privata nyckel. Mottagaren kan
sedan dekryptera signaturen med avsändarens publika nyckel.
'''

'''
Hashning:
Konvertera lösenord mm. till stora tal istället för att lagra informationen som den är.
En hashfunktion kan ge samma tal för olika lagrad information, därav är det väldigt
svårt att lista ut ursprungsinformationen.
'''


# def check_password(username, password):
#     if password[username] == hash(password):
#         return True
#     return False
#
#
# passwords = {'MarHad': hash('bajs')}
# print(passwords['MarHad'])
# check_password('MarHad', passwords)









