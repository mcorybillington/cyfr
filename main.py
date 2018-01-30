#!/usr/bin/env python

# import socket  # working progress...
# from cryptography.fernet import Fernet
from cryptoFunctions import SendCipherText
from diffhellman import MasterSecret
import sys, threading
from PyQt5 import uic, QtWidgets, QtGui, QtCore
# import time  # for testing


class AppWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        uic.loadUi('cyfr2_gui.ui', self)
        self.show()
        self.sendButton.clicked.connect(self.send_msg)

    def send_msg(self):
        message = str(self.msgInputTextBox.toPlainText())
        self.textBrowser.append("they:" + message)
        self.msgInputTextBox.setText("")

#    def generate_master_secret(self):


app = QtWidgets.QApplication(sys.argv)
w = AppWindow()
sys.exit(app.exec_())

# start_time = time.time()
# lock = b'NDc5Mzg1MjYzYTlmOTNlOGZiZjZkNDFhYWM0MDljYzE='
# unlock = b'NDc5Mzg1MjYzYTlmOTNlOGZiZjZkNDFhYWM0MDljYzE='
# print("Time to generate keys: %s seconds" % (time.time() - start_time))

# lock, unlock = MasterSecret.private_key()
#
#
# def control():
#         char = input("Press y to send a message: ")
#         char = char.lower()
#         if char != 'y':
#             sys.exit(0)
#         else:
#             message = input('Enter text: ')
#             SendCipherText.send(message, lock)
#             control()
#
#
# def main():
#         print("Encrypted messaging app")
#         print('')
#         control()
#
#
# if __name__ == "__main__":
#     main()
#
'''
def keygen():
    key = Fernet.generate_key()
    f = Fernet(key)
    print(f)
    return f


'''

