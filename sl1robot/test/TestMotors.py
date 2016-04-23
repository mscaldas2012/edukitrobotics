# File created on 4/19/16
# Author: Marcelo Caldas - mscaldas@gmail.com
#

import unittest

from sl1robot.camJamRobot import CamJamRobot
import time
import logging



class TestMotors(unittest.TestCase):

    def setUp(self):
        self.robot = CamJamRobot()

    def test_constant_speed_motor(self):
        logging.info("Make sure Robot is moving foward at constant speed")
        self.robot.fowards()
        time.sleep(1)
        self.robot.stopMotors()
        self.robot.right()
        time.sleep(1)
        self.robot.stopMotors()
        self.robot.fowards()
        time.sleep(1)
        self.robot.stopMotors()
        self.robot.backwards()
        time.sleep(1)
        self.robot.stopMotors()
        self.robot.left()
        time.sleep(1)
        self.robot.stopMotors()

    def test_variable_speed_motor(self):
        logging.info("Check if Robot is moving slower than before...")


if __name__ == '__main__':
    unittest.main()

