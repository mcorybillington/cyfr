from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from crypto.mastersecret import MasterSecret


class KeyExchange(object):
    def __init__(self, p_key, r_pub_key):
        self.private_key = p_key
        self.recv_public_key = r_pub_key
        self.shared_key = self.get_shared_key()

    def get_shared_key(self):
        return self.private_key.exchange(self.recv_public_key)

    def get_derived_key(self):
        return HKDF(
                algorithm=hashes.SHA256(),
                length=32,
                salt=None,
                info=b'handshake data',
                backend=default_backend()
            ).derive(self.shared_key)