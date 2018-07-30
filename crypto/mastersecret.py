from Crypto import Random
from Crypto.PublicKey import RSA


class MasterSecret:

    def __init__(self):
        self.modulus_length = 4096

    def generate_keys(self):
        private_key = RSA.generate(self.modulus_length, Random.new().read)
        private_key = repr(private_key)
        return private_key

