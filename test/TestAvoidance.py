# File created on 4/19/16
# Author: Marcelo Caldas - mscaldas@gmail.com
#
# This tests whether the Robot is avoiding obstacles properly.
# The logic is that every time the robot is close to an bostacle, it should turn right and try to move on.
# if still stuck, it will keep turning right.


import unittest

import RPi.GPIO as GPIO
from camJamRobot import CamJamRobot
import time

class TestAvoidance(unittest.TestCase):

    def setUp(self):
        self.robot = CamJamRobot()

    def test_avoidObstacles(self):
        try:
            while True:
                self.robot.fowards()
                time.sleep(0.1)
                if self.robot.isNearObstacle():
                    self.robot.stopMotors()
                    self.robot.avoidObstacle()

        except KeyboardInterrupt:
            self.robot.stopMotors()
            GPIO.cleanup()
            quit()

if __name__ == '__main__':
    unittest.main()