# This Python file uses the following encoding: utf-8

import time,os,sys,rospy
from std_msgs.msg import String,OBU_raw

class data_resolve:
    def __init__(self):
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


# 基本信息
def data_parse_general(data,len_msg):
    stationID = data[36:40]
    stationID = stationID[3]*pow(256,3)+stationID[2]*pow(256,2)+stationID[1]*256+stationID[0]*1
    print("stationID is: %d"%stationID)
    numofTrafficLights = int(data[2])
    print("Number of Traffic Lights is: %d"%numofTrafficLights)
    createdUTC = data[4:8]
    createdUTC = createdUTC[-1]*pow(256,3)+createdUTC[-2]*pow(256,2)+createdUTC[-3]*pow(256,1)+createdUTC[-4]*pow(256,0)
    fcreatedUTC = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(createdUTC))
    print("Created UTC is: %s"%fcreatedUTC)
    key_value = data[28:32]
    SpatTimeUTC = key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0)
    fSpatTimeUTC = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(SpatTimeUTC))
    print("SPaT time is: %s"%fSpatTimeUTC)
    key_value = data[20:24]
    intertime_UTC = key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0)
    fintertime_UTC = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(intertime_UTC))
    print("Inter time is: %s"%fintertime_UTC)
    key_value = data[40:44]
    refLat_deg = key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0)
    print("Reference Latitude is:%s"%refLat_deg)
    key_value = data[44:48]
    refLong_deg = key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0)
    print("Reference Longitude is:%s"%refLong_deg)
    key_value = data[48:52]
    refAlt_m = key_value[-1]*pow(256,3)+key_value[-2]*pow(256,2)+key_value[-3]*pow(256,1)+key_value[-4]*pow(256,0)
    print("Reference Altitude is:%s\n"%refAlt_m)
    generalInfo = [stationID,numofTrafficLights,createdUTC,SpatTimeUTC,fSpatTimeUTC,intertime_UTC,fintertime_UTC,refLat_deg,refLong_deg,refAlt_m]
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
    straightInfo = [SignalState,Likelytime,dis2StopLine,speedLimit]
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
    lefttInfo = [SignalState,Likelytime,dis2StopLine,speedLimit]
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
    rightInfo = [SignalState,Likelytime,dis2StopLine,speedLimit]
    return rightInfo


def checkCallback(msg):
    pub = rospy.Publisher('obu_str',OBU_raw,queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        
        pub.publish(raw_data)
        # rospy.loginfo("OBU Output[%d ,%d ]",raw_data.payload,raw_data,len_msg)
        rate.sleep()



def main():
    rospy.init_node('data_resolve', anonymous = True)
    rospy.Subscriber('obu_str', OBU_raw, checkCallback)
    rospy.spin()



if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass

