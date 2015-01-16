"""
This file defines how the connection betwen the pairs is done. It searches for
other pong games inside the network.
"""

from netaddr import *
import pprint

class Connector:

    def __init__(self):
        print("Creating Connector")


    def connect(self):
        self.__status = "CONECTED"

    
    def searchPair(self):
        for ip in IPNetwork('10.0.2.15/24').iter_hosts():
            print('%s' % ip)
        return "192.168.1.13"

