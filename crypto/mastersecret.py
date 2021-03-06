from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey


class MasterSecret:
    def __init__(self):
        self.private_key = self.gen_private_key()
        self.public_key = self.gen_public_key()

    @staticmethod
    def gen_private_key():
        return X25519PrivateKey.generate()

    def gen_public_key(self):
        return self.private_key.public_key()


