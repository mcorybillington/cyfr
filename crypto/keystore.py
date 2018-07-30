class FileOps():
    def __init__(self):
        self.identity = ''
        self.key = ''

    def write_new(self):
        with open("keys.txt", "r+") as f:
            f.write('{} {}'.format(self.identity, self.key))

    def check(self):
        with open("keys.txt", "r") as f:
            for line in f:
                if self.identity in line:
                    return True

    def return_key(self):
        with open("keys.txt", "r"):
            for line in f:
                id, key = line.split()
                if id == self.identity:
                    return key

