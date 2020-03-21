# This Python file uses the following encoding: utf-8
import sys, socket, time
from PySide2 import QtCore
from PySide2 import QtWidgets

class socket_connect:
    def __init__(self):
        self.port = 15676
        self.ip = '192.168.79.55'
    def connect(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.s.bind((self.ip,self.port))
        self.data,self.addr = self.s.recvfrom(1024)
        time.sleep(0.5)
        return self.data
