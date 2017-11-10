#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import curses
import math
import rospy
import sys
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64


def callback(data,pub1,pub2):
    v = data.linear.x
    w = data.angular.z
    R = 0.1
    L = 0.33
    wl = (v-w*L/2)/R
    wr = (v+w*L/2)/R
    pub1.publish(wl)
    pub2.publish(wr)
    

def pioneer_driver():
    pub1 = rospy.Publisher('/pioneer_p3dx/leftWheelCommand',Float64,queue_size=10)
    pub2 = rospy.Publisher('/pioneer_p3dx/rightWheelCommand',Float64,queue_size=10)

    rospy.init_node('pioneer_driver',anonymous=True)
    rate = rospy.Rate(10) # 10hz



    rospy.Subscriber('cmd_vel',Twist,lambda data: callback(data,pub1,pub2))
         

if __name__ =="__main__":
    try:
        pioneer_driver()
    except rospy.ROSInterruptException:
        pass

    rospy.spin()
            
    
