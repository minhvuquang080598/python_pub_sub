#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import cv2
import numpy as np
from sensor_msgs.msg import CompressedImage
import sys


class image:
    def __init__(self):
        self.speed_pub = rospy.Publisher("Team1_speed",Float32,queue_size=10)
        self.steerAngle_pub = rospy.Publisher("Team1_steerAngle",Float32,queue_size=10)
        self.subscriber = rospy.Subscriber("Team1_image/compressed",CompressedImage, self.callback,  queue_size = 1)
        
        
    
    def callback(self, ros_data):
        
        np_arr = np.fromstring(ros_data.data, np.uint8)
        image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

        
        cv2.imshow('gray', gray)
        
        self.speed_pub.publish(30)
        cv2.waitKey(2)

    
    

def main(args):
    img = image()
    rospy.init_node('image_reciver', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Image feature detector module"
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
