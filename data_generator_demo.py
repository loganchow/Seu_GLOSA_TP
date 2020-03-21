# This Python file uses the following encoding: utf-8

from PySide2 import QtWidgets
import random

class data_generator_demo:
    def __init__(self):
        self.evSpeed = 0
        self.hvSpeed = 0
        self.limitSpeed = 60
        self.listSpeed = []
        def data_gene(self):
            for i in range(0,100):
                self.evSpeed = random.randint(0,60)
                self.hvSpeed = random.randint(0,60)
                self.listSpeed.append(self.evSpeed)
                self.listSpeed.append(self.hvSpeed)
                self.listSpeed.append(self.limitSpeed)
                return self.listSpeed

