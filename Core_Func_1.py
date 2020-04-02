# -*- coding:UTF-8 -*-
import socket, time, os, math ,rospy
import Obu_connect.msg

# import xlrd
# import xlwt
# from xlutils.copy import copy

def fourbytes(key_value):
    return key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0)

# 建立socket连接
def socket_connect():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('192.168.79.55',36730))

    data, addr = s.recvfrom(1024)
    # print('Received from %s:%s.' % addr)
    # print("Recived raw: %s"%data)
    # print("Data raw length: %s"%len(data))

    time.sleep(0.5)

    return data

# 数据完整性检验
def veri_complete(data_raw):
    lenm = [0,0] #存储消息体长度
    lenm[0] = data_raw[5]
    lenm[1] = data_raw[6]
    len_msg = int(lenm[1]*256+lenm[0])
    # print("Message length is: %d"%len_msg)
    payload =data_raw[8:-1]
    return payload,len_msg

# 基本信息
def data_parse_general(data,len_msg):
    # StationID
    stationID = data[36:40]
    stationID = stationID[3]*pow(256,3)+stationID[2]*pow(256,2)+stationID[1]*256+stationID[0]*1
    print("stationID is: %d"%stationID)
    # numofTrafficLights
    numofTrafficLights = int(data[2])
    print("Number of Traffic Lights is: %d"%numofTrafficLights)
    # createdUTC
    createdUTC = data[8:12]
    createdUTC = createdUTC[-1]*pow(256,3)+createdUTC[-2]*pow(256,2)+createdUTC[-3]*pow(256,1)+createdUTC[-4]*pow(256,0)
    fcreatedUTC = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(createdUTC))
    print("Created UTC is: %s"%fcreatedUTC)
    # LastModifiedUTC
    key_value = data[16:20]
    LastModifiedUTC = key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0)
    fLastModifiedUTC = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(LastModifiedUTC))
    print("LastModified UTC is: %s"%fLastModifiedUTC)
    # SpatTimeUTC
    key_value = data[28:32]
    SpatTimeUTC = key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0)
    fSpatTimeUTC = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(SpatTimeUTC))
    print("SPaT time is: %s"%fSpatTimeUTC)
    # InterTimeUTC
    key_value = data[20:24]
    intertime_UTC = key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0)
    fintertime_UTC = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(intertime_UTC))
    print("Inter time is: %s"%fintertime_UTC)
    # refLatitude_deg
    key_value = data[40:44]
    refLat_deg = key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0)
    print("Reference Latitude is:%s"%refLat_deg)
    # refLongitude_deg
    key_value = data[44:48]
    refLong_deg = key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0)
    print("Reference Longitude is:%s"%refLong_deg)
    # refAltitude_m
    key_value = data[48:52]
    refAlt_m = key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0)
    print("Reference Altitude is:%s\n"%refAlt_m)
    generalInfo = [numofTrafficLights,stationID,fcreatedUTC,fLastModifiedUTC,fintertime_UTC,fSpatTimeUTC,refLat_deg,refLong_deg,refAlt_m]
    return generalInfo

# 直行
def data_parse_left(data,len_msg):
    print("***State of STRAIGHT Lane***")
    # 当前路口运行状况
    key_value = data[52]
    Valid_state = key_value
    print("Valid State is: %d"%Valid_state)
    # 当前信号相位个数
    key_value = data[68]
    numOfSignalPhase = key_value
    print("Number of Signal Phase is: %d"%numOfSignalPhase)
    # 相位ID
    key_value = data[56:60]
    phaseID = fourbytes(key_value)
    print("Staright PhaseID is: %d"%phaseID)
    # 当前信号灯状态
    SignalState = int(data[69])
    if SignalState == 0 :
        SignalState = 'Unavailable'
    elif SignalState == 1:
        SignalState = 'DARK'
    elif SignalState == 2:
        SignalState = 'STOP_THEN_PROCEED'
    elif SignalState == 3:
        SignalState = 'STOP_AND_REMAIN'
    elif SignalState == 4:
        SignalState = 'PRE_MOVEMENT'
    elif SignalState == 5:
        SignalState = 'PERMISSIVE_MOVEMENT_ALLOWED'
    elif SignalState == 6:
        SignalState = 'PROTECTED_MOVEMENT_ALLOWED'
    elif SignalState == 7:
        SignalState = 'PERMISSIVE_CLEARANCE'
    elif SignalState == 8:
        SignalState = 'PROTECTED_CLEARANCE'
    elif SignalState == 9:
        SignalState = 'CAUTION_CONFLICTING_TRAFFIC'
    print("Signal State of STRAIGHT is: %s"%SignalState)
    # 当前相位剩余时间
    key_value = data[74:76]
    Likelytime = 0.1*(key_value[1]*pow(256,1)+key_value[0]*pow(256,0))
    print("STRAIGHT Likely End time is: %.2f s."%Likelytime)
    # 到停车线距离
    key_value = data[64:68]
    dis2StopLine = 0.1*(key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0))
    print("Distance to STRAIGHT stop line is: %.2f m."%dis2StopLine)
    # 当前道路限速
    key_value = data[60:64]
    speedLimit = 0.0036*(key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0))
    print("Speed Limit is: %.2f km/h."%speedLimit)
    # 最大结束时间
    key_value = data[72:74]
    maxEndTime = 0.1*(key_value[1]*pow(256,1)+key_value[0]*pow(256,0))
    print("Maximum End time is: %.2f s."%maxEndTime)
    # 最小结束时间
    key_value = data[70:72]
    minEndTime = 0.1*(key_value[1]*pow(256,1)+key_value[0]*pow(256,0))
    print("Minimum End time is: %.2f s.\n"%minEndTime)
    straightInfo = [Valid_state,phaseID,numOfSignalPhase,speedLimit,dis2StopLine,SignalState,Likelytime]
    return straightInfo

