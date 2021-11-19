#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import atan2, sqrt

def inst_pose(xy):
    global turtle_x, turtle_y, turtle_theta
    turtle_x = xy.x
    turtle_y = xy.y
    turtle_theta = xy.theta


if __name__ == "__main__":
    rospy.init_node("setpoint_position", anonymous=True)

    cmdvel_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    cmdvel_sub = rospy.Subscriber("/turtle1/pose", Pose, inst_pose)
    vmsg = Twist()
    pose = Pose()
    
    x = float(input("X axis input:"))
    y = float(input("Y axis input:"))

    k_linear = 1
    k_angular = 5

    freq = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        dist = sqrt((x - turtle_x)**2 + (y - turtle_y)**2)
        angle = atan2(y - turtle_y, x - turtle_x) - turtle_theta
        
        vmsg.linear.x = k_linear * dist
        vmsg.angular.z = (k_angular * angle)
        cmdvel_pub.publish(vmsg)

        print(vmsg.angular.z)

        freq.sleep()

        if dist <= 0.1:
            vmsg.linear.x = 0
            vmsg.angular.z = 0
            cmdvel_pub.publish(vmsg)
            break

