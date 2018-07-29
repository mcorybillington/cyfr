import base64
import hashlib
import sys
from MasterSecret import Keys
from Crypto import Random
from Crypto.Cipher import AES


class AESCipher(object):

    def __init__(self, priv_key):
        self.bs = 256
        # self.public_key = hashlib.sha256(pub_key.encode()).digest()
        self.private_key = hashlib.sha256(priv_key.encode()).digest()
        # self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.private_key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.private_key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode()

    @staticmethod
    def _pad(s):
        s = str.encode(s)
        length = 16 - (len(s) % 16)
        s += bytes([length]) * length
        return s

    @staticmethod
    def _unpad(s):
        s = s[:-s[-1]]
        return s

    def __repr__(self):
        return AESCipher()


while True:

    #private_key = repr(secrets.randbelow(64))
    private_key = Keys.generate_keys()
    cipher = AESCipher(private_key)
    plaintext = input("Enter text: ")
    if plaintext == "q" or plaintext == "Q" or plaintext == "exit":
        print("\nbye")
        sys.exit()
    cipher_text = cipher.encrypt(plaintext)
    print("\nEncrypted: ", cipher_text, "\n")
    plaintext2 = cipher.decrypt(cipher_text)
    print("Decrypted: ", plaintext2, "\n\n")

