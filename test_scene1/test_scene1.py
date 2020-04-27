# This Python file uses the following encoding: utf-8
import random
import rospy
from msg_list.msg import Obu_connect

def rospub():
    pub = rospy.Publisher('/test_topic', Obu_connect, queue_size=10)
    rospy.init_node('test_scene1', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = Obu_connect()
        msg.evSpeed = random.randint(0,60)
        msg.dis2StopLineStraight = random.randint(20,200)
        msg.phaseIDStraight = random.choice([3,5])
        msg.speedLimitStraight = 60
        msg.likelyTimeStraight = random.randint(0,60)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospub()
    except rospy.ROSInterruptException:
        pass