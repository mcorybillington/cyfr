from base64 import b64decode
from Crypto.Cipher import AES


class DecryptAES(object):
    def __init__(self):
        self.bs = 16
        self.enc = ''
        self.private_key = ''

    def decrypt(self):
        enc = b64decode(self.enc)
        iv = enc[:16]
        cipher = AES.new(self.private_key, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(enc[16:])).decode('utf-8')

    @staticmethod
    def unpad(s):
        return s[:-ord(s[len(s) - 1:])]
