#!/usr/bin/env python

# import socket  # working progress...
# from cryptography.fernet import Fernet
from cryptoFunctions import SendCipherText
from diffhellman import MasterSecret
import sys
# import time  # for testing

# start_time = time.time()
# lock = b'NDc5Mzg1MjYzYTlmOTNlOGZiZjZkNDFhYWM0MDljYzE='
# unlock = b'NDc5Mzg1MjYzYTlmOTNlOGZiZjZkNDFhYWM0MDljYzE='
# print("Time to generate keys: %s seconds" % (time.time() - start_time))

lock, unlock = MasterSecret.private_key()


def control():
        char = input("Press y to send a message: ")
        char = char.lower()
        if char != 'y':
            sys.exit(0)
        else:
            message = input('Enter text: ')
            SendCipherText.send(message, lock)
            control()


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

