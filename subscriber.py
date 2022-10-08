import socket

class Subscriber():
    def __init__(self, address, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((address, port))
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def subscribe(self):
        msg = self.s.recv(1024)
        return msg.decode("utf-8")
