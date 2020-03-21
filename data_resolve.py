# This Python file uses the following encoding: utf-8
from PySide2 import QtWidgets

class data_resolve:
    def __init__(self,data):
        self.lenm=[]
        self.data_raw=[]
        self.len_msg=[]
        self.payload=[]
    def data_veri(self,data):
        self.lenm = [0,0]
        self.lenm[0] = self.data_raw[5]
        self.lenm[1] = self.data_raw[6]
        self.len_msg = int(self.lenm[1]*256+self.lenm[0])
        self.payload = self.data_raw[8:-1]
        return self.payload,self.len_msg
