# File created on 4/19/16
# Author: Marcelo Caldas - mscaldas@gmail.com
#
# CamJam Edukit 3 - Robotics - The Object Oriented Way
# Component - Drive train: combines both motors to move the robot.
#   This drive train assumes the robot moves with two motors.

from variableSpeedMotor import VariableSpeedMotor

class TwoByTwoDriveTrain:

    def __init__(self):
        self.motorLeft = VariableSpeedMotor(9, 10)
        self.motorRight = VariableSpeedMotor(8, 7)

    # TURN all motors off
    def stopMotors(self):
        self.motorLeft.stopMotors()
        self.motorRight.stopMotors()

    # turn BOTH motors fowards
    def fowards(self):
        self.motorLeft.fowards()
        self.motorRight.fowards()

    # turn BOTH motors backwards
    def backwards(self):
        self.motorLeft.backwards()
        self.motorRight.backwards()

    # turn right
    def right(self):
        self.motorLeft.backwards()
        self.motorRight.fowards()

    # turn left
    def left(self):
        self.motorLeft.fowards()
        self.motorRight.backwards()

  