# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
import random

class Widget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        # 左侧一栏
        self.groupboxBasic = QtWidgets.QGroupBox(self)
        self.groupboxBasic.setTitle("Basic")
        self.groupboxBasic.setGeometry(QtCore.QRect(30, 10, 450, 500))

        # 提示标签的实例化
        self.labelEvspeed = QtWidgets.QLabel("Ego Speed: ",self.groupboxBasic)
        self.labelPvspeed = QtWidgets.QLabel("Pre Speed: ",self.groupboxBasic)
        self.labelLimitspeed = QtWidgets.QLabel("Limit Speed: ",self.groupboxBasic)
        self.labelDis2stpline = QtWidgets.QLabel("Dis2Stopline: ",self.groupboxBasic)
        self.labelInterID = QtWidgets.QLabel("IntersectionID: ",self.groupboxBasic)
        self.labelNumpv = QtWidgets.QLabel("Num of Preceeding: ",self.groupboxBasic)
        self.labelPositionEv = QtWidgets.QLabel("EV Position: ",self.groupboxBasic)

        # 显示值标签的实例化
        self.evSpeed = QtWidgets.QLabel("0.00",self.groupboxBasic)
        self.pvSpeed = QtWidgets.QLabel("0.00",self.groupboxBasic)
        self.limitSpeed = QtWidgets.QLabel("0.00",self.groupboxBasic)
        self.dis2Stop = QtWidgets.QLabel("0.00",self.groupboxBasic)
        self.interID = QtWidgets.QLabel("000000",self.groupboxBasic)

        self.numPv = QtWidgets.QDoubleSpinBox(self.groupboxBasic)
        self.buttonNumPv = QtWidgets.QPushButton("Enter",self.groupboxBasic)

        # 提示标签的定位
        self.labelEvspeed.setGeometry(QtCore.QRect(10, 30, 150, 31))
        self.labelPvspeed.setGeometry(QtCore.QRect(10, 80, 150, 31))
        self.labelLimitspeed.setGeometry(QtCore.QRect(10, 130, 150, 31))
        self.labelDis2stpline.setGeometry(QtCore.QRect(10, 180, 150, 31))
        self.labelInterID.setGeometry(QtCore.QRect(10, 230, 200, 31))
        self.labelNumpv.setGeometry(QtCore.QRect(10, 280, 250, 31))
        self.labelPositionEv.setGeometry(QtCore.QRect(10, 380, 250, 31))

        # 显示标签的定位
        self.evSpeed.setGeometry(QtCore.QRect(230, 30, 100, 31))
        self.pvSpeed.setGeometry(QtCore.QRect(230, 80, 100, 31))
        self.limitSpeed.setGeometry(QtCore.QRect(230, 130, 100, 31))
        self.dis2Stop.setGeometry(QtCore.QRect(230, 180, 100, 31))
        self.interID.setGeometry(QtCore.QRect(230, 180, 100, 31))
        self.interID.setGeometry(QtCore.QRect(230, 230, 100, 31))

        self.numPv.setGeometry(QtCore.QRect(20, 330, 100, 31))
        self.buttonNumPv.setGeometry(QtCore.QRect(230, 330, 100, 31))


        # 提示标签的样式设置
        fontLabel = QtGui.QFont()
        fontLabel.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        fontLabel.setPointSize(14)

        self.labelEvspeed.setFont(fontLabel)
        self.labelPvspeed.setFont(fontLabel)
        self.labelLimitspeed.setFont(fontLabel)
        self.labelDis2stpline.setFont(fontLabel)
        self.labelInterID.setFont(fontLabel)
        self.labelNumpv.setFont(fontLabel)
        self.labelPositionEv.setFont(fontLabel)

        self.evSpeed.setFont(fontLabel)
        self.pvSpeed.setFont(fontLabel)
        self.limitSpeed.setFont(fontLabel)
        self.dis2Stop.setFont(fontLabel)
        self.interID.setFont(fontLabel)


        ## 中间一栏
        self.groupboxCenter = QtWidgets.QGroupBox(self)
        self.groupboxCenter.setTitle("Advice Speed")
        self.groupboxCenter.setGeometry(QtCore.QRect(490, 10, 250, 500))

        self.lowerSpeed = QtWidgets.QLCDNumber(self.groupboxCenter)
        self.upperSpeed = QtWidgets.QLCDNumber(self.groupboxCenter)

        fontLcd = QtGui.QFont()
        fontLcd.setFamily(u"Arial Black")
        fontLcd.setPointSize(10)

        self.upperSpeed.setGeometry(QtCore.QRect(20, 70, 171, 131))
        self.lowerSpeed.setGeometry(QtCore.QRect(20, 240, 171, 131))

        self.lowerSpeed.setFont(fontLcd)
        self.upperSpeed.setFont(fontLcd)

        # 右侧一栏
        self.groupboxSignal = QtWidgets.QGroupBox(self)
        self.groupboxSignal.setTitle("Signal State")
        self.groupboxSignal.setGeometry(QtCore.QRect(750, 10, 360, 500))

        self.leftSignal = QtWidgets.QLabel(self.groupboxSignal)
        self.straightSignal = QtWidgets.QLabel(self.groupboxSignal)
        self.rightSignal = QtWidgets.QLabel(self.groupboxSignal)

        self.lcdTimeLeftSignal = QtWidgets.QLCDNumber(self.groupboxSignal)
        self.lcdTimeStraightSignal = QtWidgets.QLCDNumber(self.groupboxSignal)
        self.lcdTimeRightSignal = QtWidgets.QLCDNumber(self.groupboxSignal)

        self.lcdTimeLeftSignal.setGeometry(QtCore.QRect(20,240,64,64))
        self.lcdTimeStraightSignal.setGeometry(QtCore.QRect(140,240,64,64))
        self.lcdTimeRightSignal.setGeometry(QtCore.QRect(270,240,64,64))

        fontLcdSmall = QtGui.QFont()
        fontLcdSmall.setFamily(u"Arial Black")
        fontLcdSmall.setPointSize(10)

        self.lcdTimeLeftSignal.setFont(fontLcdSmall)
        self.lcdTimeStraightSignal.setFont(fontLcdSmall)
        self.lcdTimeRightSignal.setFont(fontLcdSmall)

        # 总布局

        # 左侧栏显示功能实现
        
        self.buttonNumPv.clicked.connect(self.start_demo())

    @QtCore.Slot()
    def start_demo(self):
        self.data_gene()
        self.show_evSpeed()
        self.show_hvSpeed()
        self.show_limitSpeed()

    
    # @QtCore.Slot()
    # def play(self):
    #     listSpeed = data_generator_demo.data_gene()


    # @QtCore.Slot()
    # def show_upperSpeed(self):
    #     for j in range(1,5):
    #         self.upperSpeed.display(j)
    #         QtWidgets.QApplication.processEvents()
    #         time.sleep(1)

    # @QtCore.Slot()
    # def show_lowerSpeed(self):
    #     for j in range(1,5):
    #         self.upperSpeed.display(j)
    #         QtWidgets.QApplication.processEvents()
    #         time.sleep(1)

    @QtCore.Slot()
    def show_evSpeed(self):
        listSpeed = self.data_gene()
        j = listSpeed[0]
        self.evSpeed.setText(str(j))
        QtWidgets.QApplication.processEvents()

    @QtCore.Slot()
    def show_hvSpeed(self):
        listSpeed = self.data_gene()
        j = listSpeed[1]
        self.pvSpeed.setText(str(j))
        QtWidgets.QApplication.processEvents()
            
    @QtCore.Slot()
    def show_limitSpeed(self):
        listSpeed = self.data_gene()
        j = listSpeed[2]
        self.limitSpeed.setText(str(j))
        QtWidgets.QApplication.processEvents()

    @QtCore.Slot()
    def data_gene(self):
        self.listSpeed = []
        self.limit = 60
        # for i in range(0,100):
        self.ev = random.randint(0,60)
        self.hv = random.randint(0,60)
        self.listSpeed.append(self.ev)
        self.listSpeed.append(self.hv)
        self.listSpeed.append(self.limit)
        return self.listSpeed
