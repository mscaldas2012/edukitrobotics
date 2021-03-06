# File created on 4/23/16
# Author: Marcelo Caldas - mscaldas@gmail.com
#
# CamJam Edukit 3 - Robotics - The Object Oriented Way
# Follow The Line testing
# This is for testing how well the robot can follow the line.

import unittest

import RPi.GPIO as GPIO
from sl1robot.camJamRobot import CamJamRobot
import time

class TestFollowLine(unittest.TestCase):

    def setUp(self):
        self.robot = CamJamRobot()

    def test_followLine(self):
        try:

            while True:
                if self.robot.isOnLine():
                    self.robot.fowards()
                    time.sleep(0.01)
                    self.robot.stop()
                else:
                    self.robot.findLine()

        except KeyboardInterrupt:
            self.robot.stop()
            GPIO.cleanup()
            quit()

if __name__ == '__main__':
    unittest.main()

