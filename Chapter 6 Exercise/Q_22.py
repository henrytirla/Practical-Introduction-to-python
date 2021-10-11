from sys import exit
from itertools import zip_longest

def encryption(message):
    even_enc = ''
    odd_enc = ''
    for i in range(len(message)):
        if i % 2 == 0:
            even_enc += message[i]
        else:
            odd_enc += message[i]
    encrypt = even_enc + odd_enc
    decryption(encrypt)        

def decryption(encrypt):
    decrypt = ''
    str_len = len(encrypt)
    if str_len % 2 == 0:
        i = int(str_len / 2)
        even_dec = encrypt[:i]
        odd_dec = encrypt[i:]
    else:
        i = int(((str_len + 1) / 2))
        even_dec = encrypt[:i]
        odd_dec = encrypt[i:]
    for (j, k) in zip_longest(even_dec, odd_dec):
        if j is not None:
            decrypt += j
        if k is not None:
            decrypt += k
        else:
            continue
    show(message, encrypt, decrypt)

def show(message, encrypt, decrypt):
    print('')
    print(f'The original message was {message}.')
    print(f'The encrypted message is {encrypt}.')
    print(f'The decypted message is {decrypt}.')
    print('')
    print('')

if __name__ == '__main__':
    choices = ['1', '2']
    while True:
        print('Welcome to the Simple Encryption and Decryption Program.')
        print('')
        print('Enter "1" to type in a string to encrypt and decrypt.')
        print('Enter "2" to exit the program.')
        print('')
        choice = ''
        while choice not in choices:
            choice = input('Enter your choice (1 or 2): ')
            continue
        if choice == '1':
            message = input('Please input your message: ')
            encryption(message)
        else:
            exit()
