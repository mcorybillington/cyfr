from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes


class KeyExchange(object):
    def __init__(self):
        self.private_key = ''
        self.peer_public_key = ''
        self.shared_key = ''

    def get_shared_key(self):
        return self.private_key.exchange(ec.ECDH(), self.peer_public_key)

    def get_derived_key(self):
        return HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'handshake data',
            backend=default_backend()
        ).derive(self.shared_key)