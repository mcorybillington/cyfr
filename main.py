#!/usr/bin/env python

import sys
import threading
import socket
from PyQt5 import uic, QtWidgets, QtGui, QtCore
# import time  # for testing


class AppWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        uic.loadUi('cyfr2_gui.ui', self)
        self.msgInputLineEdit.setPlaceholderText("Send cyfr message")
        self.chat_listener = ChatListener()
        self.chat_listener.start()
        self.chat_sender = ChatSender()
        self.sendButton.setEnabled(False)
        self.msgInputLineEdit.textChanged.connect(self.check)
        self.sendButton.clicked.connect(self.send_msg)
        self.msgInputLineEdit.returnPressed.connect(self.click)
        # self.connectButton.clicked.connect(self.connect)
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

    def receive(self):
        chat_listener = ChatListener()
        chat_listener.start()
        message = chat_listener.run()
        self.textBrowser.append("Them: " + message)

    def key_exchange(self):
        ip = self.ipLineEdit.text()
        chat_sender = ChatSender(ip)
        chat_sender.port = 80
        chat_sender.address = ip
        self.textBrowser.append("Exchanging Keys...")
        chat_sender.start()
        self.textBrowser.append("Key exchange complete!")

    def send_msg(self):
        ip = self.ipLineEdit.text()
        message = self.msgInputLineEdit.text()
        chat_sender = ChatSender(ip, message)
        chat_sender.run()
        self.textBrowser.append("Me: " + message)
        self.msgInputLineEdit.setText('')


class ChatListener(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.ip = ''
        self.port = 5004

    def run(self):
        print("hi")
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind((self.ip, self.port))
        listen_socket.listen(1)
        connection, address = listen_socket.accept()
        message = connection.recv(2048)


class ChatSender(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.address = ''
        self.port = 5001
        self.message = ''

    def send(self):
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        send_socket.connect((self.address, self.port))
        send_socket.sendall(self.message)


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = AppWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

