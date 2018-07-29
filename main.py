import sys
import socket
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
from networking.listener import ChatListener
from networking.sender import ChatSender


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


def main():
    app = QApplication(sys.argv)
    w = AppWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

