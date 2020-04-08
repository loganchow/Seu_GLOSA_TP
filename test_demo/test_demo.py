import rospy
from Test.msg import Obu_connect

def main():
    rospy.init_node('test_publish',anonymous=True)

    test_pub = rospy.Publisher("/test_topic",Obu_connect,queue_size=50)

    rate = rospy.Rate(10)

    msg = Obu_connect()
    msg.likelyTimeLeft = 5
    msg.likelyTimeRight = 3
    msg.likelyTimeStraight = 4

    test_pub.publish(msg)

    rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
