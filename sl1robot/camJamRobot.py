# File created on 4/19/16
# Author: Marcelo Caldas - mscaldas@gmail.com
#
# CamJam Edukit 3 - Robotics - The Object Oriented Way
# Robot Class
# This class represents The robot itself - it collects all its sensors, motors and basic logic to make them work.
# All sensors should be encapsulated withing this class. Programs using the robot, should not worry about any of the
# sensors per say, only the functionality they provide.

import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # import the time libray

from distanceSensor import DistanceSensor
from sl1robot.twoByTwoDriveTrain import TwoByTwoDriveTrain
from lineSensor import LineSensor


class CamJamRobot:
    driveTrain = TwoByTwoDriveTrain()
    distanceSensor = DistanceSensor()
    lineSensor = LineSensor()

    # Distance valirables
    SAFE_DISTANCE = 10.0
    REVERSE_TIME = 0.3
    TURN_TIME = 0.3

    def __init__(self):
        # set variables for the GPIO modes
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def stop(self):
        self.driveTrain.stopMotors()

    def fowards(self):
        self.driveTrain.fowards()

    def backwards(self):
        self.driveTrain.backwards()

    def right(self):
        self.driveTrain.right()

    def left(self):
        self.driveTrain.left()

    def isNearObstacle(self):
        return self.distanceSensor.measure() < self.SAFE_DISTANCE

    def avoidObstacle(self):
        # Backoff a little:
        self.backwards()
        time.sleep(self.REVERSE_TIME)
        self.stop()

        # For now, simply turn:
        self.right()
        time.sleep(self.TURN_TIME)
        self.stop()

    def isOnLine(self):
        return self.lineSensor.canSeeLine()

    def findLine(self):
        if self.isOnLine:
            print("Seems like the bot is right on track...")
            return
        else:
            # Try finding the line on the right:
            maxTime = 4
            time = 1
            found = False
            while not found & time <= maxTime:
                print("Trying to find the line to the right... " + time)
                self.right()
                time.sleep(0.1)
                self.stop()
                found = self.isOnLine()
                time += 1
            # Try to find the line on the left
            if not found:
                print("Nops.. not on the right.. let's look on the left...")
                self.left()
                time.sleep(maxTime)  # Return to starting point...
                time = 1
                while not found & time <= maxTime:
                    print("Looking for the line on the left: " + time)
                    self.left()
                    time.sleep(0.1)
                    found = self.isOnLine()
                    time +=1
            if not found:
                print("Sorry Got Lost!")
