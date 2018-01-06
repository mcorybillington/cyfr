#!/usr/bin/env python

from cryptography.fernet import Fernet
import random
from diffhellman import privateKey
import sys

def userInputFile():
    with open('testfile.txt') as f:
        inFile = f.read()
        return inFile

def userInputText():
    text = input('Enter text: ')
    return text

def printFile(y):
    for line in y:
        print(line)

def keygen():
    key = Fernet.generate_key()
    f = Fernet(key)
    print(f)
    return f

def encrypt(y, f):
    num2 = random.randint(1,9)
    y = y.encode('UTF-8')
    message = Fernet(f).encrypt(y)
    for i in range(1,num2):
        message = Fernet(f).encrypt(message)
    return message, num2

def decrypt(y, f, num2):
    for i in range(1,num2):
        y=Fernet(f).decrypt(y)
    y = Fernet(f).decrypt(y)
    y = y.decode('UTF-8')
    num2 = 0
    return y, num2


def send():
    userInput = userInputText()
    print('')
    print("Sent: ")
    print(userInput)
    print('')
    lock, unlock = privateKey()
    secret, timing = encrypt(userInput, lock)
    print("[ Encrypted message: ]")
    print(secret)
    print('')
    plain, timing = decrypt(secret, unlock, timing)
    print("Received: ")
    print(plain)
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
