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