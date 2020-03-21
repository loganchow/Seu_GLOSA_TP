# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui

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
        self.numPvButton = QtWidgets.QPushButton("Enter",self.groupboxBasic)



        # 提示标签的定位
        self.labelEvspeed.setGeometry(QtCore.QRect(10, 40, 150, 31))
        self.labelPvspeed.setGeometry(QtCore.QRect(10, 90, 150, 31))
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
        self.numPvButton.setGeometry(QtCore.QRect(230, 330, 100, 31))




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

#        self.left_upper = QtWidgets.QVBoxLayout()
#        self.left_upper.addWidget(self.labelEvspeed)
#        self.left_upper.addWidget(self.evSpeed)
#        self.left_upper.addWidget(self.labelPvspeed)
#        self.left_upper.addWidget(self.pvSpeed)
#        self.left_upper.addWidget(self.labelLimitspeed)
#        self.left_upper.addWidget(self.limitSpeed)
#        self.left_upper.addWidget(self.labelDis2stpline)
#        self.left_upper.addWidget(self.dis2Stop)
#        self.left_upper.addWidget(self.labelInterID)
#        self.left_upper.addWidget(self.interID)
#        self.left_upper.addWidget(self.labelNumpv)
#        self.left_upper.addWidget(self.numPv)
#        self.left_upper.addWidget(self.numPvButton)

#        self.left_upper.addStretch(1)

#        self.groupboxBasic.setLayout(self.left_upper)
        



        ## 中间一栏
        self.groupboxCenter = QtWidgets.QGroupBox(self)
        self.groupboxCenter.setTitle("Advice Speed")
        self.groupboxCenter.setGeometry(QtCore.QRect(490, 10, 250, 400))

        self.lowerSpeed = QtWidgets.QLCDNumber(self.groupboxCenter)
        self.upperSpeed = QtWidgets.QLCDNumber(self.groupboxCenter)

        fontLcd = QtGui.QFont()
        fontLcd.setFamily(u"Arial Black")
        fontLcd.setPointSize(10)

        self.upperSpeed.setGeometry(QtCore.QRect(20, 70, 171, 131))
        self.lowerSpeed.setGeometry(QtCore.QRect(20, 240, 171, 131))

        self.lowerSpeed.setFont(fontLcd)
        self.upperSpeed.setFont(fontLcd)




        # self.center_upper = QtWidgets.QVBoxLayout()
        # self.center_upper.addWidget(self.upperSpeed)
        # self.center_upper.addWidget(self.lowerSpeed)

        # self.groupboxCenter.setLayout(self.center_upper)

        # 右侧一栏
        self.groupboxSignal = QtWidgets.QGroupBox(self)
        self.groupboxSignal.setTitle("Signal State")
        self.groupboxSignal.setGeometry(QtCore.QRect(750, 10, 360, 400))

        
        # self.picLeftturn = QtWidgets.QLabel(self.groupboxSignal)
        # self.picStraightturn = QtWidgets.QLabel(self.groupboxSignal)
        # self.picRightturn = QtWidgets.QLabel(self.groupboxSignal)



        # self.right_upper = QtWidgets.QVBoxLayout()
        # self.right_upper.addWidget(self.picLeftturn)
        # self.right_upper.addWidget(self.picStraightturn)
        # self.right_upper.addWidget(self.picRightturn)

        # self.groupboxRight.setLayout(self.right_upper)


        # 总布局
        # self.layout = QtWidgets.QHBoxLayout()

        # self.layout.addWidget(self.groupboxBasic)
        # self.layout.addWidget(self.groupboxCenter)
        # self.layout.addWidget(self.groupboxRight)

        # Set the layout to the QWidget
        # self.setLayout(self.layout)
