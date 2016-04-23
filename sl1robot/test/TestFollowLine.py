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
                self.robot.fowards()
                time.sleep(0.01)
                self.robot.stopMotors()
                if not self.robot.isOnLine():
                    self.robot.findLine()

        except KeyboardInterrupt:
            self.robot.stopMotors()
            GPIO.cleanup()
            quit()

if __name__ == '__main__':
    unittest.main()

