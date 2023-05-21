#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import numpy as np
import time
import rospy

from sensor_msgs.msg import Joy
from blower_control.msg import BlowerCmd

#ROS
node_cycle = 100 #[Hz]

#ros message
cmd_msg = BlowerCmd()

btn_info = [0,0,0,0,0,0,0,0,0,0,0,0,0]
axs_info = [0,0,0,0,0,1,0,0]

def callback_joy(joy_msg):
    global btn_info
    global axs_info
    btn_info = joy_msg.buttons
    axs_info = joy_msg.axes

def status_print():
    global btn_info
    global axs_info
    global cmd_msg

    print("[joy status]----------------------------")
    print(btn_info)
    print(axs_info)
    print("[control status]------------------------")
    print("motor cmd : %d" %cmd_msg.motor_ctrl)


def main():
    global cmd_msg
    global axs_info

    #ros node setting -------------------------------------------------
    #initialize ros node
    rospy.init_node('joy_ope_node', anonymous=True)
    #set loop rate per second [Hz]
    cycle_rate = rospy.Rate(node_cycle)
    #subscriber
    rospy.Subscriber("joy", Joy, callback_joy, queue_size=2) #Joycon 
    #publisher
    pub = rospy.Publisher('blower_cmd', BlowerCmd, queue_size=1)
    #-----------------------------------------------------------------

    cmd_msg.motor_ctrl  =  0

    while not rospy.is_shutdown():
        #control
        #wireless
        #cmd_msg.left_motor  = int(axs_info[1] * 511)
        #cmd_msg.right_motor = int(axs_info[4] * 511)
        #wire
        cmd_msg.motor_ctrl  = -int((axs_info[5]-1)/2 * 511)
        status_print()

        #publish
        pub.publish(cmd_msg)

        #sleep
        cycle_rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: pass
