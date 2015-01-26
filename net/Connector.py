"""
This file defines how the connection betwen the pairs is done. It searches for
other pong games inside the network.
"""

import socket
from Server import *
from Client import *
from net import *

class Connector:

    def __init__(self):
        self.server = None
        self.client = None
        print("Creating Connector")


    def connect(self, ip):
        self.client = Client()
        self.__status = "CONECTED"

    def waitConnection(self):
        self.server = Server(getLocalIp(), PORT)
        

    #not implemented yet *** ERROR *** 
    def searchPair(self):
        print("Searching for pairs inside the network")
        for ip in range(1, 253):
            print("trying with "+str(ip))
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = self.sock.connect_ex(('10.0.2.'+str(ip), port))
            if result == 0:
                print("open")
            self.sock.close()
        return ""


    #it's usefull to know my local ip, I didn't found a simplest and clearest
    #way, but for the game is very usefull
    def getLocalIp():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))
        return str(s.getsockname()[0])


obj = Connector()
obj.searchPair()
