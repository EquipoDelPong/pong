"""
This class allow us to make a Game server, it's necesary to connect with
other Game instance, (every instance will have a client and a server, server
will have a defined port = 5894) In fact a Game needs a Connector object and 
a Connector class will use Server class
"""


import socket
import SocketServer
from net import *


class Server():

    def __init__(self, ip, port):
        self.ipLocal = ip
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((ipLocal, port))
        self.socket.listen(5)
        print("Waiting for connection...")
        self.client, self.data = self.socket.accept()
        self.Connected()


    def Connected(self):
        print("Client connected "+str(self.data))

    def Send(self, msg):
        self.client.send(str(msg))

    def Receive(self):
        return self.client.recv(MSG_SIZE)

    def Close(self):
        self.socket.close()
