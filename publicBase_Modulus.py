import secrets
from primeTest import probably_prime


def generate_public_modulus():
    # print("Generating public Modulus")
    public_modulus = secrets.randbits(2048)
    if not probably_prime(public_modulus):
        public_modulus = secrets.randbits(2048)
    # print("test publicModulus")
    return public_modulus


def generate_public_base():
    # print("Generating public Base")
    public_base = secrets.randbits(2048)
    if not probably_prime(public_base):
        public_base = secrets.randbits(2048)
    # print("test publicBase")
    return public_base

