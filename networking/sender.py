import socket
from PyQt5.QtCore import QThread, pyqtSignal


class ChatSender(QThread):
    finished = pyqtSignal(str, str)

    def __init__(self):
        QThread.__init__(self)
        self.address = ''
        self.port = 5004
        self.message = ''
        self.send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.send_socket.connect((self.address, self.port))
        self.send_socket.sendall(self.message.encode('utf-8'))
        self.finished.emit("You", self.message)
