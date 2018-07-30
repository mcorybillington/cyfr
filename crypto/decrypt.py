from Crypto.Cipher import AES


class DecryptAES(object):
    def __init__(self):
        self.enc = ""
        self.private_key = ''

    def decrypt(self):
        iv = self.enc[:AES.block_size]
        cipher = AES.new(self.private_key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(self.enc[AES.block_size:])).decode()

    @staticmethod
    def _unpad(s):
        s = s[:-s[-1]]
        return s