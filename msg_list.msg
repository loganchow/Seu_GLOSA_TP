# OBU -> Data_Record,GUI
unit8 version   #协议版本
unit8 numofTrafficLights    # 信号灯个数（单组）
unit32 createdUTC   # 第一次收到某一路口消息的时间戳(ms)
unit32 LastModified_UTC     # 每次更新此同一路口消息的时间戳 
unit32 InterTime_UTC    # UTC time stamp from traffic light controller
unit32 SpatTime_UTC     # UTC time stamp from the network e.g.uu
unit32 StationId    # 路口ID
unit32 refLat   # 停车线坐标
unit32 refLong
unit32 refAlt

unit8 validStraight #工作状态
unit8 maxLaneConfidenceStraight 
unit32 phaseIDStraight # 相位 ID
unit32 speedLimitStraight # 当前车道限速
unit32 dis2StopLineStraight # 距停车线距离
unit8 numOfSignalPhasesStraight # 信号灯可能状态数
unit8 signalStateStraight # 信号灯状态
unit16 minEndTimeStraight
unit16 maxEndTimeStraight
unit16 likelyTimeStraight # 剩余时间

unit8 validLeft
unit8 maxLaneConfidenceLeft
unit32 phaseIDLeft
unit32 speedLimitLeft
unit32 dis2StopLineLeft
unit8 numOfSignalPhasesLeft
unit8 signalStateLeft
unit16 minEndTimeLeft
unit16 maxEndTimeLeft
unit16 likelyTimeLeft

unit8 validRight
unit8 maxLaneConfidenceRight
unit32 phaseIDRight
unit32 speedLimitRight
unit32 dis2StopLineRight
unit8 numOfSignalPhasesRight
unit8 signalStateRight
unit16 minEndTimeRight
unit16 maxEndTimeRight
unit16 likelyTimeRight


# OBU -> GUI
unit8 numofTrafficLights    # 信号灯个数（单组）
unit32 createdUTC   # 第一次收到某一路口消息的时间戳(ms)
unit32 LastModified_UTC     # 每次更新此同一路口消息的时间戳 
unit32 InterTime_UTC    # UTC time stamp from traffic light controller
unit32 SpatTime_UTC     # UTC time stamp from the network e.g.uu
unit32 StationId    # 路口ID
unit32 refLat   # 停车线坐标
unit32 refLong
unit32 refAlt

unit8 validStraight #工作状态
unit32 phaseIDStraight # 相位 ID
unit32 speedLimitStraight # 当前车道限速
unit32 dis2StopLineStraight # 距停车线距离
unit8 signalStateStraight # 信号灯状态
unit16 likelyTimeStraight # 剩余时间

unit8 validLeft
unit32 phaseIDLeft
unit32 speedLimitLeft
unit32 dis2StopLineLeft
unit8 signalStateLeft
unit16 likelyTimeLeft

unit8 validRight
unit32 phaseIDRight
unit32 speedLimitRight
unit32 dis2StopLineRight
unit8 signalStateRight
unit16 likelyTimeRight

# OBU -> GLOSA
unit32 phaseIDStraight # 相位 ID
unit32 speedLimitStraight # 当前车道限速
unit32 dis2StopLineStraight # 距停车线距离
unit8 signalStateStraight # 信号灯状态
unit16 likelyTimeStraight # 剩余时间

unit32 phaseIDLeft
unit32 speedLimitLeft
unit32 dis2StopLineLeft
unit8 signalStateLeft
unit16 likelyTimeLeft

unit32 phaseIDRight
unit32 speedLimitRight
unit32 dis2StopLineRight
unit8 signalStateRight
unit16 likelyTimeRight

Glosa_output:
    unit32 upperSpeed   # 速度区间上限
    unit32 lowerSpeed   # 速度区间下限
    string recomendAction    # 推荐操作（[STOP(1), ACCELERATE_AND_CONTINUE(2), DECELERATE_AND_CONTINUE(3), MAINTAIN(0)]）

# GLOSA -> DataRecord
unit32 upperSpeed
unit32 lowerSpeed
string recomendAction

# GUI -> DataRecord
unit8 numOfPreceedVehicle
BOOL startRecord
BOOL stopRecord
BOOL saveFile
string savePath     # 存储路径用string可以吗

# GUI -> OBU
BOOL socketConnect
BOOL socketDisconnect

# GUI -> GLOSA
BOOL startGLOSA
BOOL stopGLOSA

# MillimeterRadar -> GUI


# GPS -> GUI