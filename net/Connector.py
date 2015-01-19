"""
This file defines how the connection betwen the pairs is done. It searches for
other pong games inside the network.
"""

import socket

port = 5894

class Connector:

    def __init__(self):
		self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Creating Connector")


    def connect(self):
        self.__status = "CONECTED"

    
    def searchPair(self):
        for ip in range(0, 253)
			result = __socket.connect_ex(('192.168.1.'ip, port))
			if result == 0:
				print('open')
				__socket.close()

            print('%s' % ip)
        return "192.168.1.13"

