from cryptography.fernet import Fernet


class CryptoThings:

    def __init__(self):
        pass

    def user_input_file(self):
        with open(self) as f:
            in_file = f.read()
            return in_file

    @staticmethod
    def user_input_text():
        text = input('Enter text: ')
        return text

    def print_file(self):
        for line in self:
            print(line)

    def encrypt(self, key):
        return Fernet(key).encrypt(self.encode('UTF-8'))

    def decrypt(self, key):
        return Fernet(key).decrypt(self).decode('UTF-8')

    def send(self, key):
        return Fernet(key).encrypt(self, key)


