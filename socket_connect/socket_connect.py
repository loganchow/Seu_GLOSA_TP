# This Python file uses the following encoding: utf-8

import sys, socket, time, rospy
import OBU_raw

class socket_connect:
    def __init__(self):
        self.port = 15676
        self.ip = '192.168.79.55'
    def connect(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.s.bind((self.ip,self.port))
        self.data,self.addr = self.s.recvfrom(1024)
        time.sleep(0.5)
        return self.data

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

# def checkCallback(msg):
#     while msg == False:
#         pass
#     else:
#         SC = socket_connect()
#         data = SC.connect()
#     return data

def main():
    rospy.init_node('socket_connect', anonymous = True)
    # rospy.Subscriber('obu_check', bool, checkCallback)
    pub = rospy.Publisher('obu_str',OBU_raw,queue_size=10)
    rate = rospy.Rate(10)
    # rospy.spin()
    while not rospy.is_shutdown():
        SC = socket_connect()
        data = SC.connect()
        raw_data = OBU_raw()
        DR = data_resolve()
        raw_data.payload,raw_data.len_msg = DR.data_veri(data)
        pub.publish(raw_data)
        # rospy.loginfo("OBU Output[%d ,%d ]",raw_data.payload,raw_data,len_msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
