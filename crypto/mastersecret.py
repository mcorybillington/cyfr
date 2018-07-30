from Crypto import Random
from Crypto.PublicKey import RSA


class MasterSecret:

    def __init__(self):
        pass

    @staticmethod
    def generate_keys():
        modulus_length = 256 * 8
        private_key = RSA.generate(modulus_length, Random.new().read)
        private_key = repr(private_key)
        return private_key

