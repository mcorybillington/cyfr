#!/usr/bin/env python

import numpy as np
import hashlib
import base64
import secrets
from publicBase_Modulus import generate_public_modulus, generate_public_base


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


def generate_key(sent_key, private_key, public_mod):
    key = (hashlib.sha256(str(modular_pow(sent_key, private_key, public_mod)).encode('utf-8')).hexdigest())
    key = base64.urlsafe_b64encode(bytes((hashlib.md5(str(key).encode('utf-8')).hexdigest()).encode('utf-8')))
    return key
    # was line 2: key = (hashlib.md5(str(key).encode('utf-8')).hexdigest())


def private_key():
    public_mod = generate_public_modulus()
    public_base = generate_public_base()
    # *test code* print("\n\n", "public base:\n", public_base, "\n\n", "public mod:\n",  public_mod, "\n\n")

    alice_private = secrets.randbits(2048)
    bob_private = secrets.randbits(2048)

    alice_sends = modular_pow(public_base, alice_private, public_mod)
    bob_sends = modular_pow(public_base, bob_private, public_mod)
    lock = generate_key(alice_sends, bob_private, public_mod)
    unlock = generate_key(bob_sends, alice_private, public_mod)
    return lock, unlock

    # lockInt = hashlib.sha256(str(modular_pow(aliceSends, bobPrivate, publicMod)).encode('utf-8')).hexdigest()
    # lockInt = hashlib.md5(str(lockInt).encode('utf-8')).hexdigest()
    # unlockInt = hashlib.sha256(str(modular_pow(bobSends, alicePrivate, publicMod)).encode('utf-8')).hexdigest()
    # unlockInt = hashlib.md5(str(unlockInt).encode('utf-8')).hexdigest()
    # lock = base64.urlsafe_b64encode(bytes(lockInt.encode('utf-8')))
    # unlock = base64.urlsafe_b64encode(bytes(unlockInt.encode('utf-8')))
