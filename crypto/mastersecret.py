from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec


class MasterSecret:

    def __init__(self):
        self.private_key = self.gen_private_key()
        self.public_key = self.gen_public_key()

    def gen_private_key(self):
        return ec.generate_private_key(ec.SECP521R1, default_backend())

    def gen_public_key(self):
        return self.private_key.public_key()


