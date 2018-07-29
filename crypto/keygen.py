#!/usr/bin/env python

import secrets
import random
import math


def random_num():
    rand = secrets.randbits(2048)
    return rand


def is_prime(n):
    if n < 2 or n % 2 == 0:
        return False
    if n == 2 or n == 3:
        return True
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5

    while f <= r:
        print('\t', f)
    if n % f == 0:
        return False
    if n % (f+2) == 0:
        return False
    f += 6
    return True


def generate():
    while False:
        global num
        num = random_num()
        is_prime(num)
    return num


generate()
