import socket
import threading


class ChatListener(threading.Thread):
    port = 4430
    any = '0.0.0.0'

    def __init__(self):
        threading.Thread.__init__(self)
        self.port = None

    def run(self):
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.bind((any, self.port))
        listen_socket.listen(1)

        while True:
            connection, address = listen_socket.accept()

            print("Established connection with: ", address)

            message = connection.recv(BUFFER_SIZE)
            print("Them: ", message)


class ChatSender(threading.Thread):

    def __init__(self, ip):
        threading.Thread.__init__(self)
        self.address = ip
        self.port = None

    def run(self):
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        send_socket.connect((self.address, self.port))

        while True:

            message = input("You: ")

            if message.lower() == "quit":
                break
            else:
                try:
                    send_socket.sendall(message)
                except:
                    Exception