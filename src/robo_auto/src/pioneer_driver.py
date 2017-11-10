#! /usr/bin/env python
# -*- coding: utf-8 -*-
import curses
import math
import rospy
import sys
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

def callback(publeft,pubright,cmd):
    w = cmd.angular.z
    v = cmd.linear.x+cmd

    def pioneer_drive():
        rospy.init_node('pioneer driver',anonyme=True)

        publeft= rospy.Publisher('/pioneer_p3dx/leftWheelCommand',Float64,queue_size=10)
        pubright=rospy.Publisher('/pioneer_p3dx/rightWheelCommand',Float64,queue_size=10)
        rospy.Subscriber("/cmd_vel",Twist,lambda cmd : callback(cmd,publeft,pubright))

        rospy.spin()

        rate=rospy.Rate(10) #10Hz
