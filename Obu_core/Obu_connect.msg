unit8 numofTrafficLights    # 信号灯个数（单组）
unit32 StationId    # 路口ID
string createdUTC   # 第一次收到某一路口消息的时间戳(ms)
string LastModified_UTC     # 每次更新此同一路口消息的时间戳 
string InterTime_UTC    # UTC time stamp from traffic light controller
string SpatTime_UTC     # UTC time stamp from the network e.g.uu
string refLat   # 停车线坐标
string refLong
string refAlt

unit8 validStraight #工作状态
unit32 phaseIDStraight # 相位 ID
unit8 numOfSignalPhaseStraight #相位个数
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