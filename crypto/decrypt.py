import base64
from Crypto.Cipher import AES


class DecryptAES(object):
    def __init__(self):
        self.bs = 16
        self.enc = ''
        self.private_key = ''

    def decrypt(self):
        enc = base64.b64decode(self.enc)
        iv = enc[:self.bs]
        cipher = AES.new(self.private_key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[self.bs:])).decode('utf-8')

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]