# 左转
def data_parse_straight(data,len_msg):
    print("***State of LEFT Lane***")
    # 当前路口运行状况
    key_value = data[125]
    Valid_state = key_value
    print("Valid State is: %d"%Valid_state)
    # 当前信号相位个数
    key_value = data[141]
    numOfSignalPhase = key_value
    print("Number of Signal Phase is: %d"%numOfSignalPhase)
    # 相位ID
    key_value = data[129:133]
    phaseID = fourbytes(key_value)
    print("Left PhaseID is: %d"%phaseID)
    # 当前信号灯状态
    SignalState = int(data[142])
    if SignalState == 0 :
        SignalState = 'Unavailable'
    elif SignalState == 1:
        SignalState = 'DARK'
    elif SignalState == 2:
        SignalState = 'STOP_THEN_PROCEED'
    elif SignalState == 3:
        SignalState = 'STOP_AND_REMAIN'
    elif SignalState == 4:
        SignalState = 'PRE_MOVEMENT'
    elif SignalState == 5:
        SignalState = 'PERMISSIVE_MOVEMENT_ALLOWED'
    elif SignalState == 6:
        SignalState = 'PROTECTED_MOVEMENT_ALLOWED'
    elif SignalState == 7:
        SignalState = 'PERMISSIVE_CLEARANCE'
    elif SignalState == 8:
        SignalState = 'PROTECTED_CLEARANCE'
    elif SignalState == 9:
        SignalState = 'CAUTION_CONFLICTING_TRAFFIC'
    print("Signal State of LEFT is: %s"%SignalState)
    # 当前相位剩余时间
    key_value = data[147:149]
    Likelytime = 0.1*(key_value[1]*pow(256,1)+key_value[0]*pow(256,0))
    print("LEFT Likely End time is: %.2f s."%Likelytime)
    # 到停车线距离
    key_value = data[137:141]
    dis2StopLine = 0.1*(key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0))
    print("Distance to LEFT stop line is: %.2f m."%dis2StopLine)
    # 当前道路限速
    key_value = data[133:137]
    speedLimit = 0.0036*(key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0))
    print("Speed Limit is: %.2f km/h."%speedLimit)
    # 最大结束时间
    key_value = data[145:147]
    maxEndTime = 0.1*(key_value[1]*pow(256,1)+key_value[0]*pow(256,0))
    print("Maximum End time is: %.2f s."%maxEndTime)
    # 最小结束时间
    key_value = data[143:145]
    minEndTime = 0.1*(key_value[1]*pow(256,1)+key_value[0]*pow(256,0))
    print("Minimum End time is: %.2f s.\n"%minEndTime)
    lefttInfo = [Valid_state,phaseID,numOfSignalPhase,speedLimit,dis2StopLine,SignalState,Likelytime]
    return lefttInfo  

