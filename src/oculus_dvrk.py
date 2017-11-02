#!/usr/bin/env python

import roslib
import rospy
import sys
import serial
from math import pi
from sensor_msgs.msg import JointState
from tf2_msgs.msg import TFMessage

jnt_msg = JointState()

def callback(data):
	global roll, pitch
	roll = data.transforms[0].transform.rotation.x
	pitch = data.transforms[0].transform.rotation.z

def control_daVinci():
	jnt_pub = rospy.Publisher('/dvrk/PSM1/set_position_joint', JointState, queue_size = 10)
	imu_sub = rospy.Subscriber('/tf', TFMessage, callback)
	rospy.init_node('oculus_dvrk', anonymous = True)

	roll = 0
	pitch = 0
	deg_to_rad = pi / 180
	jnt_msg.position = [0,0,0,0,0,0,0]

	while not rospy.is_shutdown():
 		jnt_msg.position[0] = roll * deg_to_rad
 		jnt_msg.position[1] = pitch * deg_to_rad
		jnt_pub.publish(jnt_msg)

if __name__ == '__main__':
	control_daVinci()
