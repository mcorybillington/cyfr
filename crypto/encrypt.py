import base64
from Crypto import Random
from Crypto.Cipher import AES


class EncryptAES(object):

    def __init__(self):
        self.plaintext = ''
        self.private_key = ''

    def encrypt(self):
        raw = self._pad(self.plaintext)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.private_key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    @staticmethod
    def _pad(s):
        s = str.encode(s)
        length = 16 - (len(s) % 16)
        s += bytes([length]) * length
        return s


