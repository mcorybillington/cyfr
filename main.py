import sys
import socket
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QThread, pyqtSignal


class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        uic.loadUi('cyfr2_gui.ui', self)
        self.msgInputLineEdit.setPlaceholderText("Send cyfr message")
        self.chat_listener = ChatListener()
        self.chat_listener.status.connect(self.print_msg)
        self.chat_listener.start()
        self.sendButton.setEnabled(False)
        self.msgInputLineEdit.textChanged.connect(self.check)
        self.sendButton.clicked.connect(self.send_msg)
        self.msgInputLineEdit.returnPressed.connect(self.click)
        self.setFocus()
        self.show()

    def check(self):
        check = str(self.msgInputLineEdit.text())
        if check == "":
            self.sendButton.setEnabled(False)
        else:
            self.sendButton.setEnabled(True)

    def click(self):
        if self.sendButton.isEnabled():
            self.sendButton.clicked.emit()

    def print_msg(self, sender, val):
        self.textBrowser.append(sender + " : " + val)

    def send_msg(self):
        chat_sender = ChatSender()
        chat_sender.address = self.ipLineEdit.text()
        chat_sender.message = self.msgInputLineEdit.text()
        chat_sender.finished.connect(self.print_msg)
        chat_sender.run()
        while chat_sender.isRunning():
            AppWindow.processevents()
        chat_sender.terminate()
        self.msgInputLineEdit.setText('')


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


def main():
    app = QApplication(sys.argv)
    w = AppWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

