# File created on 4/19/16
# Author: Marcelo Caldas - mscaldas@gmail.com
#
import unittest
import RPi.GPIO as GPIO
from random import randint

import time

from sl1robot.camJamRobot import CamJamRobot


class TestRobotMovement(unittest.TestCase):

    def setUp(self):
        self.robot = CamJamRobot()

    def test_randomMovement(self):
        try:
            directions = {0: self.robot.fowards,
                          1: self.robot.backwards,
                          2: self.robot.left,
                          3: self.robot.right}
            while True:
                dir = randint(0, 3)
                directions[dir]()
                time.sleep(1)
                self.robot.stop()
                time.sleep(0.2)
        except KeyboardInterrupt:
            GPIO.cleanup()
            quit()

    def test_SquareMovement(self):
        for step in range(0, 4):
            self.robot.left()
            time.sleep(0.22)
            self.robot.stop()
            time.sleep(0.1)

            self.robot.fowards()
            time.sleep(1)
            self.robot.stop()
            time.sleep(0.2)

        self.robot.stop()
        GPIO.cleanup()

if __name__ == '__main__':
  unittest.main()
