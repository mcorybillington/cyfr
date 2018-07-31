import socket
from PyQt5.QtCore import QThread, pyqtSignal


class ChatListener(QThread):
    status = pyqtSignal(str, str)

    def __init__(self):
        QThread.__init__(self)
        self.ip = self.get_ip_addr()
        self.port = 5004
        self.message = ''
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @staticmethod
    def get_ip_addr():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_addr = s.getsockname()[0]
        s.close()
        return ip_addr

    def run(self):
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_socket.bind((self.ip, self.port))
        self.listen_socket.listen(1)
        while True:
            connection, address = self.listen_socket.accept()
            self.message = connection.recv(2048).decode('utf-8')
            address = str(address).split(',')[0].strip('[]\'(')
            self.status.emit(address, self.message)
