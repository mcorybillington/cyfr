import socket
import sys

###########
HOST = '25.0.18.52'
PORT = 9999
###########

name = input("Enter your name: ")
s = socket.socket()
s.connect((HOST, PORT))


def receive_message():
    while True:
        data = s.recv(1024)
        if not data:
            sys.exit(0)
        print(data)


def send_message():
    while 1:
        message = input("Message: ")
        s.send("{}: {}".format(name, message).encode('utf-8'))


Thread(target=receive_message()).start()