# 右转
def data_parse_right(data,len_msg):
    print("***State of RIGHT Lane***")
    # 当前路口运行状况
    key_value = data[198]
    Valid_state = key_value
    print("Valid State is: %d"%Valid_state)
    # 当前信号相位个数
    key_value = data[214]
    numOfSignalPhase = key_value
    print("Number of Signal Phase is: %d"%numOfSignalPhase)
    # 相位ID
    key_value = data[202:206]
    phaseID = fourbytes(key_value)
    print("Right PhaseID is: %d"%phaseID)
    # 当前信号灯状态
    SignalState = int(data[215])
    if SignalState == 0 :
        SignalState = 'Unavailable'
    elif SignalState == 1:
        SignalState = 'DARK'
    elif SignalState == 2:
        SignalState = 'STOP_THEN_PROCEED'
    elif SignalState == 3:
        SignalState = 'STOP_AND_REMAIN'
    elif SignalState == 4:
        SignalState = 'PRE_MOVEMENT'
    elif SignalState == 5:
        SignalState = 'PERMISSIVE_MOVEMENT_ALLOWED'
    elif SignalState == 6:
        SignalState = 'PROTECTED_MOVEMENT_ALLOWED'
    elif SignalState == 7:
        SignalState = 'PERMISSIVE_CLEARANCE'
    elif SignalState == 8:
        SignalState = 'PROTECTED_CLEARANCE'
    elif SignalState == 9:
        SignalState = 'CAUTION_CONFLICTING_TRAFFIC'
    print("Signal State of RIGHT is: %s"%SignalState)
    # 当前相位剩余时间
    key_value = data[220:222]
    Likelytime = 0.1*(key_value[1]*pow(256,1)+key_value[0]*pow(256,0))
    print("RIGHT Likely End time is: %.2f s."%Likelytime)
    # 到停车线距离
    key_value = data[210:214]
    dis2StopLine = 0.1*(key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0))
    print("Distance to RIGHT stop line is: %.2f m."%dis2StopLine)
    # 当前道路限速
    key_value = data[206:210]
    speedLimit = 0.0036*(key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0))
    print("Speed Limit is: %.2f km/h."%speedLimit)
    # 最大结束时间
    key_value = data[218:220]
    maxEndTime = 0.1*(key_value[1]*pow(256,1)+key_value[0]*pow(256,0))
    print("Maximum End time is: %.2f s."%maxEndTime)
    # 最小结束时间
    key_value = data[216:218]
    minEndTime = 0.1*(key_value[1]*pow(256,1)+key_value[0]*pow(256,0))
    print("Minimum End time is: %.2f s.\n"%minEndTime)   
    rightInfo = [Valid_state,phaseID,numOfSignalPhase,speedLimit,dis2StopLine,SignalState,Likelytime]
    return rightInfo


def main():
    rospy.init_node('obu_output', anonymous = True)
    pub = rospy.Publisher('obu_data',Obu_connect,queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        data_raw_b = socket_connect()
        payload, msg_len = veri_complete(data_raw_b)
        gInfo = data_parse_general(payload, msg_len)
        lInfo = data_parse_left(payload, msg_len)
        sInfo = data_parse_straight(payload, msg_len)
        rInfo = data_parse_right(payload, msg_len)
        raw_data = Obu_connect()
        raw_data.numofTrafficLights = gInfo[0]
        raw_data.StationID = gInfo[1]
        raw_data.createdUTC = gInfo[2]
        raw_data.LastModified_UTC = gInfo[3]
        raw_data.InterTime_UTC = gInfo[4]
        raw_data.SpatTime_UTC = gInfo[5]
        raw_data.refLat = gInfo[6]
        raw_data.refLong = gInfo[7]
        raw_data.refAlt = gInfo[8]

        raw_data.validStraight = sInfo[0]
        raw_data.phaseIDStraight = sInfo[1]
        raw_data.numOfSignalPhaseStraight = sInfo[2]
        raw_data.speedLimitStraight = sInfo[3]
        raw_data.dis2StopLineStraight = sInfo[4]
        raw_data.signalStateStraight = sInfo[5]
        raw_data.likelyTimeStraight = sInfo[6]

        raw_data.validLeft = lInfo[0]
        raw_data.phaseIDLeft = lInfo[1]
        raw_data.numOfSignalPhaseLeft = lInfo[2]
        raw_data.speedLimitLeft = lInfo[3]
        raw_data.dis2StopLineLeft = lInfo[4]
        raw_data.signalStateLeft = lInfo[5]
        raw_data.likelyTimeLeft = lInfo[6]

        raw_data.validRight = rInfo[0]
        raw_data.phaseIDRight = rInfo[1]
        raw_data.numOfSignalPhaseRight = rInfo[2]
        raw_data.speedLimitRight = rInfo[3]
        raw_data.dis2StopLineRight = rInfo[4]
        raw_data.signalStateRight = rInfo[5]
        raw_data.likelyTimeRight = rInfo[6]
        
        pub.publish(raw_data)
        # rospy.loginfo("OBU Output[%d ,%d ]",raw_data.payload,raw_data,len_msg)
        rate.sleep()
    


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass