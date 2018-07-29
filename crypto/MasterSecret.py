from Crypto import Random
from Crypto.PublicKey import RSA


class Keys:

    def __init__(self):
        pass

    @staticmethod
    def generate_keys():
        # RSA modulus length must be a multiple of 256 and >= 1024
        modulus_length = 256 * 8  # use larger value in production
        private_key = RSA.generate(modulus_length, Random.new().read)
        #public_key = private_key.publickey()
        private_key = repr(private_key)
        #public_key = repr(public_key)
        return private_key

