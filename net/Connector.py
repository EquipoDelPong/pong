"""
This file defines how the connection betwen the pairs is done. It searches for
other pong games inside the network.
"""

import socket

port = 5894

class Connector:

    def __init__(self):
        self.sock = None
        print("Creating Connector")


    def connect(self):
        self.__status = "CONECTED"

    
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



obj = Connector()
obj.searchPair()
