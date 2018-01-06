#!/usr/bin/env python

from cryptography.fernet import Fernet
import random
from diffhellman import private_key
import sys

lock, unlock = private_key()


def user_input_file():
    with open('testfile.txt') as f:
        in_file = f.read()
        return in_file


def user_input_text():
    text = input('Enter text: ')
    return text


def print_file(y):
    for line in y:
        print(line)


def encrypt(y, f):
    num2 = random.randint(1,9)
    y = y.encode('UTF-8')
    message = Fernet(f).encrypt(y)
    for i in range(1,num2):
        message = Fernet(f).encrypt(message)
    return message, num2


def decrypt(y, f, num2):
    for i in range(1,num2):
        y = Fernet(f).decrypt(y)
    y = Fernet(f).decrypt(y)
    y = y.decode('utf-8')
    num2 = 0
    return y, num2


def send():
    user_input = user_input_text()
    print('')
    print("Sent: ", user_input)
    print('')
    secret, timing = encrypt(user_input, lock)
    print("[ Encrypted message: ]")
    print(secret)
    print('')
    plain, timing = decrypt(secret, unlock, timing)
    print("Received: ", plain)
    print('')
    control()


def control():
    char = input("Press y to send a message: " )
    char = char.lower()
    if char != 'y':
        sys.exit(0)
    else:
        send()


def main():
    print("Encrypted messaging app")
    print('')
    control()


if __name__ == "__main__":
    main()

'''
def keygen():
    key = Fernet.generate_key()
    f = Fernet(key)
    print(f)
    return f


'''

