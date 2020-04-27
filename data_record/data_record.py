# -*- coding:UTF-8 -*-
import socket
import time
import os
import math
import xlrd
import xlwt
from xlutils.copy import copy
import rospy
from Obu_connect.msg import Obu_connect


# 设定 Excel 表格格式
def set_style(name,height,bold=False):
	style = xlwt.XFStyle()
	font = xlwt.Font()
	font.name = name
	font.bold = bold
	font.color_index = 4
	font.height = height
	style.font = font
	return style

# 创建 Excel 表格
def create_excel():
	f = xlwt.Workbook()
	sheet1 = f.add_sheet('sheet1',cell_overwrite_ok = True)
	row0_0 = ['Order','stationID','numofTrafficLights','createdUTC','SpatTimeUTC','fSpatTimeUTC','intertime_UTC','fintertime_UTC','refLat_deg','refLong_deg','refAlt_m']
	row0_1 = ['StraightSignalState','Likelytime','dis2StopLine','speedLimit']
	# row0_2 = ['LeftSignalState','Likelytime','dis2StopLine','speedLimit']
	# row0_3 = ['RightSignalState','Likelytime','dis2StopLine','speedLimit']
	# row0 = row0_0 + row0_1 + row0_2 + row0_3
	row0 = row0_0 + row0_1
	for  j in range(len(row0)):
		sheet1.write(0,j,row0[j])
	filename = time.strftime("%Y%m%d%H%M%S",time.localtime())
	filename = filename + '.xls'
	f.save(filename)
	sFileName = str(filename)
	print(sFileName)
	return sFileName

# 数据迭代写入
def write_excel(filename,gnrlInfo,strgtInfo,i,*avrc,**avrg):
	file_path = os.getcwd()
	file_name = file_path + '\\' + filename
	wb = xlrd.open_workbook(file_name)
	f = copy(wb)
	sheet1 = f.get_sheet(0)
	row_i = [i]+gnrlInfo + strgtInfo
	# row_i = [i]+gnrlInfo + strgtInfo + lftInfo + rightInfo
	for id in range(len(row_i)):
		sheet1.write(i,id, row_i[id])
	f.save(file_name)

# ROS 回调函数
def recordCallback(msg):
    file_name = create_excel()
	i = 0
	gInfo = [msg.StationId,msg.numofTrafficLights,msg.createdUTC,msg.SpatTime_UTC,msg.InterTime_UTC]
	sInfo = [msg.phaseIDStraight,msg.likelyTimeStraight,msg.dis2StopLineStraight,msg.speedLimitStraight]
    write_excel(file_name,gInfo,sInfo,i)

def main():
        rospy.init_node('test_subscriber',anonymous=True)
        rospy.Subscriber('/test_topic',Obu_connect,recordCallback)
        rospy.spinOnce()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass