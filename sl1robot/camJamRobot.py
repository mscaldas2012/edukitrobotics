# File created on 4/19/16
# Author: Marcelo Caldas - mscaldas@gmail.com
#
# CamJam Edukit 3 - Robotics - The Object Oriented Way
# Robot Class
# This class represents The robot itself - it collects all its sensors, motors and basic logic to make them work.
# All sensors should be encapsulated withing this class. Programs using the robot, should not worry about any of the
# sensors per say, only the functionality they provide.

import RPi.GPIO as GPIO # Import the GPIO Library
import time # import the time libray

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
    #set variables for the GPIO modes
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

  def stopMotors(self):
    self.driveTrain.stopMotors()

  def fowards (self):
    self.driveTrain.fowards()

  def backwards (self):
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
    self.stopMotors()

    # For now, simply turn:
    self.right()
    time.sleep(self.TURN_TIME)
    self.stopMotors()


  def isOnLine(self):
    return self.lineSensor.isOnLine()

  def findLine(self):
    if (self.isOnLine):
      return
    else:
      # Try finding the line on the right:
      maxTime = 0.4
      time = 0.1
      found = False
      while not found & time <= maxTime:
        self.right()
        time.sleep(time)
        self.stopMotors()
        found = self.isOnLine()
        time += + 0.1
      #Try to find the line on the left
      if not found:
        self.left()
        time.sleep(maxTime) # Return to starting point...
        time = 0.1;
        while not found & time <= maxTime:
          self.left()
          time.sleep(time)
          found = self.isOnLine()
          time += 0.1
      if not found:
        print("Sorry Got Lost!")
      

