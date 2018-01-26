#!/usr/bin/env python

import numpy as np
import hashlib
import base64
import secrets
from publicBase_Modulus import PublicBaseModulus
import time


class MasterSecret:

    def __init__(self):
        pass

    @staticmethod
    def modular_pow(base, exponent, modulus):
        if modulus == 1:
            return np.zeros_like(base)
        result = np.ones_like(base)
        base = base % modulus
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent = exponent >> 1
            base = (base * base) % modulus
        return result

    @staticmethod
    def generate_key(sent_key, private_key_in, public_mod):
        key = (hashlib.sha256(str(MasterSecret.modular_pow(sent_key, private_key_in, public_mod)).encode('utf-8')).hexdigest())
        key = base64.urlsafe_b64encode(bytes((hashlib.md5(str(key).encode('utf-8')).hexdigest()).encode('utf-8')))
        return key
        # was line 2: key = (hashlib.md5(str(key).encode('utf-8')).hexdigest())

    @staticmethod
    def private_key():
        public_mod = PublicBaseModulus.generate_prime_number()
        public_base = PublicBaseModulus.generate_prime_number()

        # if public_base == public_mod:
        #     print("same base/mod")
        # if public_base != public_mod:
        #     print("not the same base/mod")
        # *test code* print("\n\n", "public base:\n", public_base, "\n\n", "public mod:\n",  public_mod, "\n\n")

        alice_private = secrets.randbits(2048)
        bob_private = secrets.randbits(2048)

        # print("bob private: \n", bob_private, "\nAlice Private: \n", alice_private)

        start_time = time.time()
        alice_sends = MasterSecret.modular_pow(public_base, alice_private, public_mod)
        bob_sends = MasterSecret.modular_pow(public_base, bob_private, public_mod)
        lock = MasterSecret.generate_key(alice_sends, bob_private, public_mod)
        unlock = MasterSecret.generate_key(bob_sends, alice_private, public_mod)
        # print("Time to generate keys: %s seconds" % (time.time() - start_time))
        return lock, unlock

    # lockInt = hashlib.sha256(str(modular_pow(aliceSends, bobPrivate, publicMod)).encode('utf-8')).hexdigest()
    # lockInt = hashlib.md5(str(lockInt).encode('utf-8')).hexdigest()
    # unlockInt = hashlib.sha256(str(modular_pow(bobSends, alicePrivate, publicMod)).encode('utf-8')).hexdigest()
    # unlockInt = hashlib.md5(str(unlockInt).encode('utf-8')).hexdigest()
    # lock = base64.urlsafe_b64encode(bytes(lockInt.encode('utf-8')))
    # unlock = base64.urlsafe_b64encode(bytes(unlockInt.encode('utf-8')))
