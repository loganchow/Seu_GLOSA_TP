# This Python file uses the following encoding: utf-8
import rospy
import multithreading
from msg_list.msg import Glosa_output
from msg_list.msg import Obu_connect


def glosa(phaseID,timing,speedlimit,dis2stp):
    speedInit = dis2stp/timing
    if phaseID == 3 and speedInit<speedlimit:
        upperspeed = speedInit
        lowerspeed = 0
        advice = "BRAKE and Remian SLOW"
    elif phaseID == 5 and speedInit<speedlimit:
        upperspeed = speedlimit
        lowerspeed = speedInit
        advice = "Follow the tip"
    elif phaseID == 3 and speedInit>speedlimit:
        upperspeed = speedlimit
        lowerspeed = 0
        advice = "BRAKE and You May STOP & WAIT"
    elif phaseID == 5 and speedInit>speedlimit:
        upperspeed = speedlimit
        lowerspeed = speedlimit
        advice = "Better BRAKE and STOP & WAIT"
    return upperspeed,lowerspeed,advice


def OBUcallback(msg):
        phase = msg.phaseIDStraight
        timeleft = msg.likelyTimeStraight
        dis2stpline = msg.dis2StopLineStraight
        vlimit = msg.speedLimitStraight
        upperSpeed,lowerSpeed,advice = glosa(phase,timeleft,vlimit,dis2stpline)
        pub = rospy.Publisher('/glosa_connect',Glosa_connect,queue_size=10)
        rate = rospy.Rate(10)
        glosa_data = Glosa_output()
        glosa_data.recomendAction = advice
        glosa_data.upperSpeed = upperSpeed
        glosa_data.lowerSpeed = lowerSpeed
        pub.publish(glosa_data)
        rate.sleep()
        


def ros_connect(self):
        rospy.init_node('/test_subscriber',anonymous=True)
        # rospy.Subscriber("/test_topic",Obu_connect,testcallback)
        rospy.Subscriber('/obu_topic',Obu_connect,OBUcallback)
        rospy.spinOnce()