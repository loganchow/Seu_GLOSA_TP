# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
import random
# import Obu_connect

class Widget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        # 提示标签的样式设置
        fontLabel = QtGui.QFont()
        fontLabel.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        fontLabel.setPointSize(14)
        fontLcd = QtGui.QFont()
        fontLcd.setFamily(u"Arial Black")
        fontLcd.setPointSize(10)
        fontLcdSmall = QtGui.QFont()
        fontLcdSmall.setFamily(u"Arial Black")
        fontLcdSmall.setPointSize(10)
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
        self.labelNumpv = QtWidgets.QLabel("Num of Preceding: ",self.groupboxBasic)
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
        # 样式设置
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


    # 中间一栏
        self.groupboxCenter = QtWidgets.QGroupBox(self)
        self.groupboxCenter.setTitle("Advice Speed")
        self.groupboxCenter.setGeometry(QtCore.QRect(490, 10, 250, 500))

        self.lowerSpeed = QtWidgets.QLCDNumber(self.groupboxCenter)
        self.upperSpeed = QtWidgets.QLCDNumber(self.groupboxCenter)
        self.adviceOperation = QtWidgets.QLabel("BRAKE!",self.groupboxCenter)

        self.upperSpeed.setGeometry(QtCore.QRect(20, 70, 171, 131))
        self.lowerSpeed.setGeometry(QtCore.QRect(20, 240, 171, 131))
        self.adviceOperation.setGeometry(QtCore.QRect(20,410,150,31))

        self.lowerSpeed.setFont(fontLcd)
        self.upperSpeed.setFont(fontLcd)
        self.adviceOperation.setFont(fontLabel)

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

        self.lcdTimeLeftSignal.setFont(fontLcdSmall)
        self.lcdTimeStraightSignal.setFont(fontLcdSmall)
        self.lcdTimeRightSignal.setFont(fontLcdSmall)

    # def testcallback(self,msg):
    #     self.lcdTimeLeftSignal.display(msg.likelyTimeLeft)
    #     self.lcdTimeStraightSignal.display(msg.likelyTimeStraight)
    #     self.lcdTimeRightSignal.display(msg.likelyTimeRight)
    #     QtWidgets.QApplication.processEvents()

    def GLOSAcallback(self,msg):
        self.upperSpeed.display(msg.upperSpeed)
        self.lowerSpeed.display(msg.lowerSpeed)
        self.adviceOperation.display(msg.recomendAction)
        QtWidgets.QApplication.processEvents()

    def GPScallback(self,msg):
        self.evSpeed.setText(str(GPS_connect.evSpeed))

    def OBUcallback(self,msg):
        self.dis2Stop.setText(msg.dis2StopLineStraight)
        self.interID.setText(msg.StationId)
        self.lcdTimeLeftSignal.display(msg.likelyTimeLeft)
        self.lcdTimeStraightSignal.display(msg.likelyTimeStraight)
        self.lcdTimeRightSignal.display(msg.likelyTimeRight)
        if msg.phaseIDStraight == 3:
            self.straightSignal.setStyleSheet(u"image: url(:/traffic_lights/qt_lib/straight_red.svg);")
        elif msg.phaseIDStraight == 5:
            self.straightSignal.setStyleSheet(u"image: url(:/traffic_lights/qt_lib/straight_green.svg);")
        elif msg.phaseIDStraight == 4:
            self.straightSignal.setStyleSheet(u"image: url(:/traffic_lights/qt_lib/straight_yellow.svg);")
        else:
            pass
        if msg.phaseIDRight == 3:
            self.RightSignal.setStyleSheet(u"image: url(:/traffic_lights/qt_lib/Right_red.svg);")
        elif msg.phaseIDRight == 5:
            self.RightSignal.setStyleSheet(u"image: url(:/traffic_lights/qt_lib/Right_green.svg);")
        elif msg.phaseIDRight == 4:
            self.RightSignal.setStyleSheet(u"image: url(:/traffic_lights/qt_lib/Right_yellow.svg);")
        else:
            pass
        if msg.phaseIDLeft == 3:
            self.LeftSignal.setStyleSheet(u"image: url(:/traffic_lights/qt_lib/Left_red.svg);")
        elif msg.phaseIDLeft == 5:
            self.LeftSignal.setStyleSheet(u"image: url(:/traffic_lights/qt_lib/Left_green.svg);")
        elif msg.phaseIDLeft == 4:
            self.LeftSignal.setStyleSheet(u"image: url(:/traffic_lights/qt_lib/Left_yellow.svg);")
        else:
            pass
        QtWidgets.QApplication.processEvents()

    def ros_connect(self):
        rospy.init_node('test_subscriber',anonymous=True)
        rospy.Subscriber('/test_topic',Obu_connect,testcallback)
        rospy.Subscriber('/obu_topic',Obu_connect,OBUcallback)
        rospy.Subscriber('/glosa_topic',GLOSA_connect,GLOSAcallback)
        rospy.Subscriber('/gps_output',GPS_connect,GPScallback)
        # rospy.Subscriber('mr_output',MR_connect,MRcallback)
        rospy.spinOnce()

        # self.buttonNumPv.clicked.connect(self.start_demo())
