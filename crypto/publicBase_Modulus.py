import sys
import secrets
from random import randrange

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


class PublicBaseModulus:

    def __init__(self):
        pass

    def probably_prime(self):
        """Return True if self passes k rounds of the Miller-Rabin primality
        test (and is probably prime). Return False if n is proved to be
        composite.

        """
        # small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        if self < 2:
            return False
        for p in small_primes:
            # if self < p * p:
            #    return True
            if self % p == 0:
                return False
        r, s = 0, self - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(10):
            a = randrange(2, self - 1)
            x = pow(a, s, self)
            if x == 1 or x == self - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, self)
                if x == self - 1:
                    break
            else:
                # print("Not prime")
                return False
        # print("It's prime")
        return True

    @staticmethod
    def generate_prime_number():
        # print("Generating public Base")
        while True:
            big_number = secrets.randbits(2048)
            if PublicBaseModulus.probably_prime(big_number):
                # print("test generateprimenumber")
                return big_number


