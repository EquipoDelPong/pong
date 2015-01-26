"""
Client class define how a client will be comunicated with a server
"""

from net import *
import socket
import time


class Client():

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def Connect(self, ip, port):

        try:
            self.socket.connect((ip, port))
            print("Connection initialized with "+str(ip))
            self.connect = True
        except:
            print("I couldn't connected with the server in "+str(ip))

    def Send(self, msg):
        self.socket.send(str(msg))

    def Receive(self):
        return self.socket.recv(MSG_SIZE)

    def Close(self):
        self.connected = False
        self.socket.close()
